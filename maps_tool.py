# maps_tool.py

import requests
GOOGLE_MAPS_API_KEY=""


def search_places(preferences, lat, lng):

    # =====================================
    # Step 1: Build Query
    # =====================================

    query = f"""
    {preferences.get("keywords") or ""}
    {preferences.get("cuisine") or ""}
    {preferences.get("type") or ""}
    """

    query = query.strip()

    # =====================================
    # Step 2: Radius
    # =====================================

    radius = 5000

    max_distance = preferences.get("max_distance_km")

    if max_distance:
        radius = max_distance * 1000

    radius = max(500, min(radius, 50000))

    # =====================================
    # Step 3: Google Places API
    # =====================================

    print("\n[Tool] Calling Google Places API...")

    url = (
        "https://maps.googleapis.com/maps/api/place/"
        "textsearch/json"
    )

    params = {
        "query": query,
        "key": GOOGLE_MAPS_API_KEY,
        "location": f"{lat},{lng}",
        "radius": radius,
    }

    response = requests.get(url, params=params)

    data = response.json()

    results = data.get("results", [])

    if not results:
        return []

    # =====================================
    # Step 4: Extract Places
    # =====================================

    places = []

    for place in results[:10]:

    # Photo URL
        photo_reference = (
        place.get("photos", [{}])[0]
        .get("photo_reference")
        if place.get("photos")
        else None
    )

        photo_url = None

        if photo_reference:

            photo_url = (
            "https://maps.googleapis.com/maps/api/place/photo"
            f"?maxwidth=400"
            f"&photo_reference={photo_reference}"
            f"&key={GOOGLE_MAPS_API_KEY}"
        )

    # =====================================
    # Place Object
    # =====================================

        places.append({

            "name":
                place.get("name"),

            "rating":
                place.get("rating"),

            "address":
                place.get("formatted_address"),

            "price_level":
                place.get("price_level"),

            "location":
                place.get("geometry", {}).get("location"),

            "photo_reference":
                place.get("photos", [{}])[0].get("photo_reference")
                if place.get("photos")
                else None,
            
            "photo_url":
            photo_url
        })

    print(f"\n[Tool] Found {len(places)} candidate places")

    # =====================================
    # Step 5: Routes API
    # =====================================

    print("\n[Tool] Computing travel distances...")

    route_url = (
        "https://routes.googleapis.com/"
        "distanceMatrix/v2:computeRouteMatrix"
    )

    body = {

        "origins": [
            {
                "waypoint": {
                    "location": {
                        "latLng": {
                            "latitude": float(lat),
                            "longitude": float(lng),
                        }
                    }
                }
            }
        ],

        "destinations": [

            {
                "waypoint": {
                    "location": {
                        "latLng": {
                            "latitude":
                                p["location"]["lat"],

                            "longitude":
                                p["location"]["lng"],
                        }
                    }
                }
            }

            for p in places
        ],

        "travelMode": "DRIVE",
    }

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask":
            "originIndex,destinationIndex,distanceMeters,duration",
    }

    matrix_response = requests.post(
        route_url,
        json=body,
        headers=headers
    )

    matrix = matrix_response.json()

    # =====================================
    # Step 6: Merge Distance
    # =====================================

    enriched_places = []

    for index, place in enumerate(places):

        matched = None

        for m in matrix:

            if m.get("destinationIndex") == index:
                matched = m
                break

        distance_meters = (
            matched.get("distanceMeters")
            if matched else None
        )

        duration_seconds = None

        if matched and matched.get("duration"):

            duration_seconds = int(
                matched["duration"].replace("s", "")
            )

        enriched = {

            **place,

            "distance_value":
                distance_meters,

            "duration_value":
                duration_seconds,

            "distance_text":
                (
                    f"{distance_meters} m"
                    if distance_meters and distance_meters < 1000
                    else f"{distance_meters / 1000:.1f} km"
                )
                if distance_meters
                else None,

            "duration_text":
                (
                    f"{round(duration_seconds / 60)} min"
                )
                if duration_seconds
                else None,
        }

        enriched_places.append(enriched)

    # =====================================
    # Step 7: Return Raw Candidate Places
    # =====================================

    return enriched_places

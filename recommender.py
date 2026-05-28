# recommender.py

def rank_places(places, preferences):

    print("\n[Recommender] Ranking places...")

    scored_places = []

    for p in places:

        score = 0

        # =====================================
        # Rating Score
        # =====================================

        score += (p.get("rating") or 0) * 2

        # =====================================
        # Distance Score
        # =====================================

        if p.get("distance_value"):

            km = p["distance_value"] / 1000

            score += max(0, 10 - km)

        # =====================================
        # Price Preference
        # =====================================

        if preferences.get("price") == "cheap":

            if p.get("price_level") is not None:

                score += max(
                    0,
                    5 - p["price_level"]
                )

        elif preferences.get("price") == "expensive":

            if p.get("price_level") is not None:

                score += p["price_level"]

        # =====================================
        # Save Score
        # =====================================

        p["score"] = round(score, 2)

        scored_places.append(p)

    # =====================================
    # Final Ranking
    # =====================================

    scored_places.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_places[:3]
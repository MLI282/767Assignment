# main.py

from planner import extract_preferences
from maps_tool import search_places
from recommender import rank_places
from location import get_current_location
from memory import update_memory, get_memory
from logger import log_event
from reflection import reflect_recommendations
import reflection   

def main():

    print("===================================")
    print(" Intelligent Location Agent ")
    print("===================================")

    log_event("[System] Agent started.")

    # =====================================
    # Step 0: Detect User Location
    # =====================================

    log_event("[Agent] Detecting current location...")

    lat, lng = get_current_location()

    print(f"\n[Location Detected]")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")

    log_event(
        f"[Location] Latitude={lat}, Longitude={lng}"
    )

    # =====================================
    # Main Loop
    # =====================================

    while True:

        print("\n-----------------------------------")

        user_input = input(
            "\nWhat are you looking for?\n> "
        )

        log_event(f"[User Input] {user_input}")

        # =====================================
        # Exit
        # =====================================

        if user_input.lower() in ["exit", "quit","bye"]:

            log_event("[System] User exited program.")

            print("\n[Agent] Goodbye!")

            break

        # =====================================
        # Step 1: Planner
        # =====================================

        log_event(
            "[Planner] Understanding user goal..."
        )

        preferences = extract_preferences(
            user_input,
            get_memory()
        )

        log_event(
            f"[Planner Output] {preferences}"
        )

        # =====================================
        # Step 2: Memory Update
        # =====================================

        update_memory(preferences)

        log_event(
            f"[Memory Updated] {get_memory()}"
        )

        print("\n[Memory]")
        print(get_memory())

        print("\n[Planner Output]")
        print(preferences)

        # =====================================
        # Step 3: Maps Tool
        # =====================================

        log_event(
            "[Tool] Searching nearby places..."
        )

        print("\n[Tool] Searching nearby places...")

        candidate_places = search_places(
            preferences,
            lat,
            lng
        )

        # =====================================
        # No Results
        # =====================================

        if len(candidate_places) == 0:

            log_event(
                "[Tool] No places found."
            )

            print("\n[Agent] No places found.")

            continue

        log_event(
            f"[Tool] Retrieved "
            f"{len(candidate_places)} candidate places."
        )

        print(
            f"\n[Tool] Retrieved "
            f"{len(candidate_places)} candidate places."
        )

        # =====================================
        # Step 4: Recommender
        # =====================================

        log_event(
            "[Recommender] Evaluating places..."
        )

        print("\n[Recommender] Evaluating places...")

        recommendations = rank_places(
            candidate_places,
            preferences
        )
        # =====================================
# Reflection Agent
# =====================================

        print("\n[Reflection Agent] Evaluating recommendations...")

        reflection = reflect_recommendations(
    user_input,
    preferences,
    recommendations
)

        print("\n===================================")
        print(" REFLECTION ")
        print("===================================\n")

        print(reflection)
        log_event(
            f"[Recommender] Generated "
            f"{len(recommendations)} recommendations."
        )

        # =====================================
        # Final Output
        # =====================================

        print("\n===================================")
        print(" FINAL RECOMMENDATIONS ")
        print("===================================\n")

        log_event(
            "[Final] Displaying recommendations."
        )

        for idx, place in enumerate(recommendations):

            log_event(
                f"[Recommendation {idx+1}] "
                f"{place['name']} | "
                f"Score={place.get('score')}"
            )

            print(f"{idx + 1}. {place['name']}")

            print(
                f"   Rating: "
                f"{place.get('rating')}"
            )

            print(
                f"   Distance: "
                f"{place.get('distance_text')}"
            )

            print(
                f"   Duration: "
                f"{place.get('duration_text')}"
            )

            print(
                f"   Address: "
                f"{place.get('address')}"
            )

            print(
                f"   Score: "
                f"{place.get('score')}"
            )

            print()

        print("===================================")

        log_event(
            "[System] Recommendation cycle completed."
        )


if __name__ == "__main__":
    main()

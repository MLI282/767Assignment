# memory.py

memory = {
    "favorite_cuisine": None,
    "preferred_price": None
}


def update_memory(preferences):

    if preferences.get("cuisine"):

        memory["favorite_cuisine"] = (
            preferences["cuisine"]
        )

    if preferences.get("price"):

        memory["preferred_price"] = (
            preferences["price"]
        )


def get_memory():

    return memory
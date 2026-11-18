import requests


def fetch_stackoverflow_profile(user_id):

    url = f"https://api.stackexchange.com/2.3/users/{user_id}?site=stackoverflow"

    response = requests.get(url)

    if response.status_code != 200:

        return {
            "platform": "Stack Overflow",
            "error": "Unable to connect to Stack Overflow."
        }

    data = response.json()

    if not data.get("items"):

        return {
            "platform": "Stack Overflow",
            "error": "Profile not found."
        }

    user = data["items"][0]

    profile = {

        "platform": "Stack Overflow",

        "user_id": user.get("user_id"),

        "display_name": user.get("display_name"),

        "reputation": user.get("reputation"),

        "gold_badges": user.get("badge_counts", {}).get("gold"),

        "silver_badges": user.get("badge_counts", {}).get("silver"),

        "bronze_badges": user.get("badge_counts", {}).get("bronze"),

        "location": user.get("location"),

        "website": user.get("website_url"),

        "profile_image": user.get("profile_image"),

        "profile_url": user.get("link"),

        "account_created": user.get("creation_date")

    }

    return profile
import requests

def fetch_github_profile(username):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:

        return {
            "platform": "GitHub",
            "error": "GitHub profile not found."
        }

    data = response.json()

    profile = {

        "platform": "GitHub",

        "username": data.get("login"),

        "name": data.get("name"),

        "company": data.get("company"),

        "location": data.get("location"),

        "bio": data.get("bio"),

        "followers": data.get("followers"),

        "following": data.get("following"),

        "public_repositories": data.get("public_repos"),

        "profile_picture": data.get("avatar_url"),

        "profile_url": data.get("html_url"),

        "account_created": data.get("created_at")

    }

    return profile
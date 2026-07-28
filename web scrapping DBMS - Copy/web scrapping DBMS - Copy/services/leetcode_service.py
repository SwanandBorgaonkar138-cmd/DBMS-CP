import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query getUserProfile($username: String!) {
    matchedUser(username: $username) {
        username
        profile {
            realName
            ranking
            reputation
            userAvatar
        }
        submitStats: submitStatsGlobal {
            acSubmissionNum {
                difficulty
                count
            }
        }
    }
}
"""

def fetch_leetcode_profile(username):

    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
    }

    payload = {
        "query": QUERY,
        "variables": {"username": username}
    }

    try:
        response = requests.post(GRAPHQL_URL, json=payload, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        return {"platform": "LeetCode", "error": str(e)}

    if response.status_code != 200:
        return {
            "platform": "LeetCode",
            "error": f"Request failed with status {response.status_code}"
        }

    data = response.json()
    user = data.get("data", {}).get("matchedUser")

    if not user:
        return {
            "platform": "LeetCode",
            "error": f"User '{username}' not found on LeetCode."
        }

    # Parse solved counts by difficulty
    ac_stats = user.get("submitStats", {}).get("acSubmissionNum", [])
    solved_map = {entry["difficulty"]: entry["count"] for entry in ac_stats}

    profile_info = user.get("profile", {})

    profile = {
        "platform":        "LeetCode",
        "username":        user.get("username"),
        "real_name":       profile_info.get("realName"),
        "ranking":         profile_info.get("ranking"),
        "reputation":      profile_info.get("reputation"),
        "total_solved":    solved_map.get("All", 0),
        "easy_solved":     solved_map.get("Easy", 0),
        "medium_solved":   solved_map.get("Medium", 0),
        "hard_solved":     solved_map.get("Hard", 0),
        "profile_picture": profile_info.get("userAvatar"),
        "profile_url":     f"https://leetcode.com/u/{username}/"
    }

    return profile
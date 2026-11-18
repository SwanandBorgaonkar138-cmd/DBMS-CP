import requests

LEETCODE_API = "https://leetcode.com/graphql"


def fetch_leetcode_profile(username):

    print("Searching:", username)

    query = """
    query getUserProfile($username: String!) {
  matchedUser(username: $username) {

    username

    profile {
      ranking
      userAvatar
      realName
    }

    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
    """

    print(query)

    variables = {
        "username": username
    }

    print(variables)

    payload = {
        "query": query,
        "variables": variables
    }

    print("\nPayload:")

    print(payload)

    response = requests.post(
        LEETCODE_API,
        json=payload,
    )

    print("\nStatus Code:")
    print(response.status_code)

    print("\nRaw Response:")
    print(response.text)

    data = response.json()
    user = data["data"]["matchedUser"]
    # -------------------------
    # USER NOT FOUND
    # -------------------------

    if user is None:

     return {
        "platform": "LeetCode",
        "error": "User not found"
    }
    stats = user["submitStats"]["acSubmissionNum"]
    solved = {}

    for item in stats:
        solved[item["difficulty"]] = item["count"]
    return {
        "platform": "LeetCode",
        "username": user["username"],
        "real_name": user["profile"]["realName"],
        "ranking": user["profile"]["ranking"],
        "profile_picture": user["profile"]["userAvatar"],
        "total_solved": solved["All"],
        "easy_solved": solved["Easy"],
        "medium_solved": solved["Medium"],
        "hard_solved": solved["Hard"]


    }
from services.url_detector import detect_platform
from services.profile_parser import extract_identifier

from services.github_service import fetch_github_profile
from services.stackoverflow_service import fetch_stackoverflow_profile
from services.leetcode_service import fetch_leetcode_profile

def get_profile(profile_url):
    """
    Detect platform, extract identifier,
    fetch profile data and return it.
    """

    # Detect platform
    platform = detect_platform(profile_url)

    print("Detected Platform:", platform)

    # Extract username / user id
    info = extract_identifier(profile_url)

    print("Extracted Information:", info)

    if platform == "GitHub":

        username = info["username"]

        print("Fetching GitHub Profile...")

        profile = fetch_github_profile(username)

        return profile

    elif platform == "Stack Overflow":

        user_id = info["user_id"]

        print("Fetching Stack Overflow Profile...")

        profile = fetch_stackoverflow_profile(user_id)

        return profile
    
    elif platform == "LeetCode":

        username = info["username"]

        print("Fetching LeetCode Profile...")

        profile = fetch_leetcode_profile(username)

        return profile

    else:

        return {
            "error": "Unsupported platform."
        }
from services.url_detector import detect_platform
from services.profile_parser import extract_identifier

from services.github_service import fetch_github_profile
from services.stackoverflow_service import fetch_stackoverflow_profile
from services.leetcode_service import fetch_leetcode_profile

from services.identity_service import discover_profiles
from services.merge_service import merge_profiles
from services.confidence_services import calculate_confidence


def get_profile(profile_url):
    """
    Main Profile Aggregator

    Detects the platform,
    fetches the source profile,
    discovers profiles on other platforms,
    merges everything,
    calculates confidence,
    returns one unified profile.
    """

    print("\n========== PROFILE AGGREGATOR ==========\n")

    # ---------------------------------------
    # Detect Platform
    # ---------------------------------------

    platform = detect_platform(profile_url)

    print("Detected Platform:", platform)

    info = extract_identifier(profile_url)

    print("Extracted Information:", info)

    github_profile = None
    stack_profile = None
    leetcode_profile = None

    # ---------------------------------------
    # Fetch Source Profile
    # ---------------------------------------

    if platform == "GitHub":

        github_profile = fetch_github_profile(
            info["username"]
        )

    elif platform == "Stack Overflow":

        stack_profile = fetch_stackoverflow_profile(
            info["user_id"]
        )

    elif platform == "LeetCode":

        leetcode_profile = fetch_leetcode_profile(
            info["username"]
        )

    else:

        return {
            "error": "Unsupported Platform"
        }

    # ---------------------------------------
    # Identity Discovery
    # ---------------------------------------

    source = github_profile or stack_profile or leetcode_profile

    discovered = discover_profiles(source)

    github_profile = discovered.get("github") or github_profile

    stack_profile = discovered.get("stackoverflow") or stack_profile

    leetcode_profile = discovered.get("leetcode") or leetcode_profile

    # ---------------------------------------
    # Merge Profiles
    # ---------------------------------------

    unified = merge_profiles(

        github_profile,

        stack_profile,

        leetcode_profile

    )

    # ---------------------------------------
    # Confidence Calculation
    # ---------------------------------------

    confidence = calculate_confidence(

        github_profile,

        stack_profile,

        leetcode_profile

    )

    unified["confidence"] = confidence["score"]

    unified["match_status"] = confidence["status"]

    unified["explanation"] = confidence["explanation"]

    # ---------------------------------------
    # Return Final Profile
    # ---------------------------------------

    return unified
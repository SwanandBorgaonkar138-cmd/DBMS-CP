from services.candidate_services import generate_candidates

from services.github_service import fetch_github_profile
from services.stackoverflow_service import fetch_stackoverflow_profile
from services.leetcode_service import fetch_leetcode_profile


def discover_profiles(source_profile):

    """
    Finds matching profiles
    across GitHub, Stack Overflow,
    and LeetCode.
    """

    print("\n========== Identity Discovery ==========\n")

    candidates = generate_candidates(source_profile)

    print("Generated Candidates:")

    print(candidates)

    github_profile = None
    leetcode_profile = None

    for username in candidates:

        print(f"\nTrying GitHub username: {username}")

        profile = fetch_github_profile(username)

        if "error" not in profile:

            github_profile = profile

            print("GitHub Match Found!")

            break

    for username in candidates:

        print(f"\nTrying LeetCode username: {username}")

        profile = fetch_leetcode_profile(username)

        if "error" not in profile:

            leetcode_profile = profile

            print("LeetCode Match Found!")

            break

    return {

        "github": github_profile,

        "leetcode": leetcode_profile

    }
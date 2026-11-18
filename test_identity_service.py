from services.github_service import fetch_github_profile
from services.identity_service import discover_profiles

username = input("Enter GitHub Username: ")

profile = fetch_github_profile(username)

result = discover_profiles(profile)

print("\n\n===== Final Result =====\n")

print(result)
from services.github_service import fetch_github_profile

username = input("Enter GitHub Username: ")

data = fetch_github_profile(username)

print("\nResult:\n")

print(data)
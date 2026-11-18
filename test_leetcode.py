from services.leetcode_service import fetch_leetcode_profile

username = input("Enter LeetCode Username: ")

profile = fetch_leetcode_profile(username)

print("\nReturned Profile:\n")

print(profile)
from services.leetcode_service import fetch_leetcode_profile

username = input("Enter LeetCode Username: ")

data = fetch_leetcode_profile(username)

print("\nResult:\n")

print(data)
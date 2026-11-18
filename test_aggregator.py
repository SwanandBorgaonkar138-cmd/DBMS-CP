from services.profile_service import get_profile

url = input("Enter Any Profile URL: ")

profile = get_profile(url)

print("\n\n========== FINAL UNIFIED PROFILE ==========\n")

print(profile)
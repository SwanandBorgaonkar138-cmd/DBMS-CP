from services.profile_service import get_profile

url = input("Enter Profile URL: ")

profile = get_profile(url)

print("\nReturned Profile:\n")
print(profile)
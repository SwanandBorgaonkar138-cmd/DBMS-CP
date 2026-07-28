from services.stackoverflow_service import fetch_stackoverflow_profile

user_id = input("Enter Stack Overflow User ID: ")

profile = fetch_stackoverflow_profile(user_id)

print("\n========== PROFILE ==========\n")

for key, value in profile.items():
    print(f"{key}: {value}")
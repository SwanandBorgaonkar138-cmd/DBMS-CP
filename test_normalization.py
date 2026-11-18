from services.normalization_service import normalize_username

print(normalize_username("Krishna_Bheda"))

print(normalize_username("Krishna-Bheda"))

print(normalize_username("Krishna.Bheda"))

print(normalize_username("KRISHNABHEDA"))

print(normalize_username("Krishna Bheda"))
from services.username_similarity import  username_similarity

print(username_similarity("Krishna_Bheda", "KrishnaBheda"))

print(username_similarity("Jon-Skeet", "jonskeet"))

print(username_similarity("Krishna.Bheda", "Krishna_Bheda"))

print(username_similarity("Krishna", "Jon"))
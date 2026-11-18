from services.name_similarity import name_similarity

print(name_similarity("Jon Skeet", "Jon Skeet"))

print(name_similarity("Jon Skeet", "Jonathan Skeet"))

print(name_similarity("Krishna Bheda", "Krishna B."))

print(name_similarity("Krishna", "Jon"))
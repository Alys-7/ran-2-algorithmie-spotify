from spotify import dataset

count0_19 = 0
count20_35 = 0
count36_50 = 0
count51_ = 0

for user in dataset:
    if int(user["age"]) <= 19:
        count0_19 += 1
    
    elif int(user["age"]) <= 35:
        count20_35 += 1
    
    elif int(user["age"]) <= 50:
        count36_50 += 1
    
    else:
        count51_ += 1

print(f"Le nombre d'utilisateurs de 19 ans ou moins est de {count0_19}")
print(f"Le nombre d'utilisateurs entre 20 et 35 ans est de {count20_35}")
print(f"Le nombre d'utilisateurs entre 36 et 50 ans est de {count36_50}")
print(f"Le nombre d'utilisateurs de 51 ans ou plus est de {count51_}")
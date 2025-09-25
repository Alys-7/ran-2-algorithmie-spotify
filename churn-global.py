from spotify import dataset

total = 0 #Nombre total d'utilisateurs
churned = 0 #Nombre d'utilisateurs ayant quitté le service

for record in dataset:
    total += 1
    if record["is_churned"] == '1':
        churned += 1

print(f"Total users: {total}")
print(f"Churned users: {churned}")

percentage = round((churned / total) * 100, 2)
print(f"Churn rate: {percentage}%")
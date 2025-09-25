from spotify import dataset

### Méthode 1

def churn_rate (subscription_type): #subscription_type = liste de types d'abonnement
    total = 0 #Nombre total d'utilisateurs ayant l'abonnement subscription_type
    churned = 0 #Nombre d'utilisateurs ayant l'abonnement subscription_type et quitté le service

    for record in dataset:
        if record["subscription_type"] in subscription_type:
            total += 1
            if record["is_churned"] == '1':
                churned += 1

    percentage = round((churned / total) * 100, 2)

    return percentage

print(churn_rate(["Free"]))
print(churn_rate(["Student"]))
print(churn_rate(["Premium"]))
print(churn_rate(["Family"]))
print(churn_rate(["Free", "Student", "Premium", "Family"])) #Churn global
# print(churn_rate(["Free", "Student"]))



### Méthode 2

subscription_by_type = {"Free": 0, "Student": 0, "Premium": 0, "Family": 0}
churned_by_type = {"Free": 0, "Student": 0, "Premium": 0, "Family": 0}

for record in dataset:
    subscription_by_type[record["subscription_type"]] += 1
    if record["is_churned"] == '1':
        churned_by_type[record["subscription_type"]] +=1

percentage = []
total = 0
churned = 0

for key, value in churned_by_type.items():
    total += subscription_by_type[key]
    churned += value
    percentage.append(round((value / subscription_by_type[key]) * 100, 2))

percentage.append(round((churned / total) * 100, 2))

print(percentage)

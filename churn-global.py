from spotify import dataset


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
print(churn_rate(["Family"]))
print(churn_rate(["Student"]))
print(churn_rate(["Premium"]))
print(churn_rate(["Free", "Family", "Student", "Premium"])) #Churn global
print(churn_rate(["Free", "Student"]))
from spotify import dataset

ads = {"Free": 0, "Student": 0, "Premium": 0, "Family": 0} #Dictionnaire du nombre de pubs écoutées par subscription_type
nb_subscription_type = {"Free": 0, "Student": 0, "Premium": 0, "Family": 0} #Dictionnaire du nombre de user par subscription_type


for user in dataset:
    subscription_type = user["subscription_type"]
    ads_listened_per_week = user["ads_listened_per_week"]

    ads[subscription_type] += int(ads_listened_per_week)
    nb_subscription_type[subscription_type] += 1

for key, value in ads.items():
    print(f"La moyenne de pubs écoutées par semaine pour l'abonnement {key} est de: {round(value / nb_subscription_type[key], 2)}")
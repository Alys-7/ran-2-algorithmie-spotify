from spotify import dataset

prices = {"Free": 0.0, "Student": 4.99, "Premium": 9.99, "Family": 14.99}
mrr = {"Free": {}, "Student": {}, "Premium": {}, "Family": {}} #Dictionnaire du monthly recurring revenue par subscription_type et par country

for user in dataset:
    if user["is_churned"] == '1':
        continue

    subscription_type = user["subscription_type"]
    country = user["country"]

    if country not in mrr[subscription_type].keys():
        mrr[subscription_type][country] = prices[subscription_type]
    
    else:
        mrr[subscription_type][country] = round(mrr[subscription_type][country] + prices[subscription_type], 2)

print(mrr)
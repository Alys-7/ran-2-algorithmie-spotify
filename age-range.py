from spotify import dataset

count_19 = 0
count20_35 = 0
count36_50 = 0
count51_ = 0

# Nombre d'utilsateurs par tranche d'âge

def number_users_per_age():
    for user in dataset:
        if int(user["age"]) <= 19:
            count_19 += 1
        
        elif int(user["age"]) <= 35:
            count20_35 += 1
        
        elif int(user["age"]) <= 50:
            count36_50 += 1
        
        else:
            count51_ += 1

    return [count_19, count20_35, count36_50, count51_]



# Nombre de subscription_type par tranche d'âge

def number_subscription_type_per_age():
    subscription_type_per_age = {"count_19": {"Free": 0, "Student": 0, "Premium":0, "Family":0}, "count20_35": {"Free": 0, "Student": 0, "Premium":0, "Family":0}, "count36_50": {"Free": 0, "Student": 0, "Premium":0, "Family":0}, "count51_": {"Free": 0, "Student": 0, "Premium":0, "Family":0}}

    for user in dataset:
        subscription_type = user["subscription_type"]
        
        if int(user["age"]) <= 19:
            subscription_type_per_age["count_19"][subscription_type] += 1
        
        elif int(user["age"]) <= 35:
            subscription_type_per_age["count20_35"][subscription_type] += 1
        
        elif int(user["age"]) <= 50:
            subscription_type_per_age["count36_50"][subscription_type] += 1
        
        else:
            subscription_type_per_age["count51_"][subscription_type] += 1
    
    return subscription_type_per_age

print(number_subscription_type_per_age())
from spotify import dataset

user_to_revive = []
count = 0

for user in dataset:
    if ((float(user["skip_rate"]) > 0.3 and int(user["listening_time"]) < 100) or 
        (user["subscription_type"] == "Free" and user["offline_listening"] == '0' and int(user["ads_listened_per_week"]) > 20)):
        user_to_revive.append(user["user_id"])
        count += 1

print(user_to_revive)
print(round(count / 8000 * 100, 2))
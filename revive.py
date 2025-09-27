from spotify import dataset

user_to_revive = []

for record in dataset:
    if ((float(record["skip_rate"]) > 0.3 and int(record["listening_time"]) < 100) or 
        (record["subscription_type"] == "Free" and record["offline_listening"] == '0' and int(record["ads_listened_per_week"]) > 20)):
        user_to_revive.append(record["user_id"])

print(user_to_revive)
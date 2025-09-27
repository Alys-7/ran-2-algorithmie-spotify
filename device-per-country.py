from spotify import dataset

device_per_country = {"Mobile": {}, "Desktop": {}, "Web": {}}

for user in dataset:
    device = user["device_type"]
    country = user["country"]

    if country not in device_per_country[device]:
        device_per_country[device][country] = 1
    
    else:
        device_per_country[device][country] += 1

print(device_per_country)
from spotify import dataset

list_device = []
list_country = []

for user in dataset:
    device = user["device_type"]
    country = user["country"]

    if device not in list_device:
        list_device.append(device)
    
    if country not in list_country:
        list_country.append(country)

print(list_device)
print(list_country)
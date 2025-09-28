from spotify import dataset

device_per_country = {}

for user in dataset:
    device = user["device_type"]
    country = user["country"]

    if country not in device_per_country:
        device_per_country[country] = {device: 1}
    
    elif device not in device_per_country[country]:
        device_per_country[country][device] = 1
    
    else:
        device_per_country[country][device] += 1

print(device_per_country)

for key, value in device_per_country.items():
    mobile = int(value["Mobile"])
    desktop = int(value["Desktop"])
    web = int(value["Web"])
    if mobile > max(desktop, web):
        print(f"Le support le plus utilisé pour {key} est Mobile")
    
    elif desktop > max(mobile, web):
        print(f"Le support le plus utilisé pour {key} est Desktop")
    
    elif web > max(mobile, desktop):
        print(f"Le support le plus utilisé pour {key} est Web")
    
    elif mobile == desktop and mobile > web:
        print(f"Les supports les plus utilisés pour {key} sont Mobile et Desktop")
    
    elif mobile == web and mobile > desktop:
        print(f"Les supports les plus utilisés pour {key} sont Mobile et Web")
    
    elif desktop == web and desktop > mobile:
        print(f"Les supports les plus utilisés pour {key} sont Desktop et Web")
    
    else:
        print(f"Les supports les plus utilisés pour {key} sont Mobile, Desktop et Web")
## +de 200 min d’écoute par jour et + de 50 titres écoutés par jour

from spotify import dataset

for user in dataset:
    if int(user["listening_time"]) >= 200 and int(user["songs_played_per_day"]) >= 50:
        print(user)
from spotify import dataset

id_in_dataset = False

while not id_in_dataset:
    id = int(input("Entrez l'id de l'utilisateur: "))
    
    for user in dataset:
        if id == int(user["user_id"]):
            print(user)
            id_in_dataset = True
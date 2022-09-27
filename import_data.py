def import_data(data):
    with open('phone.csv', 'a+') as file:
        for i in data:
            file.write(f"{i}\n")
        file.write(f"\n")
       
    
    with open('phone.txt', 'a+') as file:
        for i in data:
            file.write(f"{i}\n")
        file.write(f"\n")

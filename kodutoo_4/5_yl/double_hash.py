def hash_function1(name, table_size):
    return len(name) % table_size

def hash_function2(name):
    p = 19 
    return p - (name % p)


hash_table = {}
size = 20
running = True

while running: 

    question = input("Sisesta vastav number \n \n 1 - Sisesta nimi ja telefoninumber \n 2 - Pane programm kinni \n Sinu vastus: ")

    if question == "1":

        name = input("Siseta inimese nimi: ")
        phone_number = input("Sisesta inimese telefoninumber: ")

        hash_table[hash_function2(hash_function1(name, 20))] = phone_number

        print(hash_table)

        # question = input("Sisesta vastav number \n \n 1 - Sisesta nimi ja telefoninumber \n 2 - Pane programm kinni \n Sinu vastus: ")

    else:
        running = False
    
    

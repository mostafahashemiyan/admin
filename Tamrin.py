
List = dict()


while True:

    print("1.add student ", "2.delet student ", "3.show student", "4. exit ")
    a = int(input("enter numer : "))

    if a == 1:
        id = input("ID: ")
        Name = input("Name: ")
        Ai = int(input("Ai : "))
        Algorithm = int(input("Algorithm : "))
        database = int(input("database : "))
        avg = ((Ai+Algorithm+database)/3)
        List[id] = {
            "Name": Name,
            "Ai": Ai,
            "algorithm": Algorithm,
            "database": database,
            "avg": avg
        }
        print("Added ")

    elif a == 2:
        remove = input("Enter your id : ")
        List.pop(remove)
        print("your id removed succefully")

    elif a == 3:
        print(List)

    elif a == 4:
        break

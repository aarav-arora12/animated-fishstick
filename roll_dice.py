import random
response = "y"
while response == "y":
    number = random.randint(1,6)
    if number == 1:
        print("[-----]") 
        print("[ ]") 
        print("[ 0 ]") 
        print("[ ]") 
        print("[-----]")
    response = input("PRESS Y TO ROLL AGAIN AND N TO EXIT")
    print("\n")
import os
from enum import Enum
from helper import save_data,load_data

# array decleration
my_garage = []
my_data_file = 'my_garage.json'

# Enums
class Actions(Enum):
     PRINT = 1
     ADD = 2
     FIND = 3
     REMOVE = 4
     EXIT = 5

def exit_program():
    save_data(my_data_file,my_garage)
    print("Cya Later")
    exit()

# add new contact
def add_contact():
    my_garage.append({"Model":input("Enter Car Model(Year):"),"Color":input("Enter Car Color:"),"Brand":input("Enter Brand Name: "),"License Number":input("Enter License Number: ")})
    print("Contact added!")

# search
def find_car():
    global my_garage
    search_id = input("Enter License Number: ")
    for car in my_garage:
        if car["License Number"] == search_id:
            return car
    print("Couldn't find your car...")
        
def delete_car():
    global my_garage
    search_id = input("Enter License Number: ")
    for car in my_garage:
        if car["License Number"] == search_id:
            my_garage.remove(car)
            print(f"Car with License Number {search_id} has been deleted.")
            return
        
    print("Couldn't find your car...")

def display():#Displays the menu
    print("Welcome to Qlean's Garage")
    for action in Actions:
        print(f'{action.value} : {action.name}')
    return Actions(int(input("Enter your selection: ")))

def main():
    global my_garage
    #clear Console
    os.system('cls' if os.name == 'nt' else 'clear')
    my_garage = load_data(my_data_file,my_garage)
    
    while (True):
      userSelection=display() #display a menu and get user selection and  implements menu
      if userSelection == Actions.EXIT: exit_program()
      if userSelection ==  Actions.PRINT: print(my_garage)
      if userSelection ==  Actions.FIND: print(find_car())
      if userSelection ==  Actions.ADD: add_contact()
      if userSelection ==  Actions.REMOVE: delete_car()

        
if __name__ == "__main__":
	main()

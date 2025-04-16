from pet import Pet

def display_menu():
    print("\n=== Pet Simulator ===")
    print("1. Feed your pet")
    print("2. Play with your pet")
    print("3. Let your pet sleep")
    print("4. Train your pet a new trick")
    print("5. Check your pet's status")
    print("6. Show learned tricks")
    print("7. Quit")

def main():
    print("Welcome to the Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")
    pet = Pet(pet_name)

    while True:
        display_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            pet.eat()
            print(f"{pet.name} ate. Hunger decreased, happiness increased!")
        elif choice == "2":
            if pet.energy >= 2:
                pet.play()
                print(f"{pet.name} played happily! Energy decreased, hunger increased.")
            else:
                print(f"{pet.name} is too tired to play. Try sleeping first!")
        elif choice == "3":
            pet.sleep()
            print(f"{pet.name} took a nap. Energy restored!")
        elif choice == "4":
            trick = input("What trick would you like to teach? ")
            pet.train(trick)
            print(f"{pet.name} learned '{trick}'!")
        elif choice == "5":
            pet.get_status()
        elif choice == "6":
            if pet.tricks:
                pet.show_tricks()
            else:
                print(f"{pet.name} hasn't learned any tricks yet.")
        elif choice == "7":
            print(f"Goodbye! Take care of {pet.name}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

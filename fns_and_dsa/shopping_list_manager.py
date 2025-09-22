print("Shopping List Manager")

shopping_list = []

def display_menu():
    print("\nOptions:")
    print("1. View shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Shopping List:", shopping_list)
    elif choice == 2:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added.")
    elif choice == 3:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} not found.")
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")


        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

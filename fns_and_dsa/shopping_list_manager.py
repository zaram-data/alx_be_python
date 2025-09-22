# shopping_list_manager.py

# Initialize the shopping list
shopping_list = []

# Function to display the menu


def display_menu():
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")

# Main program loop
while True:
    display_menu()
    
    # Get user's choice and ensure it's a number
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Handle choices
    if choice == 1:
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    elif choice == 2:
        if shopping_list:
            print("Your Shopping List:")
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")
        else:
            print("Your shopping list is empty.")
    elif choice == 3:
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' is not in the shopping list.")
    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

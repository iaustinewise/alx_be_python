def display_menu():
    print("\n" + "="*30)
    print("   Shopping List Manager")
    print("="*30)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*30)

def add_item(shopping_list):
    """Add an item to the shopping list"""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Invalid input. Item name cannot be empty.")

def remove_item(shopping_list):
    """Remove an item from the shopping list"""
    if not shopping_list:
        print("Your shopping list is empty. Nothing to remove.")
        return
    
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' not found in your shopping list.")

def view_list(shopping_list):
    """Display the current shopping list"""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print(f"\nYour Shopping List ({len(shopping_list)} items):")
        print("-" * 25)
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def main():
    shopping_list = []
    
    print("Welcome to the Shopping List Manager!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("\nThank you for using Shopping List Manager!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        
        # Pause for user to read the output
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main() 
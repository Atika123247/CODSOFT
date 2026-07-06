def contact_book():
    # List to store all contact dictionaries
    contacts = []
    print("--- CodSoft Python Contact Book ---")

    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit Application")
        
        choice = input("\nEnter your choice (1-6): ").strip()

        # 1. Add Contact
        if choice == '1':
            print("\n--- Add New Contact ---")
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email Address: ").strip()
            address = input("Enter Physical Address: ").strip()
            
            if name and phone:
                # Store all user-provided details into a structured dictionary
                contact = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address
                }
                contacts.append(contact)
                print(f"Contact for '{name}' added successfully!")
            else:
                print("Error: Name and Phone Number are required fields.")

        # 2. View Contact List
        elif choice == '2':
            if not contacts:
                print("\nYour contact book is empty.")
            else:
                print("\n--- Contact List ---")
                # Loop through and display only names and phone numbers
                for index, c in enumerate(contacts, start=1):
                    print(f"{index}. Name: {c['name']} | Phone: {c['phone']}")

        # 3. Search Contact
        elif choice == '3':
            if not contacts:
                print("\nNo contacts saved to search.")
                continue
            
            search_term = input("\nEnter name or phone number to search: ").strip().lower()
            found = False
            
            print("\n--- Search Results ---")
            for c in contacts:
                # Check if the search term matches either the name or the phone number
                if search_term in c['name'].lower() or search_term in c['phone']:
                    print(f"\nName: {c['name']}")
                    print(f"Phone: {c['phone']}")
                    print(f"Email: {c['email']}")
                    print(f"Address: {c['address']}")
                    found = True
            
            if not found:
                print("No matching contact found.")

        # 4. Update Contact
        elif choice == '4':
            if not contacts:
                print("\nNo contacts saved to update.")
                continue
            
            print("\n--- Update Contact ---")
            for index, c in enumerate(contacts, start=1):
                print(f"{index}. {c['name']} ({c['phone']})")
                
            try:
                num = int(input("\nEnter the number of the contact you want to update: "))
                if 1 <= num <= len(contacts):
                    selected_contact = contacts[num - 1]
                    print(f"\nUpdating profile for '{selected_contact['name']}'. (Leave blank to keep existing data)")
                    
                    new_name = input(f"New Name [{selected_contact['name']}]: ").strip()
                    new_phone = input(f"New Phone [{selected_contact['phone']}]: ").strip()
                    new_email = input(f"New Email [{selected_contact['email']}]: ").strip()
                    new_address = input(f"New Address [{selected_contact['address']}]: ").strip()
                    
                    # Update fields only if the user types something new
                    if new_name: selected_contact['name'] = new_name
                    if new_phone: selected_contact['phone'] = new_phone
                    if new_email: selected_contact['email'] = new_email
                    if new_address: selected_contact['address'] = new_address
                    
                    print("Contact updated successfully!")
                else:
                    print("Invalid contact selection number.")
            except ValueError:
                print("Please enter a valid choice number.")

        # 5. Delete Contact
        elif choice == '5':
            if not contacts:
                print("\nNo contacts saved to delete.")
                continue
                
            print("\n--- Delete Contact ---")
            for index, c in enumerate(contacts, start=1):
                print(f"{index}. {c['name']} ({c['phone']})")
                
            try:
                num = int(input("\nEnter the number of the contact you want to delete: "))
                if 1 <= num <= len(contacts):
                    removed = contacts.pop(num - 1)
                    print(f"Successfully deleted contact profile for '{removed['name']}'.")
                else:
                    print("Invalid choice number.")
            except ValueError:
                print("Please enter a valid choice number.")

        # 6. Exit Application
        elif choice == '6':
            print("\nThank you for using Contact Book! Goodbye.")
            break
        else:
            print("Invalid input! Please select an option between 1 and 6.")

if __name__ == "__main__":
    contact_book()
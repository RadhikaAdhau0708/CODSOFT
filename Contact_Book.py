contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"{name} - {info['phone']}")

def search_contact():
    key = input("Enter name or phone to search: ")
    found = False
    for name, info in contacts.items():
        if key.lower() in name.lower() or key == info['phone']:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contacts:
        print("Leave blank to keep existing info.")
        phone = input(f"New phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email ({contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address ({contacts[name]['address']}): ") or contacts[name]['address']
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

# phonebook.py
import csv
from connect import conn, cur

# Insert from CSV
def insert_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                (row['name'], row['surname'], row['phone'])
            )
    conn.commit()
    print("CSV data inserted successfully")

# Insert from console
def insert_from_console():
    name = input("Enter first name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
        (name, surname, phone)
    )
    conn.commit()
    print("Contact added successfully")

# Update contact
def update_contact():
    contact_id = input("Enter contact ID to update: ")
    field = input("What do you want to update? (name/phone): ")
    value = input(f"Enter new {field}: ")
    if field not in ['name', 'phone']:
        print("Invalid field")
        return
    cur.execute(f"UPDATE phonebook SET {field} = %s WHERE id = %s", (value, contact_id))
    conn.commit()
    print("Contact updated successfully")

# Search contacts
def search_contacts():
    pattern = input("Enter search text: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s",
        (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%")
    )
    results = cur.fetchall()
    for row in results:
        print(row)

# Delete contact
def delete_contact():
    contact_id = input("Enter contact ID to delete: ")
    cur.execute("DELETE FROM phonebook WHERE id = %s", (contact_id,))
    conn.commit()
    print("Contact deleted successfully")

# Menu
def menu():
    while True:
        print("\n1. Insert from CSV\n2. Insert from console\n3. Update contact\n4. Search\n5. Delete\n6. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            insert_from_csv('contacts.csv')
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
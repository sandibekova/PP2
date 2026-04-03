from connect import conn, cur

def search(pattern):
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    for row in cur.fetchall():
        print(row)

def paginate(limit, offset):
    cur.execute("SELECT * FROM get_phonebook_paginated(%s,%s);", (limit, offset))
    for row in cur.fetchall():
        print(row)

def insert_or_update(name, surname, phone):
    cur.execute("CALL insert_or_update_user(%s,%s,%s);", (name, surname, phone))
    conn.commit()
    print("User inserted/updated")

def insert_many(users_list):
    cur.execute("CALL insert_many_users(%s);", (users_list,))
    conn.commit()
    print("Batch insert completed")

def delete_contact(name, phone):
    cur.execute("CALL delete_contact_by_name_or_phone(%s,%s);", (name, phone))
    conn.commit()
    print("Contact deleted")

def menu():
    while True:
        print("\n1.Search\n2.Paginate\n3.Insert/Update\n4.Batch Insert\n5.Delete\n6.Exit")
        choice = input("Choose option: ")
        if choice == '1':
            search(input("Enter pattern: "))
        elif choice == '2':
            paginate(int(input("Limit: ")), int(input("Offset: ")))
        elif choice == '3':
            insert_or_update(input("Name: "), input("Surname: "), input("Phone: "))
        elif choice == '4':
            users = [['Alice','Smith','555-1234'], ['Bob','Jones','abc']]
            insert_many(users)
        elif choice == '5':
            delete_contact(input("Name: "), input("Phone: "))
        elif choice == '6':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()
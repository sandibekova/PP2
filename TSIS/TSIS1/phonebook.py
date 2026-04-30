from connect import get_connection

def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Add contact")
        print("2. Add phone")
        print("3. Move to group")
        print("4. Search")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            add_phone()
        elif choice == "3":
            move_group()
        elif choice == "4":
            search()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO contacts(name, email, birthday)
        VALUES (%s, %s, %s)
        ON CONFLICT (name) DO NOTHING;
    """, (name, email, birthday))

    conn.commit()
    cur.close()
    conn.close()


def add_phone():
    name = input("Contact name: ")
    phone = input("Phone: ")
    type_ = input("Type (home/work/mobile): ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL add_phone(%s, %s, %s);", (name, phone, type_))

    conn.commit()
    cur.close()
    conn.close()


def move_group():
    name = input("Contact name: ")
    group = input("Group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL move_to_group(%s, %s);", (name, group))

    conn.commit()
    cur.close()
    conn.close()


def search():
    query = input("Search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s);", (query,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


if __name__ == "__main__":
    menu()
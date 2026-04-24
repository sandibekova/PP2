from connect import connect

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")

import csv
from connect import connect

def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    

    path = "c:/Users/almas/Desktop/pp/work/practice7/contacts.csv"
    with open(path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()

    print("CSV data inserted!")


def search_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE first_name = %s",
        (name,)
    )

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()

def search_by_prefix(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (prefix + "%",)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

def update_contact(name, new_phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET phone = %s WHERE first_name = %s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Updated!")

def delete_contact(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE first_name = %s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")

def safe_insert(name, phone):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()
while True:
    print("\n1.Insert console")
    print("2.Insert CSV")
    print("3.Search name")
    print("4.Update")
    print("5.Delete")
    print("0.Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_from_console()
    elif choice == "2":
        insert_from_csv()
    elif choice == "3":
        name = input("Enter name: ")
        search_by_name(name)
    elif choice == "4":
        name = input("Name: ")
        phone = input("New phone: ")
        update_contact(name, phone)
    elif choice == "5":
        name = input("Name: ")
        delete_contact(name)
    elif choice == "0":
        break
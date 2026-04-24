import psycopg2
from config import load_config

def run_lab_tasks():
    # Load connection parameters from config.py
    params = load_config()
    
    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                
                # 1. TASK: Insert or Update a user (Upsert)
                # Matches procedure: upsert_user(p_name, p_phone)
                #print("--- Task: Upserting 'Ali' ---")
                #cur.execute("CALL upsert_user(%s, %s)", ("Ali", "1234567890"))
                
                
                # 2. TASK: Bulk Insert with Validation
                # Added ::text[] casting to avoid the "procedure does not exist" error
                print("--- Task: Bulk Insert ---")
                names = ['John', 'Jade', 'Robert']
                phones = ['87011112233', '87022223344', 'abc'] # '123' should be caught by your SQL logic
                cur.execute("CALL bulk_insert(%s::text[], %s::text[])", (names, phones))
                
                
                # 3. TASK: Search by pattern (Function)
                # Matches function: get_contacts_by_pattern(search_pattern)
                print("--- Task: Searching for pattern ---")
                cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", ("J",))
                results = cur.fetchall()
                for row in results:
                    print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
                
                
                # 4. TASK: Pagination (Function)
                # Matches function: get_contacts_paged(p_limit, p_offset)
                print("\n--- Task: Pagination (Limit 10, Offset 2) ---")
                cur.execute("SELECT * FROM get_contacts_paged(%s, %s)", (100, 0))
                page_results = cur.fetchall()
                for row in page_results:
                    print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")


                # 5. TASK: Delete user
                # Matches procedure: delete_contact(p_search)
                #print("\n--- Task: Deleting contact 'Bob' ---")
                #cur.execute("CALL delete_contact(%s)", ("Bob",))

                # Save all changes
                conn.commit()
                print("\nLab tasks completed and committed successfully!")

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    run_lab_tasks()
-- procedures.sql

-- 1. Insert or update a single user
CREATE OR REPLACE PROCEDURE insert_or_update_user(u_name TEXT, u_surname TEXT, u_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = u_name AND surname = u_surname) THEN
        UPDATE phonebook
        SET phone = u_phone
        WHERE name = u_name AND surname = u_surname;
    ELSE
        INSERT INTO phonebook (name, surname, phone)
        VALUES (u_name, u_surname, u_phone);
    END IF;
END;
$$;

-- 2. Insert many users with validation
CREATE OR REPLACE PROCEDURE insert_many_users(users TEXT[][])
LANGUAGE plpgsql
AS $$
DECLARE
    user_record TEXT[3];
BEGIN
    FOREACH user_record SLICE 1 IN ARRAY users LOOP
        IF user_record[3] !~ '^[0-9\-]+$' THEN
            RAISE NOTICE 'Invalid phone: % for user % %', user_record[3], user_record[1], user_record[2];
        ELSE
            CALL insert_or_update_user(user_record[1], user_record[2], user_record[3]);
        END IF;
    END LOOP;
END;
$$;

-- 3. Delete contact by name or phone
CREATE OR REPLACE PROCEDURE delete_contact_by_name_or_phone(u_name TEXT, u_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = u_name OR phone = u_phone;
END;
$$;
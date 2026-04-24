-- 1. Procedure to Insert or Update
CREATE OR REPLACE PROCEDURE upsert_user(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    INSERT INTO contacts (first_name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (phone) DO UPDATE SET first_name = EXCLUDED.first_name;
END;
$$ LANGUAGE plpgsql;

-- 2. Procedure to Delete
CREATE OR REPLACE PROCEDURE delete_contact(p_search VARCHAR)
AS $$
BEGIN
    DELETE FROM contacts 
    WHERE first_name = p_search OR phone = p_search;
END;
$$ LANGUAGE plpgsql;

-- 3. Procedure for Bulk Insert with Loop
CREATE OR REPLACE PROCEDURE bulk_insert(names TEXT[], phones TEXT[])
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_upper(names, 1) LOOP
        IF LENGTH(phones[i]) >= 10 THEN
            INSERT INTO contacts (first_name, phone) 
            VALUES (names[i], phones[i])
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            RAISE NOTICE 'Skipping invalid phone: %', phones[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
-- functions.sql

-- 1. Search contacts by pattern
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.surname, p.phone
    FROM phonebook AS p
    WHERE p.name ILIKE '%' || pattern || '%'
       OR p.surname ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Pagination function
CREATE OR REPLACE FUNCTION get_phonebook_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.surname, p.phone
    FROM phonebook AS p
    ORDER BY p.id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;
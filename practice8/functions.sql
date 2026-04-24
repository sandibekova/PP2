-- 1. Function to search by pattern
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(search_pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.first_name, c.phone 
    FROM contacts c 
    WHERE c.first_name ILIKE '%' || search_pattern || '%' 
       OR c.phone ILIKE '%' || search_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Function for pagination
CREATE OR REPLACE FUNCTION get_contacts_paged(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.first_name, c.phone 
    FROM contacts c 
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
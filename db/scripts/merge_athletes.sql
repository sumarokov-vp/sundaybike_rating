CREATE OR REPLACE FUNCTION public.merge_athletes (original_id INTEGER, duplicate_id INTEGER)
    RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
  UPDATE race_results SET athlete_id = original_id WHERE athlete_id = duplicate_id;
  DELETE FROM athlete_categories WHERE athlete_id = duplicate_id;
  DELETE FROM athletes WHERE id = duplicate_id;
END;
$$;

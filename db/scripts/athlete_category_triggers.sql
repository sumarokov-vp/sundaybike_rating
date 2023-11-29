CREATE OR REPLACE FUNCTION public.athlete_category_after_insert ()
    RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $$
DECLARE
  previous_id INTEGER;
BEGIN
  SELECT id INTO previous_id FROM athlete_categories WHERE athlete_id = NEW.athlete_id AND "end" IS NULL and id != NEW.id;
  update athlete_categories SET "end" = NEW."start" - INTERVAL '1 day' WHERE id = previous_id;
  RETURN NEW;
END;
$$;
--

CREATE OR REPLACE TRIGGER after_insert AFTER INSERT ON public.athlete_categories FOR EACH ROW EXECUTE FUNCTION public.athlete_category_after_insert ();


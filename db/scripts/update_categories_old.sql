CREATE OR REPLACE FUNCTION public.update_categories ()
    RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN

  -- MEN
  INSERT INTO athlete_categories (athlete_id, category_id, start)
  SELECT
    q1.athlete_id,
    CASE
      WHEN q1.rank <= 20 THEN 1
      WHEN q1.rank > 20 and q1.rank <= 40 THEN 2
      WHEN q1.rank > 40 THEN 3
    END AS category_id,
    CURRENT_DATE
  FROM
  (
    SELECT
      SUM(result_points) "points",
      athlete_id,
      rank() OVER (ORDER BY SUM(result_points) DESC)
    FROM race_results
    INNER JOIN races ON race_results.race_id = races.id
    INNER JOIN athletes ON race_results.athlete_id = athletes.id
    WHERE
      races.date_start >= '2023-01-01'
      AND races.date_start <= '2023-12-31'
      AND athletes.sex_id = 1
    GROUP BY athlete_id
    ORDER BY sum(result_points) DESC
  ) as q1
  ON CONFLICT (athlete_id, start) DO NOTHING;

  -- WOMEN
  INSERT INTO athlete_categories (athlete_id, category_id, start)
  SELECT
    q1.athlete_id,
    CASE
    WHEN q1.rank <= 10 THEN 1
    WHEN q1.rank > 10 and q1.rank <= 20 THEN 2
    WHEN q1.rank > 20 THEN 3
    END AS category_id,
    CURRENT_DATE
  FROM
  (
    SELECT
      SUM(result_points) "points",
      athlete_id,
      rank() OVER (ORDER BY SUM(result_points) DESC)
    FROM race_results
    INNER JOIN races ON race_results.race_id = races.id
    INNER JOIN athletes ON race_results.athlete_id = athletes.id
    WHERE
      races.date_start >= '2023-01-01'
      AND races.date_start <= '2023-12-31'
      AND athletes.sex_id = 2
    GROUP BY athlete_id
    ORDER BY sum(result_points) DESC
  ) as q1
  ON CONFLICT (athlete_id, start) DO NOTHING;
END;
$$;

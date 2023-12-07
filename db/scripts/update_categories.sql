CREATE OR REPLACE FUNCTION public.update_categories ()
    RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
  UPDATE athletes
  SET category_id= lev_3.best_category_id
  FROM (
    SELECT
      MIN(race_category) as best_category_id,
      athlete_id
    FROM
    (SELECT
      lev_1.*,
      round(race_rank::NUMERIC/cnt*100::NUMERIC, 1) as relative_rank,
      CASE
        WHEN race_rank::NUMERIC/cnt*100 <= a_category_percentage OR athlete_sex_id = 2
          THEN 1
        WHEN race_rank::NUMERIC/cnt*100 > a_category_percentage
          THEN 2
      END race_category
    FROM
    (SELECT race_results.result_time,
                rank() OVER (PARTITION BY race_results.race_id, athletes.sex_id ORDER BY race_results.result_time) AS race_rank,
                race_results.race_id,
                athletes.id AS athlete_id,
                athletes.name AS athlete_name,
                athletes.sex_id AS athlete_sex_id,
                race_classes.a_category_percentage,
                counts.cnt
              FROM race_results
                JOIN athletes ON race_results.athlete_id = athletes.id
                JOIN athlete_categories ON athlete_categories.athlete_id = race_results.athlete_id
                JOIN races ON race_results.race_id = races.id
                JOIN race_classes ON race_classes.id = races.race_class_id
                JOIN (
                  SELECT count(race_id) as cnt, athletes.sex_id, race_id  
            FROM race_results
            JOIN athletes ON athletes.id = race_results.athlete_id
            GROUP BY athletes.sex_id, race_id
            ORDER BY race_id, athletes.sex_id
                ) counts on (counts.race_id = race_results.race_id AND counts.sex_id = athletes.sex_id)
    ) as lev_1
    ) as lev_2
    GROUP BY athlete_id
    ORDER BY MIN(race_category), athlete_id
  ) as lev_3
  WHERE athletes.id = lev_3.athlete_id;
END;
$$;

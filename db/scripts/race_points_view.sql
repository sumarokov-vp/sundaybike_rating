DROP VIEW IF EXISTS season_points;
DROP VIEW IF EXISTS race_points;
CREATE OR REPLACE VIEW race_points AS
  SELECT
    row_number() OVER () AS id,
    race_ranks.result_time,
    race_ranks.race_rank,
    race_ranks.race_id,
    races."name" as race_name,
    race_ranks.category_id,
    categories."name" as category_name,
    race_ranks.athlete_id,
    race_ranks.athlete_name,

    race_ranks.athlete_sex_id sex_id,
    points_for_place.points::numeric * race_classes.multiplier AS race_points,
    date_part('Year'::text, races.date_start) AS season
  FROM (
      SELECT race_results.result_time,
            rank() OVER (PARTITION BY race_results.race_id, athletes.sex_id, athlete_categories.category_id ORDER BY race_results.result_time) AS race_rank,
            race_results.race_id,
            athlete_categories.category_id,
            athletes.id AS athlete_id,
            athletes.name AS athlete_name,
            athletes.sex_id AS athlete_sex_id
           FROM race_results
             JOIN athletes ON race_results.athlete_id = athletes.id
             JOIN athlete_categories ON athlete_categories.athlete_id = race_results.athlete_id
  ) race_ranks
  JOIN points_for_place ON points_for_place.sex_id = race_ranks.athlete_sex_id AND points_for_place.place = race_ranks.race_rank
  JOIN races ON race_ranks.race_id = races.id
  JOIN race_classes ON race_classes.id = races.race_class_id
  JOIN categories ON categories.id = race_ranks.category_id
  ORDER BY date_part('Year'::text, races.date_start), races.date_start, race_ranks.race_id, race_ranks.athlete_sex_id, race_ranks.category_id, race_ranks.race_rank;


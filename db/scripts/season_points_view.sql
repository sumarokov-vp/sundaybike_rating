DROP VIEW IF EXISTS season_points;

CREATE OR REPLACE VIEW season_points AS
  SELECT
    row_number() OVER () AS id,
    race_points.season,
    race_points.sex_id as sex_id,
    race_points.category_id,
    categories."name" as category_name,

    rank() OVER (PARTITION BY race_points.season, race_points.sex_id, race_points.category_id ORDER BY sum(race_points.race_points) desc) AS "rank",
    race_points.athlete_id,
    athletes."name" as athlete_name,
    sum(race_points.race_points) as points
  FROM race_points
  INNER JOIN athletes on athletes.id = race_points.athlete_id
  INNER JOIN categories on categories.id = race_points.category_id

  GROUP BY
    race_points.season,
    athlete_id,
    categories."name",
    athletes."name",
    race_points.category_id,
    race_points.sex_id
  ORDER BY race_points.season, race_points.sex_id, race_points.category_id, sum(race_points.race_points) desc;


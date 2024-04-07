DROP VIEW IF EXISTS race_points;
CREATE OR REPLACE VIEW race_points AS
SELECT
	race_ranks.result_time,
	race_ranks.race_rank,
	race_ranks.race_id,
	races.name AS race_name,
	1 AS category_id,
	'A'::character varying (90) AS category_name,
	race_ranks.athlete_id,
	race_ranks.athlete_name,
	race_ranks.athlete_sex_id AS sex_id,
	row_number() OVER () AS id,
	points_for_place.points::numeric * race_classes.multiplier AS race_points,
  date_part('Year'::text, races.date_start)::varchar AS season
FROM (
	SELECT
		race_results.result_time,
		race_results.race_id,
		athletes.id AS athlete_id,
		athletes.name AS athlete_name,
		athletes.sex_id AS athlete_sex_id,
		rank() OVER (PARTITION BY race_results.race_id,
			athletes.sex_id ORDER BY race_results.result_time) AS race_rank
	FROM
		race_results
		JOIN athletes ON race_results.athlete_id = athletes.id) race_ranks
	JOIN points_for_place ON race_ranks.athlete_sex_id = points_for_place.sex_id
		AND race_ranks.race_rank = points_for_place.place
	JOIN races ON race_ranks.race_id = races.id
	JOIN race_classes ON races.race_class_id = race_classes.id
ORDER BY
	(date_part('Year'::text, races.date_start)),
	races.date_start,
	race_ranks.race_id,
	race_ranks.athlete_sex_id,
	race_ranks.race_rank;


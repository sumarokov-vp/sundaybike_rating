DROP VIEW IF EXISTS season_points;

CREATE OR REPLACE VIEW season_points AS
 SELECT
	row_number() OVER () AS id,
	race_points.season,
	race_points.sex_id,
	1 AS category_id,
	'A'::text AS category_name,
	rank() OVER (PARTITION BY race_points.season,
		race_points.sex_id ORDER BY (sum(race_points.race_points))
	DESC) AS rank,
race_points.athlete_id,
athletes.name AS athlete_name,
sum(race_points.race_points) AS points
FROM
	race_points
	JOIN athletes ON athletes.id = race_points.athlete_id
GROUP BY
	race_points.season,
	race_points.athlete_id,
	athletes.name,
	race_points.sex_id
ORDER BY
	race_points.season,
	race_points.sex_id,
	(sum(race_points.race_points))
	DESC;


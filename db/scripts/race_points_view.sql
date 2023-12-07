DROP VIEW IF EXISTS season_points;
DROP VIEW IF EXISTS race_points;
CREATE OR REPLACE VIEW race_points AS
SELECT
    race_ranks.result_time,
    race_ranks.race_rank,
    race_ranks.race_id,
    races.name AS race_name,
    race_ranks.category_id,
    categories.name AS category_name,
    race_ranks.athlete_id,
    race_ranks.athlete_name,
    race_ranks.athlete_sex_id AS sex_id,

    row_number() OVER () AS id,
    points_for_place.points::numeric * race_classes.multiplier AS race_points,
    date_part('Year'::text, races.date_start) AS season
FROM (
    SELECT
        race_results.result_time,
        race_results.race_id,
        athletes.category_id,
        athletes.id AS athlete_id,
        athletes.name AS athlete_name,
        athletes.sex_id AS athlete_sex_id,
        rank()
            OVER (
                PARTITION BY
                    race_results.race_id, athletes.sex_id, athletes.category_id
                ORDER BY race_results.result_time
            )
            AS race_rank
    FROM race_results
    INNER JOIN athletes ON race_results.athlete_id = athletes.id
) AS race_ranks
INNER JOIN
    points_for_place
    ON
        race_ranks.athlete_sex_id = points_for_place.sex_id
        AND race_ranks.race_rank = points_for_place.place
INNER JOIN races ON race_ranks.race_id = races.id
INNER JOIN race_classes ON races.race_class_id = race_classes.id
INNER JOIN categories ON race_ranks.category_id = categories.id
ORDER BY
    date_part('Year'::text, races.date_start), races.date_start, race_ranks.race_id, race_ranks.athlete_sex_id, race_ranks.category_id, race_ranks.race_rank;

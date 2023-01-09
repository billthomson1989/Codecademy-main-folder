--1 finding the size of the table 
SELECT pg_size_pretty(
  pg_table_size('sensors.observations')
);

--2 getting the indexes with its size
SELECT indexname FROM pg_indexes WHERE tablename ='observations';
SELECT pg_size_pretty(pg_total_relation_size('sensors.observations_pkey')) as primary_key_size,
 pg_size_pretty(pg_total_relation_size('sensors.observations_location_id_datetime_idx')
) as location_id_datetime_idx_size; 

--3 returning table data, indexes and total relation size
SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) as tbl_size, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) as idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) as total_size;

--4 updating distance from feet to meters
 UPDATE sensors.observations 
SET distance = (distance * 3.281) 
WHERE TRUE;

--5 checking the size of the tables and indexes 
SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) as tbl_size, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) as idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) as total_size;

--6 run a vacuum on the table
VACUUM sensors.observations;
-- checking table size after vacuum
SELECT pg_size_pretty(
  pg_table_size('sensors.observations')
);

--7 adding more observations to the table
\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './additional_obs_types.csv' WITH DELIMITER ',' CSV HEADER;

--8 checking table size
SELECT pg_size_pretty(
  pg_table_size('sensors.observations')
);

--9 running vacuum full on table
VACUUM FULL sensors.observations;
--checking table size
SELECT pg_size_pretty(
  pg_table_size('sensors.observations')
);

--10 deleting data from table where location_id > 24
DELETE FROM sensors.observations
WHERE location_id > 24;

--11 table size check
SELECT pg_size_pretty(
  pg_table_size('sensors.observations')
);

--12 truncate table
TRUNCATE sensors.observations;

--13
\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './original_obs_types.csv' WITH DELIMITER ',' CSV HEADER;
 
\COPY sensors.observations (id, datetime, location_id, duration, distance, category) FROM './additional_obs_types.csv' WITH DELIMITER ',' CSV HEADER;

--14 checking the size of the total table, index and combined size of the table
SELECT 
    pg_size_pretty(pg_table_size('sensors.observations')) as tbl_size, 
    pg_size_pretty(pg_indexes_size('sensors.observations')) as idx_size,
    pg_size_pretty(pg_total_relation_size('sensors.observations')) as total_size;

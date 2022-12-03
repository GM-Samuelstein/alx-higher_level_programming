<h1 align="center"><b>0x0E-SQL MORE QUERIES</b></h1>

More SQL...
<ul>
<li>Create a new user, grant the new user privileges and show all the privileges that a user has.</li>
<li>Add DEFAULT, NOT NULL, PRIMARY KEY, FOREIGN KEY, AUTO GENERATE and UNIQUE attributes to fields in a table.</li>
<li>Manipulate and work with data from different tables using SQL SUBQUERY and SQL JOIN.</li>
</ul>

|SQL File| Description|
|---|---|
|[0-privileges.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql)|Lists all privileges of some given users in a MySQL server.|
|[1-create_user.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql)|Creates a new user in a MySQL server, sets a password for the user, and grants the user ALL privileges.|
|[2-create_read_user.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql)|Creates a new database and a new user in the database, sets a password for the user, and grants the user only the SELECT privilege, in a MySQL server.|
|[3-force_name.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql)|Creates a new table in a database in a MySQL server and sets the value of one of the fields to NOT NULL.|
|[4-never_empty.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/4-never_empty.sql)|Creates a new table in a database in a MySQL server, and adds a default value to one of the fields.|
|[5-unique_id.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/5-unique_id.sql)|Creates a new table in a database in a MySQL server, and adds a default value to one of the fields, and also makes each field data unique.|
|[6-states.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/6-states.sql)|Creates a new database and a new table in the database, and adds NOT NULL, PRIMARY KEY, and AUTO GENERATE attributes to one of the fields, and also makes each data in the field unique.|
|[7-cities.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/7-cities.sql)|Creates a new database and a new table in the database, and adds NOT NULL, PRIMARY KEY, FOREIGN KEY and AUTO GENERATE attributes to one of the fields, and also makes each data in the field unique.|
|[8-cities_of_california_subquery.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql)|Filters out some records of selected fields from a table in a database, that passes a specified condition, in a MySQL server using SQL SUBQUERY, and displays them in a particular order.|
|[9-cities_by_state_join.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/9-cities_by_state_join.sql)|Filters out some records of selected fields from a table in a database, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|[10-genre_id_by_show.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/10-genre_id_by_show.sql)|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|[11-genre_id_all_shows.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/11-genre_id_all_shows.sql)|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|[12-no_genre.sql](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/12-no_genre.sql)|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|13-count_shows_by_genre.sql|Displays the number of some selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|14-my_genres.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|15-comedy_only.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|16-shows_by_genre.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|100-not_my_genres.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN and SQL SUBQUERY, and displays them in a particular order.|
|101-not_a_comedy.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql`, that passes a specified condition, in a MySQL server using SQL JOIN and SQL SUBQUERY, and displays them in a particular order.|
|102-rating_shows.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows_rate.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|103-rating_genres.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows_rate.sql`, that passes a specified condition, in a MySQL server using SQL JOIN, and displays them in a particular order.|
|hbtn_0d_tvshows.sql|A SQL database dump containing three tables. <ul><li>tv_genres: A SQL table that records tv genres and their IDs.</li><li>tv_show_genres: A SQL table that records genre_IDs and show_IDs.</li><li>tv_shows: A SQL table that records tv_show titles and their IDs.</li></ul>|
|hbtn_0d_tvshows_rate.sql|A SQL database dump containing four tables. <ul><li>tv_genres: A SQL table that records tv genres and their IDs.</li><li>tv_show_genres: A SQL table that records genre_IDs and show_IDs.</li><li>tv_show_ratings:  A SQL table that records tv_show ratings and their IDs.</li><li>tv_shows: A SQL table that records tv_show titles and their IDs.</li></ul>|

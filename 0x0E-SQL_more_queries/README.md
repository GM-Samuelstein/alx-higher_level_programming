<h1 align="center"><b>0x0E-SQL MORE QUERIES</b></h1>

More SQL...
<ul>
<li>Create a new user, grant the new user privileges and show all the privileges that a user has.</li>
<li>Add DEFAULT, NOT NULL, PRIMARY KEY, FOREIGN KEY, AUTO GENERATE and UNIQUE attributes to fields in a table.</li>
<li></li>
<li></li>
</ul>

|SQL File| Description|
|---|---|
|0-privileges.sql|Lists all privileges of some given users in a MySQL server.|
|1-create_user.sql|Creates a new user in a MySQL server, sets a password for the user, and grants the user ALL privileges.|
|2-create_read_user.sql|Creates a new database and a new user in the database, sets a password for the user, and grants the user only the SELECT privilege, in a MySQL server.|
|3-force_name.sql|Creates a new table in a database in a MySQL server and sets the value of one of the fields to NOT NULL.|
|4-never_empty.sql|Creates a new table in a database in a MySQL server, and adds a default value to one of the fields.|
|5-unique_id.sql|Creates a new table in a database in a MySQL server, and adds a default value to one of the fields, and also makes each field data unique.|
|6-states.sql|Creates a new database and a new table in the database, and adds NOT NULL, PRIMARY KEY, and AUTO GENERATE attributes to one of the fields, and also makes each data in the field unique.|
|7-cities.sql|Creates a new database and a new table in the database, and adds NOT NULL, PRIMARY KEY, FOREIGN KEY and AUTO GENERATE attributes to one of the fields, and also makes each data in the field unique.|
|8-cities_of_california_subquery.sql|Filters out some records of selected fields from a table in a database in a MySQL server using SQL SUBQUERY, and displays them in a particular order.|
|9-cities_by_state_join.sql|Filters out some records of selected fields from a table in a database in a MySQL server using SQL JOIN, and displays them in a particular order.|
|10-genre_id_by_show.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql` in a MySQL server using SQL JOIN, and displays them in a particular order.|
|11-genre_id_all_shows.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql` in a MySQL server using SQL JOIN, and displays them in a particular order.|
|12-no_genre.sql|Filters out some records of selected fields from the database dump `hbtn_0d_tvshows.sql` in a MySQL server using SQL JOIN, and displays them in a particular order.|
|13-count_shows_by_genre.sql|Displays the number of some selected fields from the database dump `hbtn_0d_tvshows.sql` in a MySQL server using SQL JOIN, and displays them in a particular order.|
|14-my_genres.sql||
|15-comedy_only.sql||
|16-shows_by_genre.sql||
|100-not_my_genres.sql||
|101-not_a_comedy.sql||
|102-rating_shows.sql||
|103-rating_genres.sql||
|hbtn_0d_tvshows.sql||

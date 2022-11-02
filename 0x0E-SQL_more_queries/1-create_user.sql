--- Script that creates the MYSQL server user user_0d_1.
-- Creates the user user_0d_1 with all privilege.
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost'
   IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;

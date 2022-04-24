
# APP Database With Three Tables
MariaDB [app]> select * from admin;
+-----------------+----------+
| email           | password |
+-----------------+----------+
| rohan@gmail.com | 12345    |
+-----------------+----------+
1 row in set (0.029 sec)

MariaDB [app]> select * from info;
+---------+-------------------+----------+
| name    | email             | password |
+---------+-------------------+----------+
| Golu    | golu123@gmail.com | 456789   |
| shivani | shivani@gmail.com | 123      |
+---------+-------------------+----------+
2 rows in set (0.001 sec)

MariaDB [app]> select * from contact;
+--------------+------------+-------------------+---------+
| name         | number     | email             | message |
+--------------+------------+-------------------+---------+
| Rohan Rawool | 2147483647 | golu@gmail.cb     | fff     |
| user         | 2147483647 | test@gmail.com    | hello   |
| Sarvesh      | 2147483647 | golu@gmail.cb     | Laptop  |
| user         | 2147483647 | user@gmail.com    | hey     |
| user1        | 563465464  | user1@gmail.com   | hellooo |
| sarthak      | 2147483647 | sarthak@gmail.com | Hiiiiii |
| aniket       | 9623603836 | aniket@gmail.com  | hii     |
| saurabh      | 9892979465 | saurabh@gmail.com | Laptop  |
| saurabh      | 9892979465 | saurabh@gmail.com | Laptop  |
| amol sir     | 9656457896 | amol@gmail.com    | Hiii    |
|              |            |                   |         |
| abdc         | 8978451465 | abc@gmail.com     | 23      |
| shivani      | 8888457865 | shivani@gmail.com | Hii     |
+--------------+------------+-------------------+---------+
13 rows in set (0.001 sec)

MariaDB [app]>

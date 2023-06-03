# <span style="color:#f6fc2d">Relational Databases</span>

Relational databases model data by storing rows and columns in tables.<br>
The power of the relational database lies in its ability to efficiently<br>
retrieve data from those tables and in particular where there are multiple<br>
tables and the relationships between those tables involved in the query.

## <span style="color:#f6fc2d">Terminology</span>

- <span style="color:#f6fc2d">Database</span> - contains many tables
- <span style="color: #94ed1f">Relation (or table)</span> - contains tuples and attributes
- <span style="color:#ed971f">Tuple (or row)</span> - a set of fields that generally represents an "object" like a person or a music track
- <span style="color:#c">Attribute (also column or field)</span> - one of possibly many elements of data corresponding to the object represented by the row

![database](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Relational_database_terms.svg/1200px-Relational_database_terms.svg.png)

A <span style="color: #94ed1f">relation</span> is defined as a <span style="color: #94ed1f">set of</span> <span style="color: #ed971f">tuples</span> that have the seam <span style="color: #ae1fd1">attributes</span>. A <span style="color: #ed971f">tuple</span><br>
usually represents <span style="color: #ed971f">an object</span> and information about that object. <span style="color: #ed971f">Object</span> are <br>
typically physical objects or concepts. A <span style="color: #94ed1f">relation</span> is usually described as a <span style="color: #94ed1f">table</span>,<br>
which is organized into <span style="color: #ed971f">rows</span> and <span style="color: #ae1fd1">columns</span>. All tha data_referenced by an <br>
<span style="color: #ae1fd1">attribute</span> are in the same domain and <span style="color: #ae1fd1">conform to the same constrains</span>.

## <span style="color:#f6fc2d">SQL</span>

- Structured Query Language is the language we use to issue commands to the database
  - Create a table
  - Retrieve some data
  - Insert data
  - Delete data

# <span style="color:#f6fc2d">Using Databases</span>

## <span style="color:#f6fc2d">Two roles in Large Projects</span>

- <span style="color: #ae1fd1">Application Developer</span> - Builds the logic for the application, the <br>
  look and feel of the application - monitors the application for problems
- <span style="color:#f6fc2d">Database Administrator</span> - Monitors and adjusts the database as the program runs in production
- Often both people participate in the building of the "Data model"

### <span style="color:#f6fc2d">Database Administrator (dba)</span>

A database administrator (DBA) is a person responsible for the<br>
design, implementation, maintenance, and repair of an organization's <br>
database. The role includes the development and design of database <br>
strategies, monitoring and improving database performance and capacity,<br>
and planning for future expansion requirements. They may also plan, coordinate,<br>
and implement security measures to safeguard the database.

## <span style="color:#f6fc2d">Database Model</span>

A <span style="color: #94ed1f">database model</span> or <span style="color: #94ed1f">database schema</span> is the <span style="color: #ae1fd1">structure or format of a database</span>,<br>
described in a formal language supported by the database management system, In <br>
other words, a "database model" is the application of a data model when used in <br>
conjunction with a database management system.

## <span style="color:#f6fc2d">Common Database System</span>

- Three Major Database Management systems in wide use
  - <span style="color: #94ed1f">Oracle</span> - Large, commercial, enterprise-scale, very very tweakable
  - <span style="color: #94ed1f">MySql</span> - Simpler but very fast and scalable - commercial open source
  - <span style="color: #94ed1f">SqlServer</span> - Very nice - from Microsoft (also Access)
- May other smaller projects free and open source
  - HSQL, <span style="color: #94ed1f">SQLite</span>, Postgress,...

## <span style="color:#f6fc2d">SQLite Browser</span>

- SQLite is a very popular database - it is free and fast and small
- SQLite Browser allows us to do directly manipulate SQLite files
  - [SQLite](https://sqlitebrowser.org/)

There is also a Firefox plugin to manipulate SQLite database

- [plugin](https://addons.mozilla.org.en-US/firefox.addon/sqlite-manager/)

SQLite is embedded in python and a number of other languages

## <span style="color:#f6fc2d">Start Simple a A Single Table</span>

```sql
CREATE TABLE Users(
    name VARCHAR(128)
    email VARCHAR(128)
)
```

### <span style="color:#f6fc2d">SQL Insert</span>

The Insert statement inserts a row into the table

```sql
INSERT INTO Users (name,email) VALUES ('Kristin', 'kf@umich.edu')
```

### <span style="color:#f6fc2d">SQL Delete</span>

Deletes a row in a table based on a selection criteria

```sql
DELETE FROM Users WHERE email='ted@umich.edu'
```

### <span style="color:#f6fc2d">SQL Update</span>

Deletes a row in a table based on a selection criteria

```sql
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'
```

### <span style="color:#f6fc2d">Retrieving Records Select</span>

The select statement retrieves a group of records - you can either<br>
retrieve all the records or a subset of the records with a WHERE clause

```sql
SELECT * FROM Users WHERE email='csev@umich.edu'
```

### <span style="color:#f6fc2d">Sorting with ORDER BY</span>

You can add an <span style="color:#ed971f">ORDER BY</span> clause to <span style="color:#ed971f">SELECT</span> statements to get<br>
the results sorted in ascending or descending order

```sql
SELECT * FROM Users ORDER BY email
```

# <span style="color:#f6fc2d">Designing a Data Model</span>

## <span style="color:#f6fc2d">Database Design</span>

- Database design is an <span style="color:#94ed1f">art from</span> of its own with particular<br>
  skills and experience
- Our goal is to avoid the really bad mistakes and design<br>
  clean and easily understood databases
- Others may performance tune things later
- Database design starts with a picture..

![design](https://images.slideplayer.com/30/9505002/slides/slide_39.jpg)

## <span style="color:#f6fc2d">Building a Data Model</span>

- Drawing a picture of the data objects for our application<br>
  and then figuring out how to represent the objects and <br>
  their relationships
- Basic Rule: Don't put the same string data in twice - use a <br>
  relationship instead
- When there is one thing in the "real world" there should <br>
  be one copy of that thing in the database

### <span style="color:#f6fc2d">For each "piece of info"...</span>

- Is the column an object or an attribute of another object?
- Once we define objects, we need to define the relationships<br>
  between the objects

## <span style="color:#f6fc2d">Representing a Data Model in Tables</span>

```sql
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
)
```

```sql
CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
)
```

```sql
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT
)
```

```sql
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT,
    artist_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
)
```

## <span style="color:#f6fc2d">Inserting Relational Data</span>

```sql
insert into Artist (name) values ('led Zepplin')
```

```sql
insert into Artist (name) values ('AC/DC')
```

```sql
insert into Genre (name) values ('Rock');
insert into Genre (name) values ('Metal')
```

```sql
insert into Album (title, artist_id) values ('Who Made Who', 2);
insert into Album (title, artist_id) values ('IV', 1)
```

```sql
insert into Track (title, rating, len, count, album_id, genre_id) values ('Black Dog', 5, 297, 0, 2, 1);
insert into Track (title, rating, len, count, album_id, genre_id) values ('Stairway', 5, 482, 0, 2, 1);
insert into Track (title, rating, len, count, album_id, genre_id) values ('About to Rock', 5, 313, 0, 1, 2);
insert into Track (title, rating, len, count, album_id, genre_id) values ('Who Made Who', 5, 207, 0, 1, 2)
```

# <span style="color:#f6fc2d">Reconstructing Data with JOIN</span>

## <span style="color:#f6fc2d">Relational Power</span>

- By removing the replicated data and replacing it with<br>
  references to a single copy of each bit of data we build a <br>
  "<span style="color:#ae1fd1">web</span>" of information that the relational database can read<br>
  through very quickly - even for very large amounts of data
- Often when you want some data it comes from a number <br>
  of tables linked by these <span style="color:#ae1fd1">foreign keys</span>
## <span style="color:#f6fc2d">The JOIN Operation</span>
- The JOIN operation <span style="color:#ae1fd1">links across several tables as</span> part of a select<br>
  operation
- You must tell the JOIN <span style="color:#94ed1f">how to use the keys</span> that make the <br>
  connection between the tables using an <span style="color:#94ed1f">ON clause</span>

```sql
select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
```
```sql
select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id
```
## <span style="color:#f6fc2d">It can get complex...</span>
```sql
select Track.title, Artist.name, Album.title, Genre.name from 
Track join Genre join Album join Artist on Track.genre_id = 
Genre.id and Track.album_id = Album.id and Album.artist_id = 
Artist.id
```


# <span style="color:#f6fc2d">Many-to-Many Relationships</span>
## <span style="color:#94ed1f">Many-to-Many</span>
- Sometimes we need to model a relationship that is <br>
  many-to-many
- We need to add a "connection" table with two foreign keys
- There is usually no separate primary key
  
![data model](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/CPT-Databases-ManytoMany.svg/250px-CPT-Databases-ManytoMany.svg.png)
![data model](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Databases-ManyToManyWJunction.jpg/250px-Databases-ManyToManyWJunction.jpg)

## <span style="color:#94ed1f">Start with a Fresh Database</span>

```sql
CREATE TABLE User(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT,
  email TEXT
);
CREATE TABLE Course(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title TEXT,
);
CREATE TABLE Member(
  user_id INTEGER,
  course_id INTEGER,
  role INTEGER,
  PRIMARY KEY (user_id,course_id)
)
```
## <span style="color:#94ed1f">Insert Users and Courses</span>
```sql
INSERT INTO User (name, email) VALUES ('Jane','jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed','ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue','sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');
```
## <span style="color:#94ed1f">Insert Memberships</span>
```sql
INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1);
INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0);
INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0);

INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0);
INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1);

INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1);
INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0);
```
```sql
SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name
```
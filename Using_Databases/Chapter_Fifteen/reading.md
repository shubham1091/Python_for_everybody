# <span style="color:#f6fc2d">Relational Databases</span>
Relational databases model data by storing rows and columns in tables.<br>
The power of the relational database lies in its ability to efficiently<br>
retrieve data from those tables and in particular where there are multiple<br> 
tables and the relationships between those tables involved in the query.

## <span style="color:#f6fc2d">Terminology</span>
- <span style="color:#f6fc2d">Database</span> - contains many tables
- <span style="color: #94ed1f">Relation (or table)</span> - contains tuples and attributes
- <span style="color:#ed971f">Tuple (or row)</span> - a set of fields that generally represents an "object" like a person or a music track
- <span style="color:#ae1fd1">Attribute (also column or field)</span> - one of possibly many elements of data corresponding to the object represented by the row

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
    - Oracle - Large, commercial, enterprise-scale, very very tweakable
    - MySql - Simpler but very fast and scalable - commercial open source
    - SqlServer - Very nice - from Microsoft (also Access)
- May other smaller projects free and open source
    - HSQL, SQLite, Postgress,...

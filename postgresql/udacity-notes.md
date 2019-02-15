# Udacity course: Intro to Relational Databases

https://classroom.udacity.com/courses/ud197

### Some handy code snippets

**lesson 2: elements of SQL**
**joining tables**
```
QUERY = '''
select name from animals, diet where animals.species = diet.species and diet.food = 'fish'
'''
```

**adding rows**
```
SELECT_QUERY = ''' 
select name, birthdate from animals where species = 'opossum';
'''
INSERT_QUERY = '''
insert into animals values('rachel', 'opossum', '2019-01-07');
'''
```

**count**
```
QUERY = "select count (*) as num, species from animals group by species order by num desc";
```

**lesson 2: more join practice**
**List all the taxonomic orders, using their common names, sorted by the number of animals of that order that the zoo has.**

The animals table has (name, species, birthdate) for each individual.
The taxonomy table has (name, species, genus, family, t_order) for each species.
The ordernames table has (t_order, name) for each order.

Be careful:  Each of these tables has a column "name", but they don't have the same meaning!  animals.name is an animal's individual name.  taxonomy.name is a species' common name (like 'brown bear').  And ordernames.name is the common name of an order (like 'Carnivores').

```
QUERY = '''
select ordernames.name, count(*) as num
from animals, taxonomy, ordernames
where animals.species = taxonomy.name
and taxonomy.t_order = ordernames.t_order
group by ordernames.name
order by num desc
'''
```

answer:

|                name | num |
---------------------:|----:|
| even-toed ungulates |  29 |
|          carnivores |  25 |
|            primates |  15 |
|  odd-toed ungulates |   7 |
|  lizards and snakes |   4 |
|          monotremes |   4 |
|          marsupials |   3 |
| whales and dolphins |   2 |

### lesson 3: Python DB-API
**example of python db-api**
```
Import sqlite

conn = splite3.connect('database-i-want') #can also specify hostname, username, password, etc 
cursor = conn.cursor() #the cursor runs queries and fetches results, like a text cursor
cursor.execute("select something from table")
results = cursor.fetchall() #we can also fetchone
print(results)
conn.close() #always close the connection
```

**inserts in db api**
```
import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit() #**commit to the database**
db.close()
```


# postgresql

Useful for setting up PostGreSQL:
- Setting up on linux for the first time, tutorials with [boundlessgeo](http://suite.opengeo.org/docs/latest/dataadmin/pgGettingStarted/firstconnect.html)
- ```sudo -u postgres psql -l``` - to see all existing dbs
- if i want to create a new db with postgis extension I can do this in [pgadmin 3](http://connect.boundlessgeo.com/docs/suite/4.6/dataadmin/pgGettingStarted/createdb.html) or in the command line 
```
createdb -U postgres <DATABASENAME>
psql -U postgres -d <DATABASENAME> -c 'CREATE EXTENSION postgis'
```

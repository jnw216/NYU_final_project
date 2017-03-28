#Creating a full stack application in Flask

Step 1)

Create the database in postgresql:

[referenced here](https://github.com/EricSchles/postgres_flask_macosx)

`createuser -P -s -e -d username`

`createdb database_name -U username`

please replace database_name and username with the names germaine to your db and user.

Step 2)

from the top level directory of your application run:

python:

```
>>> from app import db
>>> app.create_all()
(type CTRL-C to escape this REPL)
```


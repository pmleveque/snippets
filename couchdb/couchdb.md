# Resolution for exercice #3 from learnyoucouch (from nodeschool.io)

Create a view for the database things-learn-couchdb which will just output all
the things which have the material metal.

The database is located at http://localhost:5984/things-learn-couchdb
and an example document in this database looks like:

    {
      "_id": "4a7bd4d6e47564639585459049000e15",
      "_rev": "1-eb84340e9061ff439f24e6ee56e5d8b1",
      "material": "metal",
      "name": "spoon"
    }

The value in the view for each items that is made from metal
should be the whole document.

## 1) create first a design document

    $ source resty
    $ resty http://localhost:5984/things-learn-couchdb -H "Content-Type: application/json"
    $ 

*Details*:

- "POST": Upload data. Within CouchDB POST is used to set values, including uploading documents, setting document values, and starting certain administration commands.


## map function

    function (doc) {
        if (doc.material == "metal") {
            emit(null, doc);
        }
    }


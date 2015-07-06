{
    "views": {
        "thingsMadeOfMetal": {
            "map": "function(doc) {
                if (doc.meterial == \"metal\") {
                    emit(null, doc);
                }
            }"
        }
    }
}

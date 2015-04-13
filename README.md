# About

Just some Elasticsearch tests.

# Browse

Latin texts added by `es_bulk_import.py`. Data viewable at [http://104.131.178.18:9200/texts/text/1?pretty=true].

All data on one file:
```
http://104.131.178.18:9200/texts/text/1?pretty=true
```

Get all data in `texts` index:
```
curl -XGET 'http://104.131.178.18:9200/texts/_search?pretty=true' -d '
{
    "query" : {
        "matchAll" : {}
    }
}'
```

Text query:
```
curl -XGET 'http://104.131.178.18:9200/texts/text/_search?pretty=true' -d '
{
    "query" : {
        "match" : {
            "text" : "spolia"
        }
    }
}'
```

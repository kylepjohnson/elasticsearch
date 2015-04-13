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

or:

```
curl -XGET http://104.131.178.18:9200/texts/text/_search
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

or:

```
curl -XGET http://104.131.178.18:9200/texts/text/_search?q=author:abelard
```

Ranked search results:
```
curl -XGET 'http://104.131.178.18:9200/texts/text/_search?pretty=true' -d '
{
    "query" : {
        "filtered" : {
            "query" : {
                "match" : {
                    "author" : "Caesar" 
                }
            }
        }
    }
}'
```

… responds with:

```
{
"took": 33,
"timed_out": false,
"_shards": {
"total": 5,
"successful": 5,
"failed": 0
},
"hits": {
"total": 14,
"max_score": 5.7564597,
"hits": [
{
"_index": "texts",
"_type": "text",
"_id": "413",
"_score": 5.7564597,
"_source": {
"text": "b'C. IVLI CAESARIS COMMENTARIORVM …
```

A phrase search:

```curl -XGET 'http://104.131.178.18:9200/texts/text/_search?pretty=true' -d '
{
    "query" : {
        "match_phrase" : {
            "text" : "arma virumque cano"
        }
    }
}'
```

Highlight query:

```
curl -XGET 'http://104.131.178.18:9200/texts/text/_search?pretty=true' -d '
{
    "query" : {
        "match_phrase" : {
            "text" : "arma virumque cano"
        }
    },
    "highlight": {
        "fields" : {
            "text" : {}
        }
    }
}'
```

… this returns matched search terms in `<em>` tags:

```
        "text" : [ " primo Eneidorum dicit 
<em>Arma</em>
<em>virumque</em>
<em>cano</em> \\n-; alio modo secundum quod fabricata profertur vel ab" ]
```

[Highlighting docs](http://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html).

See next: [Significant terms aggregation](https://www.elastic.co/blog/significant-terms-aggregation/).

Document count:
```
curl -XGET '104.131.178.18:9200/_count?pretty' -d '
{
    "query": {
        "match_all": {}
    }
}'
```


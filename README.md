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

… this returns matched search terms in `<em>` tags. ([Highlighting docs](http://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html).)

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

# Installation

## Mac

Using brew ([simple instructions here](http://stackoverflow.com/a/22855889)):

```
brew update
brew install elasticsearch
```

This responds with startup options:

```
To have launchd start elasticsearch at login:
    ln -sfv /usr/local/opt/elasticsearch/*.plist ~/Library/LaunchAgents
Then to load elasticsearch now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.elasticsearch.plist
Or, if you don't want/need launchctl, you can just run:
    elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml
```

Using the last of these commands, with Java 8 enabled:

```
export set JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home
elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml
```

Test running with: `curl localhost:9200`.


# Querying

Raw query example: localhost:9200/text/_search?q=200&size=5

or:

```
curl -XGET localhost:9200/text/_search -d '{
    "query" : {
        "term" : { "text": "200" }
    }
}'
```

On queries for strings (https://www.elastic.co/guide/en/elasticsearch/reference/1.x/query-dsl-query-string-query.html):


To install Kibana, download at <https://www.elastic.co/downloads/kibana> and follow installation instructions in the `README.txt`. For me, this was:

```
cd ~/Downloads/kibana-4.0.2-darwin-x64
./bin/kibana
```

Kibana will be available at <http://localhost:5601>.

Another alternative is the browser plugin (<https://github.com/OlegKunitsyn/elasticsearch-browser>). In my Mac I used: `sudo /usr/local/bin/plugin -install OlegKunitsyn/elasticsearch-browser` and then <http://localhost:9200/_plugin/browser/?database=text&table=tlg>. Seems broken, no response.

Another is: <https://github.com/polyfractal/elasticsearch-inquisitor>. `sudo /usr/local/bin/plugin -install polyfractal/elasticsearch-inquisitor`, <http://localhost:9200/_plugin/inquisitor/>. This more useable, but only for really for testing strucured queries in JSON.

ElasticHQ. 

sudo /usr/local/bin/plugin -install royrusso/elasticsearch-HQ

http://localhost:9200/_plugin/HQ/

Worth looking at this more.
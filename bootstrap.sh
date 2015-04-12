#!/usr/bin/env bash

# install basics
sudo apt-get update
sudo apt-get -y upgrade

# auto-select Java license
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update
sudo apt-get install -y oracle-java8-installer

# install logstash
cd /tmp
curl -O https://download.elastic.co/logstash/logstash/packages/debian/logstash_1.4.2-1-2c0f5a1_all.deb
sudo dpkg --install logstash_1.4.2-1-2c0f5a1_all.deb
sudo service logstash start

# install elasticsearch
curl -O https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.1.deb
sudo dpkg --install elasticsearch-1.5.1.deb
sudo service elasticsearch start

# install kibana
curl -O https://download.elastic.co/kibana/kibana/kibana-4.0.1-linux-x64.tar.gz
tar zxvf kibana-4.0.1-linux-x64.tar.gz
sudo mv kibana-4.0.1-linux-x64 /opt/kibana
cd /opt/kibana
# maybe: Open config/kibana.yml in an editor; set the elasticsearch_url to point at your Elasticsearch instance
./bin/kibana
# curl http://yourhost.com:5601

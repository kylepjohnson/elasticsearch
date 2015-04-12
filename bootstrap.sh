#!/usr/bin/env bash

# install basics
sudo apt-get update
sudo apt-get -y upgrade
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer

# install logstash
curl -O https://download.elastic.co/logstash/logstash/packages/debian/logstash_1.4.2-1-2c0f5a1_all.deb
sudo dpkg --install logstash_1.4.2-1-2c0f5a1_all.deb
# start?

# install elasticsearch
curl -O https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.1.deb
sudo dpkg --install elasticsearch-1.5.1.deb 
sudo service elasticsearch start

# install kibana
curl -O https://download.elastic.co/kibana/kibana/kibana-4.0.1-linux-x64.tar.gz
sudo dpkg --install kibana-4.0.1-linux-x64.tar.gz
# start?

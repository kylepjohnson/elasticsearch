#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y upgrade
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get install oracle-java8-installer
sudo apt-get update
sudo apt-get install oracle-java8-installer
curl -O https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.1.deb
sudo dpkg --install elasticsearch-1.5.1.deb 
sudo service elasticsearch start


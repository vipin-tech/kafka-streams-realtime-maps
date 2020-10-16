# Tracking DublinBus in RealTime using Apache Kafka, Leaflet and Flask.

Apache Kafka is the open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java.
Apache Kafka is based on the commit log, and it allows users to subscribe to it and publish the data to any number of systems or real time applications.
Monitoring end-to-end performance requires tracking metrics from brokers, consumers and producers, in addition to monitoring Zookeeper, which Kafka uses
for coordination among consumers.

This project involves the tracking of bus in realtime using coordinate data generated from buses which is published to the topic on the broker. The message is put
into respective topic which inturn can be divided into partitions to resolve memory and storage issues. The published data is taken up by a consumer or group of consumers to process the streaming data.
The bus location is visulaized using micro web framework called Flask and Leaflet, which is the opensource Javascript library used to build web applications. The coordinates are generated using GeoJSON. The bus location is plotted on the map
using Mapbox, which provides the online maps for websites and applications.
  
WebApp UI

![alt text](https://github.com/vipin-tech/kafka-streams-realtime-maps/blob/main/templates/bustrack.jpg)


*Above is the screenshot of the webapp which is to track Dublin buses in real time. I am tracking the bus routes 4 (Monkstown-Harristown) and 39a (UCD Belfield - Ongar)*


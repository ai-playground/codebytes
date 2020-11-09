Requirements:

1) Getting data from PWS
2) user query for weather in location
3) notification of any inclement weather



API
----
def send_data(api_key,pws_id,lat,lng,data)
def query(client_id,zipcode)

Scale Req:
----------

PWS_Data
A single PWS
freq:every 30 min
payloadsize:1KB
Total 48KB from every sensor

Number of PWS:500K
bandwidth = 500MB/sec
num_request = 500K

Reads
33M WAU =~5M DAU
assume reads are unformly spread
reads per sec = 5M/24*60*60 =5M/86k = 50 reads per sec

read:write
50:500K
1:30

DATA MODEL:
-----------
geo(index) | avg_temp| avg_humidity | ts(index) | ttl

HIGH LEVEL SKETCH:
-----------------
PWS->Kafka->ETL->writer->S3
                        ->db_loader->db

Client -> DNS->load balancer-> web server->loadbalancer->db

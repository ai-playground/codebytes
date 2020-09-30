API
----
def user(user_id)
def follow_friend(user_id, friend_id)
def upload_image(user_id, image, metadata)
def newsfeed(user_id)
def comment(user_id, image_id)
def like_dislike(user_id, image_id)


SCALE REQUIREMENTS
------------------
#
total users = 30 million
WAU = 30 million
DAU = 4 million
number of connections at peak = 4 million

## reads
data is getting read everyday = 4 million * 20 images per user * 1 MB
= 4*20* TB = 80 TB data is getting read every day

## writes
400k images are uploaded every day
each image is 1 MB
400 GB/sec of data is getting uploaded


Total size = 400 GB *8000 = 3200 TB = ~4 PB

DATA MODEL
----------
user
user_id | username | password | last_login | follows | followed_by

follower
user_id | followers_id

follows
user_id | follows_id



HIGH-LEVEL-SKETCH
-----------------

user

read -> load_balancer -> web_server -> api_server -> load_balancer ->db1/db2/db3

(available/not consistency)
write -> load_balancer -> web_server -> api_server -> load_balancer ->db1/db2/db3
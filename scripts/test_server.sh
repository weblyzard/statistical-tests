#!/usr//bin/env bash

# 
#server_url=$1
#username=$2
#password=$3
api_version=1.0
#echo 'sending to' $server_url/$api_version/
#token needs to be replaced every 8 hours
test_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJwZXJtaXNzaW9ucyI6WyJjb20ud2VibHl6YXJkLmFwaS5kb2N1bWVudC5yZXRyaWV2ZTp3ZWJseXphcmQuY29tL3Rlc3QiLCJjb20ud2VibHl6YXJkLmFwaS5kb2N1bWVudC5hZGQ6d2VibHl6YXJkLmNvbS90ZXN0IiwiY29tLndlYmx5emFyZC5hcGkuZG9jdW1lbnQudXBkYXRlOndlYmx5emFyZC5jb20vdGVzdCIsImNvbS53ZWJseXphcmQuYXBpLmRvY3VtZW50LmRlbGV0ZTp3ZWJseXphcmQuY29tL3Rlc3QiLCJjb20ud2VibHl6YXJkLmFwaS5hbm5vdGF0ZTpzZW50aW1lbnQiLCJjb20ud2VibHl6YXJkLmFwaS5hbm5vdGF0ZTpuYW1lZGVudGl0aWVzIl0sImlhdCI6MTQ1NTExNDYwOCwiZXhwIjoxNDU1MTUzMDA4LCJhdWQiOlsiY29tLndlYmx5emFyZC5hcGkiXSwiaXNzIjoiY29tLndlYmx5emFyZC5hcGkiLCJzdWIiOiJ0ZXN0QHdlYmx5emFyZCJ9.QN3lKG6LvIHz0tF91VGbKyofbbNGgfgFbM0oQM2wwcqkT0LzXOvsu0WVUklu8_htha07kyxJUaaqiTgUvB-MoA=='

auth="Authorization: Bearer "$test_token

#curl -X GET $server_url/$api_version/status
#VALID POSTS
curl -H "$auth" -H "Content-Type: application/json" -X POST --data @valid_observation.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans2
curl -H "$auth" -H "Content-Type: application/json" -X POST --data @valid_observation2.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans
curl -H "$auth" -H "Content-Type: application/json" -X POST --data @valid_observation3.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans2

#INVALID POSTS
curl -H "$auth" -H "Content-Type: application/json" -X POST --data @invalid_observation.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans2
curl -H "$auth" -H "Content-Type: application/json" -X POST --data @invalid_observation2.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans2

#PUT
curl -H "$auth" -H "Content-Type: application/json" -X PUT --data @update_observation.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans/1

#GET
curl -H "$auth" -X GET https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans2/1

#DELETE
curl  -H "$auth" -X DELETE https://api.weblyzard.com/0.2/observations/weblyzard.com/test/esairtrans2/1


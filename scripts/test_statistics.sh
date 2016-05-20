#!/usr//bin/env bash

# 
server_url=$1
api_version=1.0
echo 'sending to' $server_url/$api_version/

curl -X GET $server_url/$api_version/status

# validations
#curl -H "Content-Type: application/json" -X POST --data @valid_observation.json $server_url/$api_version/checkObservationResource
#curl -H "Content-Type: application/json" -X POST --data @invalid_observation.json $server_url/$api_version/checkObservationResource

# add document
curl -H "Content-Type: application/json" -X POST --data @valid_observation.json $server_url/$api_version/observations/statistics/esairtrans2
curl -H "Content-Type: application/json" -X POST --data @valid_observation2.json $server_url/$api_version/observations/statistics/esairtrans
curl -H "Content-Type: application/json" -X POST --data @valid_observation3.json $server_url/$api_version/observations/statistics/esairtrans2
curl -H "Content-Type: application/json" -X POST --data @invalid_observation2.json $server_url/$api_version/observations/statistics/esairtrans2


# update document
#curl -H "Content-Type: application/json" -X PUT --data @update_observation.json $server_url/$api_version/observations/statistics/esairtrans/1

# retrieve document
curl -X GET $server_url/$api_version/observations/statistics/esairtrans2/1

# delete document
curl -X DELETE $server_url/$api_version/observations/statistics/esairtrans2/1

# delete indicator
#curl -X DELETE $server_url/$api_version/observations/statistics/esairtrans2
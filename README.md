# statistical-tests

To obtain a token for the user, do a

    curl -u test@weblyzard:demo https://api.weblyzard.com/0.2/token

With that token, the following operations are possible

ADD:

    curl -H 'Authorization: Bearer <token>' -d @observation.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/<indicator-id>

RETRIEVE:

    curl -H 'Authorization: Bearer <token>' https://api.weblyzard.com/0.2/observations/weblyzard.com/test/<indicator-id>/<observation-id>

UPDATE:

    curl -H 'Authorization: Bearer <token>' -d @observation.json https://api.weblyzard.com/0.2/observations/weblyzard.com/test/<indicator-id>/<observation-id>

DELETE:

    curl -H 'Authorization: Bearer <token>' -XDELETE https://api.weblyzard.com/0.2/observations/weblyzard.com/test/<indicator-id>/<observation-id>
    
## TESTS

In order to test the API it is enough to simply run the same commands that are included in the API together with a set of files that are known to follow / not follow the specification.

To run the tests simply run the following bash scripts: [test_server](https://github.com/weblyzard/statistical-tests/blob/master/scripts/test_server.sh)

Do not forget to change the permission of the script previously:
        
    sudo chmod u+x pathToScript/test_server.sh

It contains the following tests:

#### POST validation 

3 examples (valid_observation.json, valid_observation2.json, valid_observation3.json) are availalbe due to the fact that one can upload JSON files that contain observations with different fields. The webLyzard API defines a set of required and optional fields.

The first example (valid_observation.json) only contains required fields: *id*, *uri*, *added_date* (indexing date), *date* (observation/document date), *indicator_id*, *indicator_name*, *value*).

Some examples of optional fields are presented in the next example (valid_observation2.json): target_country, target_type, target_location, etc.

The last example is somewhat similar to the first example.

All these examples are expected to pass!

#### invalid POST 

2 examples (invalid_observation.json, invalid_observation2.json) are available in order to highlight various types of errors.

In the first example a fictional field (field that does not exists in the required or optional sets of fields described in the webLyzard API) named *testerror* is defined which will make this test fail.

The second example is expected to fail, as the *id* of the observation is missing.

#### PUT test 

The current example (update_observation.json) corresponds to an UPDATE statement.

The expected output is a value of 2000 instead of 1000 for the first observation (id=1).

#### GET test 

This test simply returns the data for a single observation.

#### DELETE test

This test simply deletes the data for a single observation.

## WHAT TO DO IF ALL TESTS FAIL

Please let us know. This generally happens when the deployed backend and frontend versions do not correspond. Generally all tests are changed to correspond to a certain version of the backend API.

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

In order to test the API it is enough to simply run the same commands that are included in the API together with a set of files that are known to respect / not respect the specification.

To run the tests simply run the following bash scripts: [test_server](https://github.com/weblyzard/statistical-tests/blob/master/scripts/test_server.sh)

It contains the following tests:

1) POST validation - 3 examples (valid_observation.json, valid_observation2.json, valid_observation3.json)

2) invalid POST - 1 example (invalid_observation2.json)

3) PUT test - 1 example (update_observation.json)

4) GET test - 1 example

5) DELETE test - 1 example


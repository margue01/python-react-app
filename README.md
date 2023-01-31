# Python and React App

This project implements an API and a basic User Interface to manage a list of users.


## Local Run

### Build

    $ pip install -r requirements.txt
	$ cd ui-people
    $ yarn install
    $ yarn build
    $ cd ..

``Python >= 3.6`` is required.

Tested with Node 12.

### Execution

    $ ./run_local.sh

## Run and build with Docker and nginx to serve static files

    $ make build
    $ make run

>**Warning**
> The yarn build is slow.

## API

### Healthcheck
```
GET http://localhost:8003/app/healthcheck
```
Response
```
{
    "status": "ok"
}
```

### Version
```
GET http://localhost:8003/app/version
```
Response
```
{
    "version": "0.0.1"
}
```

### Get all the people
```
GET http://localhost:8003/app/people
```

Query parameters:
- `sort_by` to sort the records. Valid values are `email`, `name`, `age`, `balance`
- `limit` to limit the number of records in the response.
- `name`: search people with `name` string included in the name field.

### Create a person
```
POST http://localhost:8003/app/people
```
Body:
```
{
	"address": "Dub",
	"age": 18,
	"balance": 10.0,
	"email": "m@g.com",
	"flag": false,
	"name": "John"
}
```
Response
```
{
    "created": "ok"
}
```
Example:
```
curl -X POST -H 'Content-Type: application/json' \
    -d '{"email":"m@g.com","flag":false,"name": "John","balance": 10.0,"address": "Dub","age": 18}' \
    http://127.0.0.1:8003/app/people
```
### Update the person Flag
```
PUT http://localhost:8003/app/people/{person_id}
```
Body:
```
{
	"flag": true
}
```

### Delete a person
```
POST http://localhost:8003/app/people
```

## Tests

    $ pytest tests/

## UI

The User Interface can be reached on http://localhost:8003/index.html

## Improvements
- Add unit tests.
- Add UI to create a person.
- Add spinner instead of description when a request was sent.
- Update frontend packages.

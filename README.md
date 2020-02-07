# Python and React App

This project implemets an API and a basic User Interface to manage a list of users.


## Installation

    $ pip install -e requirements.txt
    $ yarn install
    $ yarn build
    $ cd ..

``Python 3.6`` is required.


## Execution

    $ ./run_local.sh

### API

#### Get all the people
```
GET http://localhost:8003/app/people
```
Response
```
{
    "created": "ok"
}
```

#### Create a person
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
#### Update the person Flag
```
PUT http://localhost:8003/app/people/{person_id}
```
Body:
```
{
	"enable": true
}
```

#### Delete a person
```
POST http://localhost:8003/app/people
```

### UI

The User Interface can be reached on http://localhost:8003/index.html

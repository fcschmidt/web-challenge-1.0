# Web Challenge 1.0

Web Challenge 1.0 - RestFull API with Pyramid


## RESTful API Resources
API available in: [https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes](https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes)


#### Endpoints: HTTP method and URI list
**HTTP method**|**URI path**|**Description**
:--|:--|:--
GET|/quotes|Retrieves information all quotes
GET|/quotes/{quote_number}|Retrieves information detail from a quote



**GET /quotes**
```json
{
  "quotes": [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "..."
  ]
}
```


**GET /quotes/0**
```json
{
  "quote": "Beautiful is better than ugly."
}
```


## Challenge Description
Create an application using the framework [pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/), for API use.


Create a python package in the project to perform API queries containing the following functions:

- **get_quotes( ):** Query API and returns python dictionary containing the quotes.
- **get_quotes(quote_number):** Query API and return the corresponding quote.


#### Routers

- `/`:  Features simple HTML page containing title "Challenge Web 1.0"

- `/quotes:`: Show page containing the sentences in bullet points all the quotes returned by the API.

- `/quotes/<quote_number>`: Display page containing the quote returned by the API corresponding to the `<quote_number>`.

- `/quotes/random/`: Display page containing a random quote. Display the number of the generate quote and its corresponding quote.

#### Session creation and logging
Using the framework session mechanism create a unique identifier for all accesses made in the application originated from the same browser.

#### Record accesses to a database
Using SQLAlchemy + sqlite create template / templates to register:

- Session identifier for each query register.
- Date, time and page accessed within a session.

#### Create RESTful endpoints for viewing sessions/queries.



## Quotes Application

Application developed using version 3.5 of the [Python](http://), using the [pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/) framework.


#### Preparing the environment

Configuring the project and installing dependencies

**Download project via git clone:**

`$ git clone git@github.com:fcschmidt/web-challenge-1.0.git`

**Accessing the application folder:**

`$ cd web-challenge-1.0/quotes_app`

**Installing and configuring the project:**

`$ python3 ./setup.py develop`

**Create a Database:**

`$ initialize_quotes_app_db development.ini`

#### Run

`$ pserve development.ini --reload`

View application in [http://localhost:6543/](http://localhost:6543/).


#### Views

**View**|**URIs**|**Description**
:--|:--|:--
Home|localhost:6543|Page displays the name of the challenge
Quotes|localhost:6543/quotes|Page displays all quotes
Quote|localhost:6543/quotes/{quote_number}|Page displays a quote
Random|localhost:6543/quotes/random/|Displays and generates random quotes


### RESTful API Resources
API for visualization and query via http of the saved information generated of each session accessed.

#### Endpoints: HTTP method and URI list

**HTTP method**|**URI path**|**Description**
:--|:--|:--
GET|/api/sessions|Retrieves information all sessions
GET|/api/sessions/{id}|Retrieves information detail from a session


#### Requests
To make requests via the terminal use the [curl](https://curl.haxx.se/).

In Python scripts use [requests](http://docs.python-requests.org/en/master/).
Or, use applications to test example: [Postman](https://www.getpostman.com/) and
[Insomnia](https://insomnia.rest/?utm_content=bufferd23bb&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer).

**List all resources**

`$ curl http://localhost:6543/api/sessions`

```json
[
    {
        "date": "2018-01-17",
        "session_uid": "5a5ebf6538af6f3eb0281eec38e35816bd386fdc",
        "id": 1,
        "time": "01:21:39.318109",
        "session_url": "http://localhost:6543/"
    },
    {
        "date": "2018-01-17",
        "session_uid": "5a5ebf6538af6f3eb0281eec38e35816bd386fdc",
        "id": 2,
        "time": "01:21:39.318109",
        "session_url": "http://localhost:6543/quotes"
    },
    "{...}"
]
```

**Resources Detail**

`curl http://localhost:6543/api/sessions/1`

```json
{
  "date":"2018-0117",
  "session_uid":"5a5ebf6538af6f3eb0281eec38e35816bd386fdc",
  "id":1,
  "time":"01:21:39.318109",
  "session_url":"http://localhost:6543/"
}
```

<!--#### Tests

-->


## License
[MIT License](https://opensource.org/licenses/MIT) © Fábio Schmidt

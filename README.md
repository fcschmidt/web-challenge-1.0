# Web Challenge 1.0
Web Challenge 1.0 - RestFull API with Pyramid


## RESTful API Resources
API dispónivel em: [https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes](https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes)


#### Endpoins: HTTP method and URI list
**HTTP method**|**URI path**|**Description**
:--|:--|:--
GET|/quotes|Retrieves cluster information.
GET|/quotes/quote_number|Retrieves cluster details.


- - -


**GET /quotes**
```json
{
  "quotes": [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    ...
  ]
}
```


- - -


**GET /quotes/0**
```json
{
  "quote": "Beautiful is better than ugly."
}
```


## Challenge Description
Criar uma aplicação utilizando o framework [pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/), para uso da API.


Criar um pacote python no projeto para realizar consultas à API contendo as seguintes funções:

- **get_quotes( ):** consulta API e retorna dicionário python contendo os quotes.
- **get_quotes(quote_number):** Consulta API e retorna o quote correspondente.



#### Routers

- `/`:  Apresenta página HTML simples contendo título "Desafio Web 1.0"

- `/quotes:`: Apresenta página contendo as frases em bullet points todos os quotes retornados pela API.

- `/quotes/<quote_number>`: Apresentar página contendo o quote retornado pela API correspondente ao `<quote_number>`.

- `/quotes/random`: Apresentar página contendo um quote randômico. Exibir o quote_number sorteado e o quote correspondente.




## Quotes Application
Inside that directory, it will generate the initial project structure and install the transitive dependencies:
```text
web-challenge-1.0/
├── LICENSE
├── quotes_api
│   ├── CHANGES.txt
│   ├── development.ini
│   ├── entrypoint.sh
│   ├── lib
│   │   ├── consumer_api.py
│   │   └── __init__.py
│   ├── MANIFEST.in
│   ├── production.ini
│   ├── pytest.ini
│   ├── quotes_api
│   │   ├── __init__.py
│   │   ├── templates
│   │   │   ├── index.jinja2
│   │   │   ├── layout.jinja2
│   │   │   ├── quote.jinja2
│   │   │   ├── quotes.jinja2
│   │   │   └── random.jinja2
│   │   ├── tests.py
│   │   └── views.py
│   ├── README.txt
│   └── setup.py
└── README.md
```

## Endpoints

**HTTP method**|**URI path**|**Description**
:--|:--|:--

## License
[MIT License](https://opensource.org/licenses/MIT) © Fábio Schmidt

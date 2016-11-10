# Flask Scrapy Test

## Setup

1. Fork/Clone
1. Create and activate a virtualenv
1. Install dependencies

## Run

```sh
$ python app.py
```

Then send a POST request in a new terminal window:

```sh
$ http POST http://localhost:5000/data spider=dmoz url=http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
```

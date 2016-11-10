# Flask Scrapy Test

## Setup

1. Fork/Clone
1. Create and activate a virtualenv
1. Install dependencies

## Run

```sh
$ python app.py
```

### POST

URL:

```
http://localhost:5000/data
```

Payload:

```json
{
	"spider": "spider_name",
	"url": "spider_url"
}
```

Example:


```sh
$ http POST http://localhost:5000/data spider=dmoz url=http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
```

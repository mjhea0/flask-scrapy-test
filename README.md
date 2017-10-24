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

## Pipelines

Want to add data to a database? Add a [Item Pipeline](https://doc.scrapy.org/en/1.2/topics/item-pipeline.html).

First, update the `ITEM_PIPELINES` in the spider:

```python
custom_settings = {
    'ITEM_PIPELINES': {
        'pipelines.NewPipeline': 500
    }
}
```

Then add the new class to *pipelines.py*:

```python
class NewPipeline(object):

    def process_item(self, item, spider):
	# add code to insert date into db
        return item
```

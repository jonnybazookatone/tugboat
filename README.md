[![Build Status](https://travis-ci.org/adsabs/tugboat.svg?branch=master)](https://travis-ci.org/adsabs/tugboat)
[![Coverage Status](https://coveralls.io/repos/github/adsabs/tugboat/badge.svg?branch=master)](https://coveralls.io/github/adsabs/tugboat?branch=master)
# Tugboat

Tugboat proxy, integration tools to use alongside harbour-service

## usage
You can test the behaviour by visiting `localhost:8000/index.html`. Fill in a list of bibcodes, and press go. This should redirect you to ADS Bumblebee, with the relevant bibcodes.

From the front end you just want to do the equivalent to this curl:

```bash
curl -X POST 'http://localhost:8000/redirect --data '["bib1", "bib2", "bib3", ...., "bibN"]'
# returns
{'redirect': 'https://ui.adsabs.harvard.edu/#search/q=*%3A*&__qid=945gfd9gfda9d'}, 200
```

You then redirect to the returning URL

## development

```bash
pip install virtualenvwrapper
mkvirtualenv tug
workon tug
pip install -r requirements.txt
nosetests tugboat/tests/
```

## deployment

Manually build
```bash
$ more build.sh
#!/bin/bash

docker stop tuboat
docker rm tugboat
docker build --tag adsabs/tugboat:$1 . # skip this if it exists on hub.docker.com
docker run -d --name tugboat -p 5000:80 -e API_DEV_KEY=$2 adsabs/tugboat:$1

# Check it works
curl localhost:5000
```

You need to make sure the API dev key you use is the one for tugboat, or you will be limited to the limits given to normal users (5000/24hr).

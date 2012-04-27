Localize.py
===========

Ultra simple and useless geoip service... this time in python


Installation
------------

- Install [the bottle microframework](http://bottlepy.org/)

        $ sudo pip install bottle

- Install the GeoIP python api

        $ wget http://www.maxmind.com/download/geoip/api/python/GeoIP-Python-1.2.4.tar.gz
        $ tar xvzf GeoIP-Python-1.2.4.tar.gz && cd GeoIP-Python-1.2.4
        $ python setup.py build && sudo setup.py install

- Install the MaxMind-s GeoIP database

        $ cd data && wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
        $ gunzip GeoLiteCity.dat.gz && cd ..

- Start the server: `python localize/app.py`


Try it
------

You can test it with a browser or with curl

    $ curl -i http://localhost:8080/74.125.230.223

The server will response a 200 with a json

    HTTP/1.0 200 OK
    Date: Mon, 16 Apr 2012 10:27:13 GMT
    Server: WSGIServer/0.1 Python/2.6.1
    Content-Length: 329
    Content-Type: application/json

    {
        "country_code":"US",
        "country_code3":"USA",
        "country_name":"United States",
        "region":"CA",
        "city":"Mountain View",
        "postal_code":"94043",
        "latitude":37.4192008972168,
        "longitude":-122.05740356445312,
        "metro_code":807,
        "dma_code":807,
        "area_code":650,
        "continent_code":"NA"
    }

In case the given IP does not find a localization, the server will response a 404

    $ curl -i http://localhost:8080/127.0.0.1

    HTTP/1.0 404 Not Found
    Date: Mon, 16 Apr 2012 10:25:06 GMT
    Server: WSGIServer/0.1 Python/2.6.1
    Content-Length: 54
    Content-Type: application/json; charset=utf8

    {"message":"No localization found."}

Finaly, a last case is provided if you mispealed the IP in the URI, by send us a 400

    $ curl -i  http://localhost:8080/127.0.0

    HTTP/1.0 400 Bad Request
    Date: Mon, 16 Apr 2012 10:24:38 GMT
    Server: WSGIServer/0.1 Python/2.6.1
    Content-Length: 63
    Content-Type: application/json; charset=utf8

    {"message":"No IP address found in the URI."}

License
-------

(The MIT License)

Copyright (c) 2012 Bertrand Tornil <bertrand.tornil@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This product includes GeoLite data created by MaxMind, available from http://maxmind.com/
from bottle import Bottle, run, response
import logging
import json
import pygeoip


logging.basicConfig(level=logging.DEBUG)
gi = pygeoip.GeoIP("./data/GeoLiteCity.dat")
app = Bottle()

error_statuses = {
    400: 'Bad request: must be a /x.y.z.t form.',
    404: 'No localization found.'
}


def get_message(status):
    return error_statuses[status]


@app.route('/<ip:re:(\d{1,3}\.){3}\d{1,3}>')
def geolocalize(ip='127.0.0.1'):

    result = gi.record_by_addr(ip)

    if result is None:
        response.status = 404
        response.content_type = 'application/json; charset=utf8'

        return json.dumps({
            'message': get_message(404)
        })

    else:
        return result


@app.error(404)
def badRequest(error):
    response.status = 400
    response.content_type = 'application/json; charset=utf8'

    return json.dumps({
        'message': get_message(400)
    })


if __name__ == "__main__":
    try:
        run(app, host='0.0.0.0', port=8080)
    except Exception, e:
        raise

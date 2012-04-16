from bottle import run, route, response, error
import logging
import re
import json
import GeoIP

class PyLocalize:

    def __init__(self, geoip):
        logging.basicConfig(level=logging.DEBUG)
        self.geoip = geoip

    @route('/:ip')
    def geolocalize(ip='127.0.0.1'):

         # sanitize
        if (re.match('(?:\d{1,3}\.){3}\d{1,3}', ip) is None) :
            response.status = 400
            response.content_type = 'application/json; charset=utf8'

            return json.dumps({
                'status': '400',
                'message': 'No IP address found in the URI.'
            })
        else :
            result = gi.record_by_addr(ip)

            if result is None:
                response.status = 404
                response.content_type = 'application/json; charset=utf8'

                return json.dumps({
                    'status': '404',
                    'message': 'No localization found.'
                })

            else:
                # we must decode / encode some text fields
                result['city'] = result['city'].decode('iso-8859-15')
                result['region_name'] = result['region_name'].decode('iso-8859-15')
                logging.debug(result)
                return result


    @error(404)
    def error404(error):
        response.status = 404
        response.content_type = 'application/json; charset=utf8'

        return json.dumps({
            'status': '404',
            'message': 'Bad request: must be a /x.y.z.t form.'
        })




if __name__ == "__main__":

    try:
        gi = GeoIP.open("./data/GeoLiteCity.dat",GeoIP.GEOIP_STANDARD)
        pyLocalize = PyLocalize(gi)
        run(host='0.0.0.0', port=8080)
    except Exception, e:
        raise

from collections import defaultdict

from pygeoip import (
    GeoIP,
    MMAP_CACHE,
)


def configure_geoip():

    gi = GeoIP("./data/GeoLiteCity.dat", flags=MMAP_CACHE)
    return gi


def main():

    gi = configure_geoip()

    coords = defaultdict(int)

    for ip1 in range(255):
        print ip1
        for ip2 in range(255):
            for ip3 in range(10):
                ip = '{}.{}.{}.0'.format(ip1, ip2, ip3)
                result = gi.record_by_addr(ip)

                if result is not None:
                    latitude = result['latitude']
                    longitude = result['longitude']
                    coords['{};{}'.format(latitude, longitude)] = coords['{};{}'.format(latitude, longitude)] + 1

    with open('db_coords.txt', 'w') as f:
        for coord, count in coords.iteritems():
            f.write('{};{}\n'.format(coord, count))

if __name__ == '__main__':
    main()

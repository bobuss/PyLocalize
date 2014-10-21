from pygeoip import (
    GeoIP,
    MMAP_CACHE,
)
import matplotlib.pyplot as pl


def configure_map():

    from mpl_toolkits.basemap import Basemap
    m = Basemap()
    m.drawcoastlines(linewidth=0.1)
    m.drawcountries(linewidth=0.1)

    return m


def configure_geoip():

    gi = GeoIP("./data/GeoLiteCity.dat", flags=MMAP_CACHE)
    return gi


def main():

    gi = configure_geoip()

    m = configure_map()

    for ip1 in range(255):
        for ip2 in range(255):
            for ip3 in range(2):
                ip = '{}.{}.{}.0'.format(ip1, ip2, ip3)
                result = gi.record_by_addr(ip)

                if result is not None:
                    print ip
                    latitude = result['latitude']
                    longitude = result['longitude']

                    if m is not None:
                        #Convert latitude and longitude to coordinates X and Y
                        x, y = m(longitude, latitude)

                        #Plot the points on the map
                        m.plot(x, y, 'r,')

    if m is not None:
        pl.savefig('test', dpi=300)


if __name__ == '__main__':
    main()

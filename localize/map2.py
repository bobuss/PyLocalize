import matplotlib.pyplot as pl


def configure_map():

    from mpl_toolkits.basemap import Basemap
    m = Basemap()
    m.drawcoastlines(linewidth=0.1)
    m.drawcountries(linewidth=0.1)

    return m

def main():

    m = configure_map()

    with open('db_coords.txt') as f:

        data = f.readline().split(";")

        while data is not None:

            try:
                latitude = float(data[0])
                longitude = float(data[1])
                count = int(data[2])

                #Convert latitude and longitude to coordinates X and Y
                x, y = m(longitude, latitude)

                #Plot the points on the map
                m.plot(x, y, 'r,')
                data = f.readline().split(";")

            except ValueError:
                data = None

        pl.savefig('test2', dpi=300)


if __name__ == '__main__':
    main()

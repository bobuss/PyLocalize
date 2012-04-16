import unittest
import GeoIP
from bottle import run
from localize.app import PyLocalize

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.gi = GeoIP.open("./data/GeoLiteCity.dat",GeoIP.GEOIP_STANDARD)
        self.pyLocalize = PyLocalize(self.gi)

    def testGeoIp(self):
        self.pyLocalize.geolocalize('78.212.123.32')
        pass


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestApplication))

if __name__ == "__main__":
    unittest.main()

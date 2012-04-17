import unittest
import localize.app as app


class TestApplication(unittest.TestCase):

    def setUp(self):
        #self.app = Bottle()
        pass

    def testDefault(self):
        response = app.geolocalize()
        self.assertEqual(response, '{"message": "%s"}' % app.get_message(404))

    def test404(self):
        response = app.geolocalize(ip='0.0.0.0')
        self.assertEqual(response, '{"message": "%s"}' % app.get_message(404))

    def test400(self):
        response = app.badRequest(None)
        self.assertEqual(response, '{"message": "%s"}' % app.get_message(400))



suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestApplication))

if __name__ == "__main__":
    unittest.main()

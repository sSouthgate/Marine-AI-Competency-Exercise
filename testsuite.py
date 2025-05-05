import unittest
from checksum import checksum
from pos_converter import position_convert
from speed_converter import speed_convert


class TestChecksum(unittest.TestCase):

    def testValidChecksum(self):

        # This is a know valid RMC message
        testRMCdata = "$GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"
        cksum = checksum(testRMCdata)
        self.assertTrue(cksum.checksumValidate(),
                        "Checksum should confirm with RMC message")

    def testInvalidChecksum(self):

        # This is a know invalid RMC message - the checksum value has been changed
        testRMCdata = "$GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*FF"
        cksum = checksum(testRMCdata)
        self.assertFalse(cksum.checksumValidate(),
                         "Checksum should not match with RMC message")

    def testChecksumResult(self):

        testRMCdata = "$GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"
        cksum = checksum(testRMCdata)
        nmeaData, rmcCksum, calc_cksum = cksum.checksumResult()
        self.assertTrue(nmeaData.startswith("GPRMC"),
                        "RMC Message should be parsed correctly")
        self.assertEqual(rmcCksum.lower(), calc_cksum.lower(
        ), "The RMC message checksum and calculated checksum should match")

    def testValidChecksumWithoutDollar(self):

        # Known valid RMC message without "$"
        testRMCdata = "GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"
        cksum = checksum(testRMCdata)
        self.assertTrue(cksum.checksumValidate(
        ), "Checksum should confirm with RMC message even without $")


class TestPositionConvert(unittest.TestCase):

    def testConvLatNorth(self):

        testRMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
        pos = position_convert(testRMCdata)
        lat = pos.convLat()
        # expected_lat = 50 + 21/60 + ((0.5874 % 1) * 60) / 3600

        self.assertAlmostEqual(lat, 50.3598, places=4)

    def testConvLatSouth(self):

        testRMCdata = "$GPRMC,112000.000,A,5021.5874,S,00408.9009,W,9.09,309.61,201022,,,A*74"
        pos = position_convert(testRMCdata)
        lat = pos.convLat()
        # expected_lat = (50 + 21/60 + ((0.5874 % 1) * 60) / 3600) *-1

        # S will meean we should have negative number
        self.assertAlmostEqual(lat, -50.3598, places=4)

    def testConvLngWest(self):

        testRMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
        pos = position_convert(testRMCdata)
        lng = pos.convLng()
        # expected_lat = (4 + 8/60 + ((0.9009 % 1) * 60) / 3600) *-1

        # W will mean we should have negative number
        self.assertAlmostEqual(lng, -4.1483, places=4)

    def testConvLngEast(self):

        testRMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,E,9.09,309.61,201022,,,A*74"
        pos = position_convert(testRMCdata)
        lng = pos.convLng()
        # expected_lat = 4 + 8/60 + ((0.9009 % 1) * 60) / 3600

        self.assertAlmostEqual(lng, 4.1483, places=4)

    def testconvPosition(self):

        testRMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
        pos = position_convert(testRMCdata)
        lat, lng = pos.convPosition()
        self.assertAlmostEqual(lat, 50.3598, places=4)
        self.assertAlmostEqual(lng, -4.1483, places=4)


class TestSpeedConvert(unittest.TestCase):

    def testKnotsToMps(self):
        testRMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
        speed = speed_convert(testRMCdata)
        expected_speed = round(9.09 * (1852 / 3600), 4)
        self.assertAlmostEqual(speed.knotsToMps(), expected_speed, places=4)

    def testGetCog(self):
        testRMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
        speed = speed_convert(testRMCdata)
        self.assertEqual(speed.getCog(), 309)

    def testZeroSpeed(self):
        testRMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,0.00,180.00,201022,,,A*74"
        speed = speed_convert(testRMCdata)
        self.assertEqual(speed.knotsToMps(), 0.0)


if __name__ == '__main__':
    unittest.main()

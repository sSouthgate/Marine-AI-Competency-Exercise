import unittest
from checksum import checksum
from pos_converter import position_convert

class TestChecksum(unittest.TestCase):

    def testValidChecksum(self):
        # This is a know valid RMC message
        testRMCdata = "$GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"
        cksum = checksum(testRMCdata)
        self.assertTrue(cksum.checksumValidate(), "Checksum should confirm with RMC message")

    def testInvalidChecksum(self):
        # This is a know invalid RMC message - the checksum value has been changed
        testRMCdata = "$GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*FF"
        cksum = checksum(testRMCdata)
        self.assertTrue(cksum.checksumValidate(), "Checksum should not match with RMC message")

    def testChecksumResult(self):
        testRMCdata = "$GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"
        cksum = checksum(testRMCdata)
        nmeaData, rmcCksum, calc_cksum = cksum.checksumResult()
        self.assertTrue(nmeaData.startswith("GPRMC"), "RMC Message should be parsed correctly")
        self.assertEqual(rmcCksum.lower(), calc_cksum.lower(), "The RMC message checksum and calculated checksum should match")

    def testValidChecksumWithoutDollar(self):
        # Known valid RMC message without "$"
        testRMCdata = "GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"
        cksum = checksum(testRMCdata)
        self.assertTrue(cksum.checksumValidate(), "Checksum should confirm with RMC message even without $")


class TestPositionConvert(unittest.TestCase):

    def test_latitude_conversion_north(self):

        testRMCdata = "$GPRMC,053740.000,A,2503.6319,N,12136.0099,E,2.69,79.65,100106,,,A*53"
        pos = position_convert(testRMCdata)
        lat = pos.convLat()
        expected_lat = 50 + 21/60 + ((0.5874 % 1) * 60) / 3600
        self.assertAlmostEqual(lat, expected_lat, places=4)

    def 
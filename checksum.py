import re

class checksum:
    def __init__(self, RMCdata):
        if RMCdata.startswith("$"):
            self.__rmcData = RMCdata[1:]
        else:
            self.__rmcData = RMCdata

    def __parseNMEA(self):
        # Split string into 2 parts from the *
        self.__nmeaData, self.__cksum = re.split('\*', self.__rmcData)
        # Convert the checksum result into hex for verification
        self.__cksum = '0x' + self.__cksum

    def __checksumCalc(self):
        self.__calc_cksum = 0
        # Start XOR checksum calculation of the RMC Message
        data = self.__nmeaData
        for c in data:
            self.__calc_cksum ^= ord(c)
        return self.__calc_cksum

    def checksumResult(self):
        self.__parseNMEA()
        self.__checksumCalc()
        # Return tuple
        return (
            self.__nmeaData,
            self.__cksum,
            hex(self.__calc_cksum)
        )

    def checksumValidate(self):
        _, _, calc = self.checksumResult()
        # Lower function enssures no case sensitive issues occur for instance with 0x2b and 0x2B
        return self.__cksum.lower() == calc.lower()


if __name__ == "__main__":

    RMCmessage = "$GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"
    nmea = checksum(RMCmessage)
    print("parsed result:", nmea.checksumResult())
    print("checksum is:", nmea.checksumValidate())

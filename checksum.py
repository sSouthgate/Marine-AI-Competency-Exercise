import re


class checksum:
    def __init__(self, RMCdata):
        if RMCdata.startswith("$"):
            self.__RMCdata = RMCdata[1:]
        else:
            self.__RMCdata = RMCdata

    def __parseNMEA(self):
        # Split string into 2 parts from the *
        self.__NMEAdata, self.__cksum = re.split('\*', self.__RMCdata)
        # Convert the checksum result into hex for verification
        self.__cksum = '0x' + self.__cksum

    def __checksumCalc(self):
        self.__calc_cksum = 0
        # Start XOR checksum calculation of the RMC Message
        data = self.__NMEAdata
        for c in data:
            self.__calc_cksum ^= ord(c)
        return self.__calc_cksum

    def checksumResult(self):
        self.__parseNMEA()
        self.__checksumCalc()
        # Return tuple
        return (
            self.__NMEAdata,
            self.__cksum,
            hex(self.__calc_cksum)
        )

    def checksumValidate(self):
        _, _, calc = self.checksumResult()
        return self.__cksum == calc


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    nmea = checksum(RMCmessage)
    print("parsed result:", nmea.checksumResult())
    print("checksum is:", nmea.checksumValidate())

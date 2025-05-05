import re


class checksum:
    def __init__(self, RMCdata):
        if RMCdata.startswith("$"):
            self.RMCdata = RMCdata[1:]
        else:
            self.RMCdata = RMCdata

    def parseNMEA(self):
        # Split string into 2 parts from the *
        self.NMEAdata, self.cksum = re.split('\*', self.RMCdata)
        # Convert the checksum result into hex for verification
        self.cksum = '0x' + self.cksum

    def checksumCalc(self):
        self.calc_cksum = 0
        # Start XOR checksum calculation of the RMC Message
        data = self.NMEAdata
        for c in data:
            self.calc_cksum ^= ord(c)
        return self.calc_cksum

    def checksumResult(self):
        self.parseNMEA()
        self.checksumCalc()
        # Return tuple
        return (
            self.NMEAdata,
            self.cksum,
            hex(self.calc_cksum)
        )

    def checksumValidate(self):
        _, _, calc = self.checksumResult()
        return self.cksum == calc


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    nmea = checksum(RMCmessage)
    print("parsed result:", nmea.checksumResult())
    print("checksum is:", nmea.checksumValidate())

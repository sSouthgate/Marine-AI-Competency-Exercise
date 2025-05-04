import re

class checksum:
    def __init__(self, RMCdata):
        if RMCdata.startswith("$"):
            self.RMCdata = RMCdata[1:] 
        else:
            self.RMCdata = RMCdata

    def parseNMEA(self):
        #Split string into 2 part from the *
        self.NMEAdata, self.cksum = re.split('\*', self.RMCdata)
        #Convert the checsum result into hex for verification
        self.cksum = '0x' + self.cksum

        
    def calcChecksum(self):
        self.calc_cksum = 0
        # Start XOR checksum calculation of the RMC Message
        data = self.NMEAdata
        for c in data:
            self.calc_cksum ^= ord(c)

    def checksumResult(self):
        self.parseNMEA()
        self.calcChecksum()
        # Return tuple
        return (
            self.NMEAdata,
            self.cksum,
            hex(self.calc_cksum)
        )
    
    def validateChecksum(self):
        _, _, calc = self.checksumResult()
        return self.cksum == calc

if __name__== "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    nmea = checksum(RMCmessage)
    print("parsed result:", nmea.checksumResult())
    print("checksum is:", nmea.validateChecksum())
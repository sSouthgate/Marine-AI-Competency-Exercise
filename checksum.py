import re


class checksum:
    def __init__(self, RMCdata):
        if RMCdata.startswith("$"):
            self.__rmcData = RMCdata[1:]
        else:
            self.__rmcData = RMCdata

    def __parseNMEA(self):
        try:
            if "*" not in self.__rmcData:
                raise ValueError("NMEA Sentence does not contain '*' as delimter for checksum")
            
            __sentence = re.split("\*", self.__rmcData)

            if len(__sentence) !=2:
                raise ValueError("RMC Data error - expected single '*' seperating data and checksum")
            
            # Split string into 2 parts from the *
            self.__nmeaData, self.__cksum = __sentence
            # Convert the checksum result into hex for verification
            self.__cksum = "0x" + self.__cksum
        
        except Exception as e:
            raise ValueError("Error parsing NMEA: %s" %e)

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
        # lower() enssures no case sensitive issues occur for instance with 0x2b and 0x2B
        return self.__cksum.lower() == calc.lower()


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    nmea = checksum(RMCmessage)
    print("parsed result:", nmea.checksumResult())
    print("checksum is:", nmea.checksumValidate())

import math


class position_convert:
    """Input the RMS Data String to extract coodonates information
    """

    def __init__(self, RMCdata):

        self.__splitRMC = RMCdata.split(",")
        self.__RMClat = self.__splitRMC[3]
        self.__RMClng = self.__splitRMC[5]
        self.__RMClatIndicator = self.__splitRMC[4]
        self.__RMClngIndicator = self.__splitRMC[6]

    def __DMS(self, coord, coordIndicator, x):

        self.__dec = int(coord[:x])
        self.__min = int(coord[-2:])
        self.__sec = round(math.modf(float(coord))[0] * 60, 4)

        return (
            self.__dec,
            self.__min,
            self.__sec,
            coordIndicator
        )

    def __convDecDeg(self, coord, coordIndicator, x):

        self.__DMS(coord, coordIndicator, x)
        self.__decDeg = round(self.__dec + self.__min/60 + self.__sec, 4)
        if coordIndicator == "S" or coordIndicator == "W":
            self.__decDeg *= -1
        # return(self.__DMS(coord, coordIndicator, x),decDeg)
        return (self.__decDeg)

    def convLat(self):
        """Returns the latitude of the RMS Data in Decimal Degrees
        """
        return self.__convDecDeg(self.__RMClat, self.__RMClatIndicator, 2)

    def convLng(self):
        """Returns the longitude of the RMS Data in Decimal Degrees
        """
        return self.__convDecDeg(self.__RMClng, self.__RMClngIndicator, 3)

    def convposition(self):
        """Returns the latitude and longitude of the RMS Data as a double(Lat, Lng) in Decimal Degrees
        """
        return self.convLat(), self.convLng()


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    position = position_convert(RMCmessage)
    print("Dec. Degree Lat Coord:", position.convLat())
    print("Dec. Degree Lng Coord:", position.convLng())

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

        # get the first x characters for the degree value found in the coord variable
        self.__deg = int(coord[:x])

        # extract integer from coordonate part of the RMC Message
        self.degMin = math.modf(float(coord))[1]
        # from integer extract last 4 characters and turn back into int - this is the minutes
        self.__min = int(float(str(self.degMin)[-4:]))

        # extract the decimal value fround in the coord value and *60 to get the seconds
        self.__sec = round(math.modf(float(coord))[0] * 60, 4)

        # Print for test
        # print(self.__deg)
        # print(self.__min)
        # print(self.__sec)

        return (
            self.__deg,
            self.__min,
            self.__sec,
            coordIndicator
        )

    def __convDecDeg(self, coord, coordIndicator, x):

        self.__DMS(coord, coordIndicator, x)
        self.__decDeg = round(
            self.__deg + (self.__min/60) + (self.__sec/3600), 4)
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

    def convPosition(self):
        """Returns the latitude and longitude of the RMS Data as a double(Lat, Lng) in Decimal Degrees
        """
        return self.convLat(), self.convLng()


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    position = position_convert(RMCmessage)
    print("Dec. Degree Lat Coord:", position.convLat())
    print("Dec. Degree Lng Coord:", position.convLng())

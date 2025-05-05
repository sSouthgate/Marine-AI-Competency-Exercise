import math
import re


class position_convert:
    """Input the RMS Data String to extract coodonates information
    """

    def __init__(self, RMCdata):

        self.splitRMC = RMCdata.split(",")
        self.RMClat = self.splitRMC[3]
        self.RMClng = self.splitRMC[5]
        self.RMClatIndicator = self.splitRMC[4]
        self.RMClngIndicator = self.splitRMC[6]

    def DMS(self, coord, coordIndicator, x):

        self.dec = int(coord[:x])
        self.min = int(coord[-2:])
        self.sec = round(math.modf(float(coord))[0] * 60, 4)

        return (
            self.dec,
            self.min,
            self.sec,
            coordIndicator
        )

    def convDecDeg(self, coord, coordIndicator, x):

        self.DMS(coord, coordIndicator, x)
        decDeg = round(self.dec + self.min/60 + self.sec, 4)
        if coordIndicator == "S" or coordIndicator == "W":
            decDeg *= -1
        # return(self.DMS(coord, coordIndicator, x),decDeg)
        return (decDeg)

    def convLat(self):
        """Returns the latitude of the RMS Data in Decimal Degrees
        """
        return self.convDecDeg(self.RMClat, self.RMClatIndicator, 2)

    def convLng(self):
        """Returns the longitude of the RMS Data in Decimal Degrees
        """
        return self.convDecDeg(self.RMClng, self.RMClngIndicator, 3)

    def convposition(self):
        """Returns the latitude and longitude of the RMS Data as a double(Lat, Lng) in Decimal Degrees
        """
        return self.convLat(), self.convLng()


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    position = position_convert(RMCmessage)
    print("Dec. Degree Lat Coord:", position.convLat())
    print("Dec. Degree Lng Coord:", position.convLng())

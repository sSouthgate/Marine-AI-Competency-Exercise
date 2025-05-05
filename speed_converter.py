class speed_convert:
    def __init__(self, RMCdata):
        self.__splitRMC = RMCdata.split(",")
        self.__RMCspeed = float(self.__splitRMC[7])
        self.__cog = int(float(self.__splitRMC[8]))
        # 1 Knot = 1852 m/h | 1h = 3600s
        self.__knToMps = 1852/3600

    def knotsToMps(self):
        # Convert knots into m/s
        self.speed = round(self.__RMCspeed * self.__knToMps, 4)
        return (self.speed)

    def getCog(self):
        return (self.__cog)


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    speed = speed_convert(RMCmessage)
    print(speed.knotsToMps(), "m/s")
    print(speed.getCog())

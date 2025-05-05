class speed_convert:
    def __init__(self, RMCdata):
        self.splitRMC = RMCdata.split(",")
        self.RMCspeed = float(self.splitRMC[7])
        self.cog = int(float(self.splitRMC[8]))
        # 1 Knot = 1852 m/h
        self.knToMph = 1852
        # 1 m/h = 0.0002777778 m/s
        self.mphToMps = 0.0002777778

    def knotsToMps(self):
        # Convert knots into m/s
        self.speed = round(self.RMCspeed * self.knToMph * self.mphToMps, 2)
        return (self.speed)

    def getCog(self):
        return (self.cog)


if __name__ == "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    speed = speed_convert(RMCmessage)
    print(speed.knotsToMps(), "m/s")
    print(speed.getCog())

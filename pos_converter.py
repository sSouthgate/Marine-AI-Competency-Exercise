import math

class pos_convert:
    def __init__(self, RMCdata):
        self.splitRMC = RMCdata.split(",")
        self.RMClng = float(self.splitRMC[3])
        self.RMClat = float(self.splitRMC[5])

    def DMS(self, rmc, x):
        decMin = math.modf(rmc)
        self.dec = int(str(decMin[1])[:x])
        self.min = int(float(str(decMin[1])[-4:]))
        self.sec = round(decMin[0] * 60, 4)
        return (
            self.dec,
            self.min,
            self.sec
        )
    
    def convDecDeg(self, rmc, x):
        self.DMS(rmc, x)
        print("DMS coord:", self.DMS(rmc, x))
        decDeg = round(self.dec + self.min/60 + self.sec/3600, 4)
        return(decDeg)

    def convLng(self):
        return self.convDecDeg(self.RMClng, 2)


    def convLat(self):
        return self.convDecDeg(self.RMClat, 3)

if __name__== "__main__":

    RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*75"
    position = pos_convert(RMCmessage)
    print("Decimal Degree coord:", position.convLng())
import json
import os
from pos_converter import position_convert
from speed_converter import speed_convert
from datetime import datetime


class jsondump:
    def __init__(self, lat, lon, sog, cog):
        self.date = datetime.today().strftime("%Y-%m-%d")
        self.time = datetime.now().strftime("%H-%M-%S")
        self.lib = {
            "LAT": float(lat),
            "LON": float(lon),
            "SOG": float(sog),
            "COG": int(cog)
        }

    def jsonexport(self):
        filePath = "/Marine AI Competency Exercise/%s/" % self.date

        if os.path.exists(filePath):
            with open("/Marine AI Competency Exercise/%s/rmc_%s.json" % (self.date, self.time), "w") as outfile:
                json.dump(self.lib, outfile)

        if not os.path.exists(filePath):
            os.mkdir(filePath)
            with open("/Marine AI Competency Exercise/%s/rmc_%s.json" % (self.date, self.time), "w") as outfile:
                json.dump(self.lib, outfile)


if __name__ == "__main__":

    RMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    coordonates = position_convert(RMCdata)
    speed = speed_convert(RMCdata)
    lat = coordonates.convLat()
    lon = coordonates.convLng()
    sog = speed.knotsToMps()
    cog = speed.getCog()
    jsonexport = jsondump(lat, lon, sog, cog)
    jsonexport.jsonexport()

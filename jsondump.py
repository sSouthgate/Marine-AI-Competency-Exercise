import json
from pos_converter import position_convert
from speed_converteer import speed_convert
from datetime import date


class jsondump:
    def __init__(self, lat, lon, sog, cog):
        self.date = date.today().strftime("%Y-%m-%d")
        self.lib = {
            "LAT": float(lat),
            "LON": float(lon),
            "SOG": float(sog),
            "COG": int(cog)
        }

    def jsonexport(self):
        with open("rmc_%s.json" %self.date, "w") as outfile:
            json.dump(self.lib, outfile)

    
if __name__== "__main__":
    
    RMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
    coordonates = position_convert(RMCdata)
    speed = speed_convert(RMCdata)
    lat = coordonates.convLat()
    lon = coordonates.convLng()
    sog = speed.knotsToMps()
    cog = speed.getCog()
    jsonexport = jsondump(lat,lon,sog,cog)
    jsonexport.jsonexport()
from checksum import checksum
from pos_converter import position_convert
from speed_converteer import speed_convert
from jsondump import jsondump

# Creating Variables
RMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
cksum = checksum(RMCdata)
coordonates = position_convert(RMCdata)
speed = speed_convert(RMCdata)

def main():
    if cksum.checksumValidate() == True:
        print("chesksum successfully validated")
        lat = coordonates.convLat()
        lng = coordonates.convLng()
        sog = speed.knotsToMps()
        cog = speed.getCog()

        jsonexport = jsondump(lat,lng,sog,cog)
        jsonexport.jsonexport()
        print(jsonexport.lib)
    else:
        print("Failed to validate checksum")
        
main()
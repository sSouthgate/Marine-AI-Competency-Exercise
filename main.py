from checksum import checksum
from pos_converter import position_convert
from speed_converter import speed_convert
from jsondump import jsondump


def main(RMCdata):
    """Input the RMC Data String into the main function to retreive position and speed information to terminal and to a .json file with the date
    """
    cksum = checksum(RMCdata)
    coordonates = position_convert(RMCdata)
    speed = speed_convert(RMCdata)

    if cksum.checksumValidate() == True:
        print("chesksum successfully validated with result: %s" %
              cksum.checksumResult()[2])
        lat = coordonates.convLat()
        lng = coordonates.convLng()
        sog = speed.knotsToMps()
        cog = speed.getCog()

        jsonexport = jsondump(lat, lng, sog, cog)
        jsonexport.jsonexport()
        print("JSON export string: \n", jsonexport.lib)
    else:
        print("Failed to validate checksum")


RMCdata = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
RMCdata1 = "GPRMC,053740.000,A,2503.6319,N,12136.0099,E,2.69,79.65,100106,,,A*53"
RMCdata2 = "$GPRMC,092750.000,A,5321.6802,N,00630.3372,W,0.02,31.66,280511,,,A*43"
RMCdata3 = "GPRMC,203522.00,A,5109.0262308,N,11401.8407342,W,0.004,133.4,130522,0.0,E,D*2B"

main(RMCdata)

import math
import json
from datetime import date

# Variables
RMCmessage = "$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74"
print("RMC Message: ", RMCmessage)
date = date.today().strftime("%Y-%m-%d")

# Split the RMC Message string into a list with "," as delimiter
splitRMC = RMCmessage.split(',')

def knotsToMps(input):
    # Convert knots into m/s
    speed = round(input * 1852 * 0.0002777778, 2)
    return(speed)

def convDecDeg(coord):
    DecDeg = math.modf(coord)
    Deg = int(DecDeg[1])
    # Manipulate decimal to obtain minutes
    Min = math.modf(DecDeg[0] * 60)
    # Manipulates decimal of minutes to obtain seconds
    Sec = round(Min[0] * 60, 4)
    Min = int(Min[1])
    return(Deg, Min, Sec)

lat = convDecDeg(float(splitRMC[3]))
lon = convDecDeg(float(splitRMC[5]))
sog = knotsToMps(float(splitRMC[7]))
# Make this string an int
cog = int(float(splitRMC[8]))

jsonexport = {
    "LAT": lat,
    "LON": lon,
    "SOG": sog,
    "COG": cog
}

with open("rmc_%s.json" %date, "w") as outfile:
    json.dump(jsonexport, outfile)
# Print all to terminal
print("\nLat =", lat, "Lon =", lon, "\nSOG =",sog,"\nCOG =", cog)

# Marine-AI-Competency-Exercise
Small competency exercise designed by Marine AI, relating to their activites.

The aim is to derive, from a given NMEA 0183 sentence, the position, course and speed of a given vessel.<br>
The program should create a JSON file with the desired information, named with current time and placed within a folder marked to the current date.

It must adeer to OOP principles and the Pep8 style guide.

**GitHub Profile:** https://github.com/sSouthgate

## Running the Program (`main()`):

# Commandline or IDE
cd into the `.\Marine_AI_Competency_Exercise` directory and run
```bash
python3 '.\Marine AI Competency Exercise\main.py'
```

# Building and running a docker container
This assumes you have docker installed.<br>
cd into the `Marine_AI_Competency_Exercise` directory and run
```bash
docker build -t nmea_decode .
```
```bash
docker run --volume .\:/usr/local/app/Marine_AI_Competency_Exercise -i -t nmea_decode
```

Running the main program or container will prompt the user to input an NMEA sentence.
Several NMEA sentences are provided in `NMEA_Sentences.txt` for validation of the written code.

Expected output:
```
Enter NMEA Sentence$GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74
NMEA Sentence input: $GPRMC,112000.000,A,5021.5874,N,00408.9009,W,9.09,309.61,201022,,,A*74
chesksum successfully validated with result: 0x74
JSON export string: 
 {'LAT': 50.3598, 'LON': -4.1483, 'SOG': 4.6763, 'COG': 309}
 ```

It will then run and print the JSON string to the terminal after creating the associated file and folder.

## How It's Made:

**Language Used:** Python

Several classes are used to accomplish each required task:

1. Validating the checksum of the NMEA sentence
2. Convert Latitude and Longitude from the NMEA sentence to decimal degrees
3. Convert the SOG from the NMEA from knots to meters per second
4. Output desired information to a JSON string and save it to a date named folder

## CheckSum Class (`checksum`):
This class isolates the NMEA sentence between the `$` and `*` as well as saves the checksum given by the sentence for validation.

The NMEA checksum is a XOR sum, given in hexadecimal, of all ASKI characters found within it, excluding `$`.
By running our own calculation and comparing the result with that of the expected checksum result we can validate the data string.

This is performed by running the `checksumValidate()` function.
it will return True if the checksum is validated for the given NMEA sentence.

## Position Converter Class (`position_convert`):

From the documentation provided, the 3rd amd 5th values in the sentence are latitude and longitude coordonates respectivly, with fields <4> and <5> determining the hemisphere.

Longitude and Latitude are given in a `DDMM.MMMM` format, where `D` and `M` are `Degrees` and `Minutes` respectivly. 
*It is important to note that for longitude there is an extra character to determine the degrees as the highest number can 3 characters long (`180`).*

This means we can isolate the first two to three characters to determine the degrees, then troncate what is left of the interger part for the minutes. Lastly the decimal value are the seconds in minutes, we simply multiply by `60` to obtain the amount of seconds.

This supplies us with the variables to create a DMS coordonate (D°, M', S'').
From the DMS we can easily determine the Decimal Degree following this formula: 
$D_{dec} = D° + (M/60) + (S/3600)$

Running `convLat()` or `convLng()` will return the decimal degree of a supplied RMC message when calling the class. Alternativly `convPosition()` can be used to return both Latitude and Longitude.

## Speed Converter Class (`speed_convert`):

Similarly to the Position Converter Class, speed in knots is given by field <7> of the NMEA sentance.
It is simply extracted and multiplied by $1852/3600$. This convert knots in to meters per second.

Running the `knotsToMps()` function will return the converted value.
`getCog()` simply takes the Course Of Ground value given in field <8> and returns it as an interger value for exporting.

## JSON Dump Class (`jsondump`):

By using the returned values of all previous functions we can use the `jsonexport()` function to export that data into the desired JSON format and creating the required folders and file nomenclature.


## Testing Suite:

To accompagny the code there is a supplied test suite to ensure that all functions work as expected and return the correct values, especially in the case of fake or erronious NMEA sentences.

The suite uses known valid and unvalid NMEA sentences the test the various functions called through the project. The constants used have been cross referenced using online NMEA converters to ensure accuracy of the test environment.

## Lessons Learned:

I had never been required to run a checksum. This project has taught me the value in using them but also how to look for the information used to validate them. Trying out different NMEA sentences allowed me to see errors and oversights originaly made.

Parsing data was also fairly new to me, I have learned alot about manipulating data in python and utilising the languages strengths to simplify certain functions (Turning a string into a float or an int). 
Using a RegEx could be very valuable tool to use to make the code more robust, but validating the checksum also validates the format in a way.

Keeping track of many variable names and convensions can be tricky and I still need more experience so that I don't confuse myself.
Reusing the same ones within an isolated class keeps things easier to read and memorise what they represent like sticking to `RMCdata`.

I am not entirely sure how a ReadMe.md for an excercise such as this should present. So I have opted for explaning the different classes and functions used to achieve the different tasks. AS well as what I have learned.

## Sources:
Here are all the ressources I used to achieve the task:

**Decimal degrees wiki page to learn how to convert:**
https://en.wikipedia.org/wiki/Decimal_degrees

**Splitting interger and decimal for floats:**
https://stackoverflow.com/questions/6681743/splitting-a-number-into-the-integer-and-decimal-parts

**Knot wiki page to get convertion numbers:**
https://en.wikipedia.org/wiki/Knot_(unit)

**Meter per hour to meter per second converter for conversion table:**
https://www.unitconverters.net/speed/meter-hour-to-meter-second.htm

**Writting to a JSON file in python with json python package:**
https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

**How to calculate NMEA checksum:**
https://rietman.wordpress.com/2008/09/25/how-to-calculate-the-nmea-checksum/

**NMEA sentence checksum (Python recipe):**
https://code.activestate.com/recipes/576789-nmea-sentence-checksum/

**NMEA 0183 wiki page - used for GPRMC referances:**
https://en.wikipedia.org/wiki/NMEA_0183

**NMEA 0183 wiki page (FR):**
https://fr.wikipedia.org/wiki/NMEA_0183

**Converting Degrees, Minutes, and Seconds to Decimal Degrees - Vocabulary and Equations:**
https://study.com/skill/learn/how-to-convert-degrees-minutes-seconds-to-decimal-degrees-explanation.html

**Pep8 Style Guide:**
https://peps.python.org/pep-0008/

**autopep8 for VSCode:**
https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8

**NMEA Analyser for testing:**
https://swairlearn.bluecover.pt/nmea_analyser

**How to write a readme.md:**
https://www.reddit.com/r/learnprogramming/comments/vxfku6/how_to_write_a_readme/

**ReadMe.md template:**
https://github.com/alec-chernicki/portfolio-template/tree/master

**Writing mathematical expressions (for GitHub ReadMe):**
https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions

**How to “Dockerize” Your Python Applications:**
https://www.docker.com/blog/how-to-dockerize-your-python-applications/

**Writing a Dockerfile:**
https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/

**Dockerfile reference:**
https://docs.docker.com/reference/dockerfile/#add

**Docker Volumes:**
https://docs.docker.com/engine/storage/volumes/
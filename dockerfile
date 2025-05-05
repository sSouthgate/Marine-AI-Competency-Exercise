# Dockerfile, Image, Container

FROM python:3.9

WORKDIR /usr/local/app/Marine_AI_Competency_Exercise

ADD main.py checksum.py pos_converter.py speed_converter.py jsondump.py testsuite.py NMEA_Sentences.txt /usr/local/app/Marine_AI_Competency_Exercise/

CMD ["python", "./main.py"]
#creating docker image

FROM python:3.11.4-bookworm

#CMD tail -f /dev/null
RUN apt-get update && apt-get install -y python3-dev build-essential
 
COPY  requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
COPY . /tmp/

COPY app.py /etc

COPY . .
CMD ./app.py
 
# EXPOSE 5000
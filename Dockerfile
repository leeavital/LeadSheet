FROM python:2.7

RUN apt-get update

ADD lib lib
EXPOSE 5000

# install MIDIUtil
RUN apt-get install unzip \
    && cd lib \
    && unzip MIDIUtil-0.89.zip \
    && cd MIDIUtil-0.89 \
    && python setup.py install

# install timidity
RUN apt-get -y install timidity

ADD src/ app/

RUN pip install flask

# run
WORKDIR /app
CMD ["python", "flaskr.py"]

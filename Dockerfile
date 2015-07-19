FROM python:2.7

RUN apt-get update -qqy; \
    apt-get install -qqy \
        nodejs \
        npm; \
    cp $(which nodejs) /bin/node; \
    apt-get clean -qqy;
RUN git clone https://github.com/sugarlabs/docker /docker; \
    cd /docker; \
    /usr/bin/npm install

RUN git clone https://github.com/sugarlabs/sugar-docs /docs
ADD . /app
RUN pip install -r /app/requirements.txt

WORKDIR /docs
CMD python /app/main.py

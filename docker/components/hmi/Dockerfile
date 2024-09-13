# HMI Dockerfile
FROM python

WORKDIR /usr/src/app

RUN apt-get update

RUN pip install flask
RUN pip install flask requests

COPY . .

# ENTRYPOINT [ "curl" ]

CMD python hmi.py
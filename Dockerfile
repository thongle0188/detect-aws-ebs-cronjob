FROM python:3.6-alpine

ADD script.py /
COPY requirements.txt /
WORKDIR /
RUN apk add --no-cache --virtual .build_deps gcc musl-dev \
    && pip3 install -r requirements.txt

CMD [ "python", "./script.py" ]
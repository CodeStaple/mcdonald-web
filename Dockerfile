FROM alpine:3.13.0

RUN set -e; \
  apk update \
  && apk add --virtual .build-deps gcc python3 py3-configobj py3-setuptools python3-dev py3-pip musl-dev libffi-dev curl gcc bash openssl \
  # Workaround for Cryptography
  && apk del libressl-dev \
  && apk add openssl-dev \
  && pip install cryptography==2.2.2 \  
  && apk del openssl-dev \
  && apk add libressl-dev \
  # Workaround end
  && pip3 install --upgrade pip cffi

ADD src/requirements.txt /opt/src/requirements.txt
RUN pip3 install -r /opt/src/requirements.txt
ADD src /opt/src

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

ARG IMAGE=containers.intersystems.com/intersystems/iris:2021.2.0.651.0
ARG IMAGE=intersystemsdc/iris-community

FROM $IMAGE

WORKDIR /irisdev/app

COPY src src
COPY module.xml module.xml
COPY iris.script /tmp/iris.script

RUN iris start IRIS \
	&& iris session IRIS < /tmp/iris.script \
    && iris stop IRIS quietly

# create Python env
ENV PYTHON_PATH=/usr/irissys/bin/irispython
ENV SRC_PATH=/irisdev/app
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "USER"

RUN pip3 install flask gunicorn

ENTRYPOINT [ "/tini", "--", "/irisdev/app/entrypoint.sh" ]
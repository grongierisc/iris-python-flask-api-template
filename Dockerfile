ARG IMAGE=intersystemsdc/iris-community
ARG IMAGE=containers.intersystems.com/intersystems/iris:2021.2.0.651.0
FROM $IMAGE

COPY key/iris.key /usr/irissys/mgr/iris.key

USER root   
        
WORKDIR /irisdev/app
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /irisdev/app
USER ${ISC_PACKAGE_MGRUSER}

COPY  src src
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

RUN ln -s /usr/irissys/bin/irispython /usr/irissys/bin/python

RUN pip3 install flask gunicorn

ENTRYPOINT [ "/tini", "--", "/irisdev/app/entrypoint.sh" ]
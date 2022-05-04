# 1. intersystems-iris-docker-rest-template
This is a template of a REST API application built in python in InterSystems IRIS.
It also has OPEN API spec, can be developed with Docker and VSCode.

- [1. intersystems-iris-docker-rest-template](#1-intersystems-iris-docker-rest-template)
- [2. Prerequisites](#2-prerequisites)
- [3. Installation](#3-installation)
  - [3.1. Installation for development](#31-installation-for-development)
- [4. How to Work With it](#4-how-to-work-with-it)
  - [4.1. Testing POST request](#41-testing-post-request)
  - [4.2. Testing GET requests](#42-testing-get-requests)
  - [4.3. Testing PUT request](#43-testing-put-request)
  - [4.4. Testing DELETE request](#44-testing-delete-request)
- [5. How to start coding](#5-how-to-start-coding)
- [6. What's insde the repo](#6-whats-insde-the-repo)
  - [6.1. Dockerfile](#61-dockerfile)
  - [6.2. .vscode/settings.json](#62-vscodesettingsjson)
  - [6.3. .vscode/launch.json](#63-vscodelaunchjson)


# 2. Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

# 3. Installation

## 3.1. Installation for development

Clone/git pull the repo into any local directory e.g. like it is shown below:
```
$ git clone https://github.com/grongierisc/iris-python-flask-api-template.git
```

Open the terminal in this directory and run:

```
$ docker-compose up -d --build
```

# 4. How to Work With it

This template creates /crud REST web-application on IRIS which implements 4 types of communication: GET, POST, PUT and DELETE aka CRUD operations.
These interface works with a sample persistent class `Person` found in `src/python/person/obj.py`.

First of all, it is needed to start the 'app.py' situated in `src/python/person/app.py` using flask.<br>
To do this, go in the `app.py` file, then to the `run and debug` window in VSCode and select `Python: Flask` then run.
This will run the app.

## 4.1. Testing POST request

Create a POST request,for example in Postman or in RESTer for mozilla, with raw data in JSON like:
```
{"Name":"Elon Mask","Title":"CEO","Company":"Tesla","Phone":"123-123-1233","DOB":"1982-01-19"}
```
Using `Content-Type` as `application/json`

Adjust the authorisation if needed - it is basic for container with default login and password for IRIS Community edition container.<br>
Send the POST request to `localhost:5000/persons/`
This will create a record in the table Sample.Person of IRIS.

![Here is an example](https://user-images.githubusercontent.com/77791586/165950755-0800b414-a26a-4616-9360-4ecf41c90363.mov) of the POST request to ad Elon Musk to the table.

## 4.2. Testing GET requests

To test GET you need to have some data. You can create it with a [POST request](#41-testing-post-request).

This REST API exposes two GET requests: all the data and one record.
To get all the data in JSON call:
```
localhost:5000/persons/all
```

To request the data for a particular record provide the id in GET request like 'localhost:5000/persons/id', here is an example:
```
localhost:5000/persons/1
```

This will return JSON data for the person with ID=1, something like that:
```
{"Name":"Elon Mask","Title":"CEO","Company":"Tesla","Phone":"123-123-1233","DOB":"1982-01-19"}
```

## 4.3. Testing PUT request

PUT request could be used to update the records. This needs to send the similar JSON as in POST request above supplying the id of the updated record in URL.
For example we want to change the record with id=5. Prepare the JSON in raw like following:
```
{"Name":"Jeff Besos","Title":"CEO","Company":"Amazon","Phone":"123-123-1233","DOB":"1982-01-19"}
```

and send the put request to:
```
localhost:5000/persons/5
```

## 4.4. Testing DELETE request

For delete request this REST API expects only the id of the record to delete. E.g. if the id=5 the following DELETE call will delete the record:

```
localhost:5000/persons/5
```

# 5. How to start coding
This repository is ready to code in VSCode with InterSystems plugins.
Open `/src/python/person/app.py` to change anything on the api.
Open `/src/python/person/bo.py` to be able to change things related to the internal requests, this is where you can use SQL - it will be compiled in running IRIS docker container.

# 6. What's insde the repo

## 6.1. Dockerfile

The simplest dockerfile to start IRIS.
Use the related docker-compose.yml to easily setup additional parametes like port number and where you map keys and host folders.

## 6.2. .vscode/settings.json

Settings file to let you immedietly code in VSCode with [VSCode ObjectScript plugin](https://marketplace.visualstudio.com/items?itemName=daimor.vscode-objectscript))

## 6.3. .vscode/launch.json
Config file if you want to debug with VSCode ObjectScript

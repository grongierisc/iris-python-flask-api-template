# 1. intersystems-iris-docker-rest-template
This is a template of a REST API application built in python in InterSystems IRIS.
It also has OPEN API spec, can be developed with Docker and VSCode.

- [1. intersystems-iris-docker-rest-template](#1-intersystems-iris-docker-rest-template)
- [2. Prerequisites](#2-prerequisites)
- [3. Installation](#3-installation)
  - [3.1. Installation for development](#31-installation-for-development)
  - [3.2. Management Portal and VSCode](#32-management-portal-and-vscode)
  - [3.3. Having the folder open inside the container](#33-having-the-folder-open-inside-the-container)
- [4. How it works](#4-how-it-works)
- [5. How to Work With it](#5-how-to-work-with-it)
  - [5.1. POST request](#51-post-request)
    - [5.1.1. Testing POST request](#511-testing-post-request)
    - [5.1.2. How POST request works](#512-how-post-request-works)
  - [5.2. GET requests](#52-get-requests)
    - [5.2.1. Testing GET request](#521-testing-get-request)
    - [5.2.2. How GET request works](#522-how-get-request-works)
  - [5.3. PUT request](#53-put-request)
    - [5.3.1. Testing PUT request](#531-testing-put-request)
    - [5.3.2. How PUT request works](#532-how-put-request-works)
  - [5.4. DELETE request](#54-delete-request)
    - [5.4.1. Testing DELETE request](#541-testing-delete-request)
    - [5.4.2. How DELETE request works](#542-how-delete-request-works)
- [6. How to start coding](#6-how-to-start-coding)
- [7. What's inside the repo](#7-whats-inside-the-repo)
  - [7.1. Dockerfile](#71-dockerfile)
  - [7.2. .vscode/settings.json](#72-vscodesettingsjson)
  - [7.3. .vscode/launch.json](#73-vscodelaunchjson)


# 2. Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

It is to be noted that the table Sample.Person was already created in advance for the demo using in the management portal in the sql tab:
```sql
CREATE TABLE Sample.Person (

         Company                                  VARCHAR(50),
         DOB                                      DATE,
         Name                                     VARCHAR(4096),
         Phone                                    VARCHAR(4096),
         Title                                    VARCHAR(50)
)
```

# 3. Installation

## 3.1. Installation for development

Clone/git pull the repo into any local directory e.g. like it is shown below:
```
$ git clone https://github.com/grongierisc/iris-python-flask-api-template.git
```

Open the terminal in this directory and run:

```
$ DOCKER_BUILDKIT=1 docker-compose up -d --build
```
## 3.2. Management Portal and VSCode

This repository is ready for [VS Code](https://code.visualstudio.com/).

Open the locally-cloned `formation-template-python` folder in VS Code.

If prompted (bottom right corner), install the recommended extensions.

## 3.3. Having the folder open inside the container
**It is really important** to be *inside* the container before coding.<br>
For this, docker must be on before opening VSCode.<br>
Then, inside VSCode, when prompted (in the right bottom corner), reopen the folder inside the container so you will be able to use the python components within it.<br>
The first time you do this it may take several minutes while the container is readied.

[More information here](https://code.visualstudio.com/docs/remote/containers)

![Architecture](https://code.visualstudio.com/assets/docs/remote/containers/architecture-containers.png)

<br><br><br>

By opening the folder remote you enable VS Code and any terminals you open within it to use the python components within the container. Configure these to use `/usr/irissys/bin/irispython`

<img width="1614" alt="PythonInterpreter" src="https://user-images.githubusercontent.com/47849411/145864423-2de24aaa-036c-4beb-bda0-3a73fe15ccbd.png">

# 4. How it works

The `app.py`, once launched (inside the container) will gather CRUD request.<br>
Depending on the type of the request, the right message will be created to send to the `FlaskService`, this service will call the CrudPerson operation that will, depending on the type of the message send from the service to it, dispatch the information needed to do the action requested.

For more details you can check the `How it works` part of [this fully documented demo](https://github.com/grongierisc/interoperability-embedded-python).

# 5. How to Work With it

This template creates /crud REST web-application on IRIS which implements 4 types of communication: GET, POST, PUT and DELETE aka CRUD operations.
These interface works with a sample persistent class `Person` found in `src/python/person/obj.py`.

First of all, it is needed to start the 'app.py' situated in `src/python/person/app.py` using flask.<br>
To do this, go in the `app.py` file, then to the `run and debug` window in VSCode and select `Python: Flask` then run.
This will run the app.
## 5.1. POST request

### 5.1.1. Testing POST request

Create a POST request, for example in Postman or in RESTer for mozilla, with raw data in JSON like:
```json
{"name":"Elon Musk","title":"CEO","company":"Tesla","phone":"123-123-1233","dob":"1982-01-19"}
```
Using `Content-Type` as `application/json`

Adjust the authorisation if needed - it is basic for container with default login and password for IRIS Community edition container.<br>
Send the POST request to `localhost:5000/persons/`<br>
This will create a record in the table Sample.Person of IRIS and return the `id` of the newly added `Person`

![Here is an example](https://user-images.githubusercontent.com/77791586/166916610-de0791ab-18d4-4dd4-a416-fffb9b6254cb.mov) of the POST request to add `Elon Musk` to the table.

### 5.1.2. How POST request works

```python
    def create_person(self,request:CreatePersonRequest):
        """
        > Create a new person in the database and return the new person's ID
        
        :param request: The request object that was passed in from the client
        :type request: CreatePersonRequest
        :return: The ID of the newly created person.
        """

        # sqlInsert = 'insert into Sample.Person values (?,?,?,?,?)'
        # iris.sql.exec(sqlInsert,request.person.company,dob,request.person.name,request.person.phone,request.person.title)
        
        # IRIS ORM
        person = iris.cls('Sample.Person')._New()
        if (v:=request.person.company) is not None: person.Company = v 
        if (v:=request.person.name) is not None: person.Name = v 
        if (v:=request.person.phone) is not None: person.Phone = v 
        if (v:=request.person.title) is not None: person.Title = v 
        if (v:=request.person.dob) is not None: person.DOB = v 

        Utils.raise_on_error(person._Save())
        
        return CreatePersonResponse(person._Id())
```
Using IRIS ORM we can create a new `Person` and save into our database.


## 5.2. GET requests

### 5.2.1. Testing GET request

To test GET you need to have some data. You can create it with a [POST request](#41-testing-post-request).

This REST API exposes two GET requests: all the data and one record.
To get all the data in JSON call:
```
localhost:5000/persons/all
```

<br><br>

To request the data for a particular record provide the id in GET request like 'localhost:5000/persons/id', here is an example:
```
localhost:5000/persons/1
```

This will return JSON data for the person with ID=1, something like that:
```json
{"name":"Elon Musk","title":"CEO","company":"Tesla","phone":"123-123-1233","dob":"1982-01-19"}
```

### 5.2.2. How GET request works

```python
    def get_person(self,request:GetPersonRequest):
        """
        > The function takes a `GetPersonRequest` object, executes a SQL query, and returns a
        `GetPersonResponse` object
        
        :param request: The request object that is passed in
        :type request: GetPersonRequest
        :return: A GetPersonResponse object
        """
        sql_select = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            where ID = ?
            """
        rs = iris.sql.exec(sql_select,request.id)
        response = GetPersonResponse()
        for person in rs:
            response.person= Person(company=person[0],dob=person[1],name=person[2],phone=person[3],title=person[4])
        return response

    def get_all_person(self,request:GetAllPersonRequest):
        """
        > This function returns a list of all the people in the Person table
        
        :param request: The request object that is passed to the service
        :type request: GetAllPersonRequest
        :return: A list of Person objects
        """

        sql_select = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            """
        rs = iris.sql.exec(sql_select)
        response = GetAllPersonResponse()
        response.persons = list()
        for person in rs:
            response.persons.append(Person(company=person[0],dob=person[1],name=person[2],phone=person[3],title=person[4]))
        return response
```

This time, using the `iris python` `sql.exec` function, we can directly run SQL code inside the IRIS database, gather the information needed and send it back to the API and to the user.


## 5.3. PUT request
### 5.3.1. Testing PUT request

PUT request could be used to update the records. This needs to send the similar JSON as in POST request above supplying the id of the updated record in URL.
For example we want to change the record with id=5. Prepare the JSON in raw like following:
```
{"name":"Jeff Besos","title":"CEO","company":"Amazon","phone":"123-123-1233","dob":"1982-01-19"}
```

and send the put request to:
```
localhost:5000/persons/5
```

### 5.3.2. How PUT request works

```python
    def update_person(self,request:UpdatePersonRequest):
        """
        > Update a person in the database
        
        :param request: The request object that will be passed to the service
        :type request: UpdatePersonRequest
        :return: UpdatePersonResponse()
        """

        # IRIS ORM
        if iris.cls('Sample.Person')._ExistsId(request.id):
            person = iris.cls('Sample.Person')._OpenId(request.id)
            if (v:=request.person.company) is not None: person.Company = v 
            if (v:=request.person.name) is not None: person.Name = v 
            if (v:=request.person.phone) is not None: person.Phone = v 
            if (v:=request.person.title) is not None: person.Title = v 
            if (v:=request.person.dob) is not None: person.DOB = v 
            Utils.raise_on_error(person._Save())
        
        return UpdatePersonResponse()
```
Using IRIS ORM we can check if the id leads to a `Person`, if it does, we can update it using our new information and save it into our database.

## 5.4. DELETE request
### 5.4.1. Testing DELETE request

For delete request this REST API expects only the id of the record to delete. E.g. if the id=5 the following DELETE call will delete the record:

```
localhost:5000/persons/5
```
### 5.4.2. How DELETE request works

```python
    def delete_person(self,request:DeletePersonRequest):
        """
        > Delete a person from the database
        
        :param request: The request object that is passed to the service
        :type request: DeletePersonRequest
        :return: The response is being returned.
        """

        sql_select = """
            DELETE FROM Sample.Person as Pers
            WHERE Pers.id = ?
            """
        rs = iris.sql.exec(sql_select,request.id)
        response = DeletePersonResponse()
        return response
```

This time, using the `iris python` `sql.exec` function, we can directly run SQL code inside the IRIS database and delete the person.

# 6. How to start coding
This repository is ready to code in VSCode with InterSystems plugins.
Open `/src/python/person/app.py` to change anything on the api.
Open `/src/python/person/bo.py` to be able to change things related to the internal requests, this is where you can use SQL - it will be compiled in running IRIS docker container.

# 7. What's inside the repo

## 7.1. Dockerfile

The simplest dockerfile to start IRIS.
Use the related docker-compose.yml to easily setup additional parametes like port number and where you map keys and host folders.

## 7.2. .vscode/settings.json

Settings file to let you immedietly code in VSCode with [VSCode ObjectScript plugin](https://marketplace.visualstudio.com/items?itemName=daimor.vscode-objectscript))

## 7.3. .vscode/launch.json
Config file if you want to debug with VSCode ObjectScript

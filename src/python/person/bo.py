import iris
from datetime import date

from grongier.pex import BusinessOperation
from grongier.pex import Utils


from msg import (CreatePersonResponse,CreatePersonRequest,
                            GetPersonRequest,GetPersonResponse,
                            GetAllPersonRequest,GetAllPersonResponse,
                            UpdatePersonRequest,UpdatePersonResponse,
                            DeletePersonRequest,DeletePersonResponse
)

from obj import Person

# > The CrudPerson class is a business operation that handles Create, Update, Get and GetAll requests
# for a Person object
class CrudPerson(BusinessOperation):

    def on_message(self, request):
        return 

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
        if (v:=request.person.dob) is not None: person.DOB = iris.system.SQL.DATE(v.isoformat())

        Utils.raise_on_error(person._Save())
        
        return CreatePersonResponse(person._Id())

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
            if (v:=request.person.dob) is not None: person.DOB = iris.system.SQL.DATE(v.isoformat())
            Utils.raise_on_error(person._Save())
        
        return UpdatePersonResponse()

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
            try:
                dob = date.fromisoformat(iris.system.SQL.TOCHAR(person[1],"YYYY-MM-DD"))
            except:
                dob = ''
            response.person= Person(company=person[0],dob=dob,name=person[2],phone=person[3],title=person[4])
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
            try:
                dob = date.fromisoformat(iris.system.SQL.TOCHAR(person[1],"YYYY-MM-DD"))
            except:
                dob = ''
            response.persons.append(Person(company=person[0],dob=dob,name=person[2],phone=person[3],title=person[4]))
        return response

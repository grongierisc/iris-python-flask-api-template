import iris
import uuid,decimal
from datetime import datetime
from grongier.pex import BusinessOperation


from interop.msg import (CreatePersonResponse,CreatePersonRequest,
                            GetPersonRequest,GetPersonResponse,
                            GetAllPersonResquest,GetAllPersonResponse,
                            UpdatePersonRequest,UpdatePersonResponse
)

from interop.obj import Person

class CrudPerson(BusinessOperation):

    # It's can be dynamic, but here for demo purpose it's hard coded
    DISPATCH  = [
                    ('interop.msg.CreatePersonRequest','CreatePerson'),
                    ('interop.msg.GetAllPersonRequest','GetAllPerson'),
                    ('interop.msg.GetPersonRequest','GetPerson'),
                    ('interop.msg.UpdatePersonRequest','UpdatePerson'),
                ]

    def OnMessage(self, request):
        return 

    def CreatePerson(self,request:CreatePersonRequest):

        # sqlInsert = 'insert into Sample.Person values (?,?,?,?,?)'
        # iris.sql.exec(sqlInsert,request.person.company,dob,request.person.name,request.person.phone,request.person.title)
        
        # IRIS ORM
        person = iris.cls('Sample.Person')._New()
        if (v:=request.person.company) is not None: person.Company = v 
        if (v:=request.person.name) is not None: person.Name = v 
        if (v:=request.person.phone) is not None: person.Phone = v 
        if (v:=request.person.title) is not None: person.Title = v 
        if (v:=request.person.dob) is not None: person.DOB = v 

        person._Save()
        
        return CreatePersonResponse(person._Id())

    def UpdatePerson(self,request:UpdatePersonRequest):

        # IRIS ORM
        if iris.cls('Sample.Person')._ExistsId(request.id):
            person = iris.cls('Sample.Person')._OpenId(request.id)
            if (v:=request.person.company) is not None: person.Company = v 
            if (v:=request.person.name) is not None: person.Name = v 
            if (v:=request.person.phone) is not None: person.Phone = v 
            if (v:=request.person.title) is not None: person.Title = v 
            if (v:=request.person.dob) is not None: person.DOB = v 
            person._Save()
        
        return UpdatePersonResponse()

    def GetPerson(self,request:GetPersonRequest):
        sqlSelect = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            where ID = ?
            """
        rs = iris.sql.exec(sqlSelect,request.id)
        response = GetPersonResponse()
        for person in rs:
            response.person= Person(person[0],person[1],person[2],person[3],person[4])
        return response

    def GetAllPerson(self,request:GetAllPersonRequest):
        sqlSelect = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            """
        rs = iris.sql.exec(sqlSelect)
        response = GetAllPersonResponse()
        response.persons = list()
        for person in rs:
            response.persons.append(Person(person[0],person[1],person[2],person[3],person[4]))
        return response


if __name__ == '__main__':
    pass
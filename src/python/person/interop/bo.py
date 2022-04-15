from grongier.pex import BusinessOperation
import iris

from msg import (CreatePersonResponse,CreatePersonRequest,
                            GetPersonRequest,GetPersonResponse,
                            GetAllPersonResquest,GetAllPersonResponse
)

from obj import Person

class CrudPerson(BusinessOperation):

    def OnMessage(self, request):
        if isinstance(request,CreatePersonRequest):
            return self.CreatePerson(request)
        if isinstance(request,GetAllPersonResquest):
            return self.GetAllPerson(request)

        return 

    def CreatePerson(self,request:CreatePersonRequest):
        sqlInsert = 'insert into Sample.Person values (?,?,?,?,?)'
        iris.sql.exec(sqlInsert,request.Person.Company,request.Person.DOB,request.Person.Name,request.Person.Phone,request.Person.Title)
        return CreatePersonResponse()

    def GetPerson(self,request:GetPersonRequest):
        sqlSelect = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            where ID = ?"""
        rs = iris.sql.exec(sqlSelect,request.Id)
        response = GetPersonResponse()
        for person in rs:
            response.Person= Person(person)
        return response

    def GetAllPerson(self,request:GetPersonRequest):
        sqlSelect = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            """
        rs = iris.sql.exec(sqlSelect)
        response = GetAllPersonResponse()
        response.Persons = list()
        for person in rs:
            response.Persons.append(Person(person))
        return response

if __name__ == '__main__':
    crudPerson = CrudPerson()
    request = GetAllPersonResquest()
    response = crudPerson.OnMessage(request)
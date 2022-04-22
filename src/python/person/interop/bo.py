from grongier.pex import BusinessOperation
import iris
from datetime import datetime
import uuid,decimal

from interop.msg import (CreatePersonResponse,CreatePersonRequest,
                            GetPersonRequest,GetPersonResponse,
                            GetAllPersonResquest,GetAllPersonResponse
)

from interop.obj import Person

class CrudPerson(BusinessOperation):

    DISPATCH  = [
                    ('interop.msg.CreatePersonRequest','CreatePerson'),
                    ('interop.msg.GetPersonRequest','GetPerson')
                ]

    def OnMessage(self, request):
        if isinstance(request,CreatePersonRequest):
            return self.CreatePerson(request)
        if isinstance(request,GetAllPersonResquest):
            return self.GetAllPerson(request)

        return 

    def CreatePerson(self,request:CreatePersonRequest):
        sqlInsert = 'insert into Sample.Person values (?,?,?,?,?)'
        if request.person.dob is None:
            dob = ''
        else:
            dob = request.person.dob
        iris.sql.exec(sqlInsert,request.person.company,dob,request.person.name,request.person.phone,request.person.title)
        return CreatePersonResponse()

    def GetPerson(self,request:GetPersonRequest):
        sqlSelect = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            where ID = ?"""
        rs = iris.sql.exec(sqlSelect,request.id)
        response = GetPersonResponse()
        #response.person = Person(name='name',company='company',title='title',phone='phone',dob=datetime.now())
        for person in rs:
            response.person= Person(person)
        return response

    def GetAllPerson(self,request:GetPersonRequest):
        sqlSelect = """
            SELECT 
                Company, DOB, Name, Phone, Title
            FROM Sample.Person
            """
        rs = iris.sql.exec(sqlSelect)
        response = GetAllPersonResponse()
        response.persons = list()
        # person = Person(nameBytes=b'name',companyUUID=uuid.uuid4(),titleDecimal=decimal.Decimal(10),phone='phone',dob=datetime.now())
        # response.persons.append(person)
        for person in rs:
            response.persons.append(Person(person))
        return response

class MyOperation(BusinessOperation):

    def OnMessage(self, request):
        self.LOGINFO('toto')
        return 
        
    def EnsString(self,reques:'iris.Ens.StringRequest'):
        return iris.cls('Ens.StringResponse')._New(reques.StringValue)

    def EnsPython(self,request:GetPersonRequest):
        return iris.cls('Ens.StringResponse')._New('GetPersonRequest')

if __name__ == '__main__':
    crudPerson = MyOperation()
    crudPerson._dispatchOnInit('')
    request = iris.cls('Ens.StringRequest')._New('toto')
    response = crudPerson._dispatchOnMessage(request)

    # request = GetAllPersonResquest()
    # request = 'msg.CreatePersonRequest:{"person": {"nameBytes": "bytes:bmFtZQ==", "titleDecimal": "decimal:10", "companyUUID": "uuid:d162d152-b1fe-4cd6-aadb-af861d2087a6", "phone": "phone", "dob": "datetime:2022-04-19T15:57:08.331"} }'
    # response = crudPerson._dispatchOnMessage(request)
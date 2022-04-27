from bo import CrudPerson
from msg import GetAllPersonRequest
from obj import Person

if __name__ == '__main__':
    crud = CrudPerson()
    json = {"name":"test"}
    person = Person(**json)
    msg = GetAllPersonRequest()
    response = crud.GetAllPerson(msg)
    

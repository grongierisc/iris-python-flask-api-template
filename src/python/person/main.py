from interop.bo import CrudPerson
from interop.msg import GetAllPersonResquest
from interop.obj import Person

if __name__ == '__main__':
    crud = CrudPerson()
    json = {"name":"test"}
    person = Person(**json)
    msg = GetAllPersonResquest()
    response = crud.GetAllPerson(msg)
    pass

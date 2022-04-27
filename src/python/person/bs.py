# Importing the `BusinessService` class from the `grongier.pex` module.
from grongier.pex import BusinessService

# > The FlaskService class is a BusinessService that sends a request to the CrudPerson service and
# returns the response
class FlaskService(BusinessService):

    def OnInit(self):
        
        if not hasattr(self,'target'):
            self.target = "Python.CrudPerson"
        
        return 

    def OnProcessInput(self,request):

        return self.SendRequestSync(self.target,request)

 
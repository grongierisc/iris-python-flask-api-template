# Importing the `BusinessService` class from the `grongier.pex` module.
from grongier.pex import BusinessService

# > The FlaskService class is a BusinessService that sends a request to the CrudPerson service and
# returns the response
class FlaskService(BusinessService):

    def on_init(self):
        
        if not hasattr(self,'target'):
            self.target = "Python.CrudPerson"
        
        return 

    def on_process_input(self,request):
        res = self.send_request_sync(self.target,request)
        return res

 
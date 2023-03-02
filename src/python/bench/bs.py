# Importing the `BusinessService` class from the `grongier.pex` module.
from grongier.pex import BusinessService

# > The FlaskService class is a BusinessService that sends a request to the CrudPerson service and
# returns the response
class BenchService(BusinessService):

    def on_init(self):
        
        if not hasattr(self,'target'):
            self.target = "Python.BenchOperation"
        
        return 

    def on_process_input(self,request):
        
        self.iris_handle._RequestHeader.Priority = request.value

        return self.send_request_sync(self.target,request)

 
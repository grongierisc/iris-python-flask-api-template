from grongier.pex import BusinessService

class FlaskService(BusinessService):

    def OnInit(self):
        
        if not hasattr(self,'Target'):
            self.Target = "Python.CrudPerson"
        
        return 

    def OnProcessInput(self,request):

        return self.SendRequestSync(self.Target,request)

 
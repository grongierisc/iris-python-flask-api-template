import grongier.pex

class FlaskService(grongier.pex.BusinessService):

    def OnInit(self):
        
        if not hasattr(self,'Target'):
            self.Target = "Python.CrudPerson"
        
        self.LastPostName = ""
        
        return 1

    def OnProcessInput(self,request):

        return self.SendRequestSync(self.Target,request)

 
from grongier.pex import BusinessOperation

import time

class BenchOperation(BusinessOperation):

    def on_message(self, request):
        # wait for 1 second use time.sleep(1)
        time.sleep(1)
        return request
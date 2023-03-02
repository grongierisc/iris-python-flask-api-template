Class ObjectScript.BS Extends Ens.BusinessService
{

Method OnProcessInput(pDocIn As %RegisteredObject, Output pDocOut As %RegisteredObject) As %Status
{
    set status = $$$OK

    try {
        Set ..%RequestHeader = ##class(Ens.MessageHeader).%New()
        set ..%RequestHeader.Priority = 3
        set ..%RequestHeader.TimeCreated = ""

        if $IsObject(..%RequestHeader)&&(""=..%RequestHeader.TimeCreated) {
            $$$LOGINFO("TimeCreated is empty")
        }

        $$$LOGINFO("Before Send"_..%RequestHeader.Priority)
        $$$ThrowOnError(..SendRequestSync("Python.BenchOperation",pDocIn,.pDocOut))
        $$$LOGINFO("After Send"_..%RequestHeader.Priority)
        
    } catch ex {
        set status = ex.AsStatus()
    }

    Quit status
}

}

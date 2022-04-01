Class Python.CrudPerson Extends Grongier.PEX.BusinessOperation [ GeneratedBy = Grongier.PEX.Utils ]
{

Parameter SETTINGS = "%classname:Python ,%module:Python ,%settings:Python ,%classpaths:Python ";

Property %classname As %String [ InitialExpression = "CrudPerson", Internal ];

/// One or more Classpaths (separated by '|' character) needed in addition to the ones configured in the Remote Gateway
Property %classpaths As %String(MAXLEN = "") [ InitialExpression = "/irisdev/app/src/python/flask/|/irisdev/app/src/python/flask/interop" ];

Property %module As %String [ InitialExpression = "CrudPerson", Internal ];

}

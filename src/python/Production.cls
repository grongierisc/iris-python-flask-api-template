Class Python.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="Python.Production" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="Python.FlaskService" Category="" ClassName="Python.FlaskService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%classpaths">/irisdev/app/src/python/flask/</Setting>
    <Setting Target="Host" Name="%module">interop.FlaskService</Setting>
  </Item>
  <Item Name="Python.CrudPerson" Category="" ClassName="Python.CrudPerson" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%classpaths">/irisdev/app/src/python/flask/</Setting>
    <Setting Target="Host" Name="%module">interop.CrudPerson</Setting>
  </Item>
</Production>
}

}

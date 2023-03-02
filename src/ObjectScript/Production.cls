Class Python.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="Python.Production" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="Python.BenchService" Category="" ClassName="Python.BenchService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
  <Item Name="Python.BenchOperation" Category="" ClassName="Python.BenchOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
</Production>
}

}

###importing wbgapi, pandas
import wbgapi as wb
import pandas as pd

###importing CO2 emisssions dataset using wbgapi, and creating a transposed version of it
wb.source.info()
df=wb.data.DataFrame('EN.ATM.CO2E.LF.KT',['ARG', 'BDI', 'BRA', 'CAF', 'CHE', 'CMR', 'CYM', 'DNK', 'FJI', 'MEX'], range(2000,2010)).transpose()
dfclimate=pd.DataFrame(df)
df2=wb.data.DataFrame('EN.ATM.CO2E.LF.KT',['ARG', 'BDI', 'BRA', 'CAF', 'CHE', 'CMR', 'CYM', 'DNK', 'FJI', 'MEX'], range(2000,2010))
dfclimate2=pd.DataFrame(df2)



###line graph for the dflimate dataset imported 
dfclimate.plot()
df.plot()
###bar plot of the dfclimate2 dataset
dfclimate2.plot.bar()

##importing various datasets for merging before the heatmap
##dfclimate.plot(x='ARG', 'BDI', 'BRA', 'CAF', 'CHE', 'CMR', 'CYM', 'DNK', 'FJI', 'MEX', kind='line', title="CO2 Emission by country")
##elec_access='EG.ELC.RNWX.KH'
##countries=['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX']
##dff=wb.data.DataFrame('EG.ELC.RNWX.KH',['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX'] , range(2000,2010))
##dff
agricultural_land='AG.LND.AGRI.ZS'
countriesAGRIC=['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX']
dffagric=wb.data.DataFrame('AG.LND.AGRI.ZS',['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX'] , range(2000,2002))
dffagric
elec_access='EG.ELC.RNWX.KH'
countries=['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX']
dff=wb.data.DataFrame('EG.ELC.RNWX.KH',['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX'] , range(2000,2002))
dff
bus_ease='IC.BUS.EASE.XQ'
countriesbus=['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX']
dffbus=wb.data.DataFrame('IC.BUS.EASE.XQ',['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX'] , range(2000,2002))
dffbus
co2emis='EN.ATM.CO2E.LF.KT'
countriesco2emis=['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX']
dffco2emis=wb.data.DataFrame('EN.ATM.CO2E.LF.KT',['ARG', 'BRA', 'CHE', 'CMR', 'DNK', 'MEX'] , range(2000,2002))
dffco2emis
dfmerge=dffco2emis.merge(dffagric, on='economy'  )
dfmerge
dfmerge2=dfmerge.merge(dff, on='economy'  )
dfmerge2
###heatmap creation 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sb
plt.pcolor(dfmerge2)
plt.show()
print(dfmerge2.corr())
dataplot=sb.heatmap(dfmerge2.corr(), cmap="YlGnBu", annot=True)
plt.show()
dffagric2=dffagric.transpose()
dffagric2.plot()

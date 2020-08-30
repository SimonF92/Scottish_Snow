import plotly.graph_objects as go
import pandas as pd
import numpy as np

lat=[56.952699946355196,
     57.101050380315705,
     57.15181364614503,
    56.798726195708845,
    57.04445012102833,
    56.84103107673674,
    57.36876671642763,
    56.56194982435603,
     56.535851327970605,
     56.64077849723661
    ]
lon=[-4.57494735455839,
     -3.665306567272637,
     -3.6341500299749896,
    -4.951683281979058,
     -3.5009980223549064,
    -4.491527081409004,
     -5.095174310845323,
    -4.21819925395539,
    -4.645657540240791,
     -4.16107177734375
    ]
name=['Creag_Meagaidh',
      'Coire_Domhain',
      'Ciste_Mhearad',
     'Nevis_Gullys',
     'Beinn_a_Bhuird',
     'Gael_Charn',
     'An_Riabhachan',
     'An_Stuc',
     'Beinn_Mhanach',
      'Coire_Cruach_Sneachda'
     ]

size2020=[3.415,
     7.88,
     2.83,
     10.1,
      5.18,
      6.47,
     4.22,
     1.09,
      2.28,
    2.83]
size2017=[1.52,
     1.11,
     0.578,
     3.29,
      1.01,
      0.25,
     0.89,
     0.022,
      0.16,
         0.189]
size2018=[2.13,
     1.59,
     1.79,
     6.32,
      1.86,
      2.28,
     2.84,
     0.28,
      1.69,
         1.52]
size2019=[0.855,
     3.49,
     1.54,
     3.87,
      2.12,
      0.67,
     1.20,
     0.94,
      0.29,
         1.33]



coords = pd.DataFrame(list(zip(lat, lon,name,size2020,size2017,size2018,size2019)), 
                   columns =['Latitude', 'Longitude','Snowpatch','Area2020','Area2017','Area2018','Area2019']) 


coords['Longitude_2019']=coords['Longitude']-0.06
coords['Longitude_2018']=coords['Longitude_2019']-0.06
coords['Longitude_2017']=coords['Longitude_2018']-0.06


coords['normalised2017']=np.log10(coords['Area2017']/coords['Area2017'])+1
coords['normalised2018']=np.log10(coords['Area2018']/coords['Area2017'])+1                               
coords['normalised2019']=np.log10(coords['Area2019']/coords['Area2017'])+1
coords['normalised2020']=np.log10(coords['Area2020']/coords['Area2017'])+1

n2017=coords.normalised2017.tolist()
n2018=coords.normalised2018.tolist()
n2019=coords.normalised2019.tolist()
n2020=coords.normalised2020.tolist()
n2020

normtuple=[]

for x in range (0,10):

    list1= n2017[x],n2018[x],n2019[x],n2020[x]
    normlist=[float(i)/max(list1) for i in list1]
    normtuple += (normlist,)
    
normtuple
normvals = pd.DataFrame.from_records(normtuple, columns =['Normalised2017', 'Normalised2018', 'Normalised2019', 'Normalised2020']) 

finalmap=pd.concat([coords, normvals], axis=1)

finalmap2 = finalmap.append({'Latitude':1, 'Longitude':2, 'Snowpatch':'Scale','Area2020':10
                            ,'Area2017':10, 'Area2018':10, 'Area2019':10, 'Longitude_2019':1,
                            'Longitude_2018':1,'Longitude_2017':1,'normalised2017':1
                            ,'normalised2018':1,'normalised2019':1,'normalised2020':1
                            ,'Normalised2017':1
                            ,'Normalised2018':1,'Normalised2019':1,'Normalised2020':1}, ignore_index=True)

finalmap2 = finalmap2.append({'Latitude':2, 'Longitude':3, 'Snowpatch':'Scale','Area2020':10
                            ,'Area2017':10, 'Area2018':10, 'Area2019':10, 'Longitude_2019':1,
                            'Longitude_2018':1,'Longitude_2017':1,'normalised2017':0
                            ,'normalised2018':0,'normalised2019':0,'normalised2020':0
                            ,'Normalised2017':0
                            ,'Normalised2018':0,'Normalised2019':0,'Normalised2020':0}, ignore_index=True)



year2017=['2017','2017','2017','2017']
year2018=['2018','2018','2018','2018']
year2019=['2019','2019','2019','2019']
year2020=['2020','2020','2020','2020']

latitude=[56.1394982435603,56.1394982435603,56.1394982435603,56.1394982435603]
longitude=[-2.8200000567272637,-2.8200000567272637,-2.8200000567272637,-2.8200000567272637,]

yearscale = pd.DataFrame(list(zip(year2017,year2018, year2019, year2020, latitude,longitude)), 
                   columns =['Year2017','Year2018','Year2019','Year2020','Latitude', 'Longitude']) 


yearscale['Longitude_2019']=yearscale['Longitude']-0.15
yearscale['Longitude_2018']=yearscale['Longitude_2019']-0.15
yearscale['Longitude_2017']=yearscale['Longitude_2018']-0.15

yearscale




mapbox_access_token = 'pk.eyJ1Ijoic2ltb25mOTIiLCJhIjoiY2tlZWdvMTNjMTJmcTJ0cDc5MGZqdjJpaCJ9.EdEy9ghDy1al0NEeKSlGtA'

meanlat=np.mean(finalmap['Latitude'].values.tolist())
meanlon=np.mean(finalmap['Longitude'].values.tolist())

data = go.Scattermapbox(lat=list(finalmap2['Latitude']),
                        lon=list(finalmap2['Longitude']),
                        mode='markers+text',
                        marker=dict(cmax=1,cmin=0.3,
                            
                            
                            size=15, color=finalmap2['Normalised2020'],colorscale=[[0, 'yellow'],[0.6, 'red'],
                        [1, 'blue']],showscale=True),
                        textposition='middle right',
                        textfont=dict(size=12, color='black'),
                        text=finalmap2['Snowpatch'])

data_2 = go.Scattermapbox(lat=list(finalmap2['Latitude']),
                        lon=list(finalmap2['Longitude_2019']),
                        mode='markers',
                        marker=dict(cmax=1,cmin=0.3,
                            
                            
                            size=15, color=finalmap2['Normalised2019'],colorscale=[[0, 'yellow'],[0.6, 'red'],
                        [1, 'blue']],),
                        )


data_3 = go.Scattermapbox(lat=list(finalmap2['Latitude']),
                        lon=list(finalmap2['Longitude_2018']),
                        mode='markers',
                        marker=dict(cmax=1,cmin=0.3,
                            
                            
                            size=15, color=finalmap2['Normalised2018'],colorscale=[[0, 'yellow'],[0.6, 'red'],
                        [1, 'blue']],),
                        )

data_4 = go.Scattermapbox(lat=list(finalmap2['Latitude']),
                        lon=list(finalmap2['Longitude_2017']),
                        mode='markers',
                        marker=dict(cmax=1,cmin=0.3,
                            
                            
                            size=15, color=finalmap2['Normalised2017'],colorscale=[[0, 'yellow'],[0.6, 'red'],
                        [1, 'blue']],),
                        )

data_5 = go.Scattermapbox(lat=list(yearscale['Latitude']),
                        lon=list(yearscale['Longitude_2017']),
                        mode='markers+text',
                        marker=dict(size=20,color='Black'),
                        textposition='bottom center',
                        textfont=dict(size=13, color='black'),
                        text=yearscale['Year2017'])
data_6 = go.Scattermapbox(lat=list(yearscale['Latitude']),
                        lon=list(yearscale['Longitude_2018']),
                        mode='markers+text',
                        marker=dict(size=20,color='Black'),
                        textposition='bottom center',
                        textfont=dict(size=13, color='black'),
                        text=yearscale['Year2018'])
data_7 = go.Scattermapbox(lat=list(yearscale['Latitude']),
                        lon=list(yearscale['Longitude_2019']),
                        mode='markers+text',
                        marker=dict(size=20,color='Black'),
                        textposition='bottom center',
                        textfont=dict(size=13, color='black'),
                        text=yearscale['Year2019'])
data_8 = go.Scattermapbox(lat=list(yearscale['Latitude']),
                        lon=list(yearscale['Longitude']),
                        mode='markers+text',
                        marker=dict(size=20,color='Black'),
                        textposition='bottom center',
                        textfont=dict(size=13, color='black'),
                        text=yearscale['Year2020'])


layout = go.Layout(
    title='',
    width=1000,
    height=1000,
    showlegend=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=meanlat,
            lon=meanlon
        ),
        pitch=0,
        zoom=7.5
    ),
)


fig = go.Figure(data=[data,data_2,data_3,data_4,data_5,data_6,data_7,data_8], layout=layout)
fig.update_layout(showlegend=False)
fig.show()
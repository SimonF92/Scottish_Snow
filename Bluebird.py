#---------------------------------BLUEBIRD------------------------------------#


import cv2
import numpy as np
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta, date
from selenium import webdriver
import time
import seaborn as sns; sns.set()
from numpy import array, linspace
from scipy.interpolate import interp1d
from imageai.Prediction.Custom import CustomImagePrediction
from sklearn import metrics
from numpy import trapz
from scipy.integrate import simps
from scipy.interpolate import UnivariateSpline

lat=None
lng=None

area_under_curve=[]
area_under_curve2=[]



year_range=[2017,2018,2019,2020]
#snowpatch_name='Creag_Meagaidh'
#url='https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=56.952699946355196&lng=-4.57494735455839&zoom=16&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=99&gain=1.3&gamma=0.7&time=2017-12-01%7C2018-06-05&atmFilter=&showDates=false'
#snowpatch_name='Coire_Domhain'
#url='https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=57.101050380315705&lng=-3.665306567272637&zoom=16&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2020-02-01%7C2020-08-15&atmFilter=&showDates=false'
#snowpatch_name='Ciste_Mhearad'
#url='https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=57.12181364614503&lng=-3.6341500299749896&zoom=16&preset=92_NDWI&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2020-02-01%7C2020-08-17&atmFilter=&showDates=false'
#snowpatch_name='Nevis_Gullys'
#url='https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=56.798726195708845&lng=-4.951683281979058&zoom=16&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=100&gain=1.0&gamma=1.0&time=2016-12-01%7C2017-06-20&atmFilter=&showDates=false'
#snowpatch_name='Beinn_a_Bhuird'
#url='https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=57.07445012102833&lng=-3.5009980223549064&zoom=16&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=99&gain=1.3&gamma=0.7&time=2017-12-01%7C2018-06-30&atmFilter=&showDates=false'
#snowpatch_name='Gael_Charn'
#url='https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=56.84103107673674&lng=-4.491527081409004&zoom=16&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=99&gain=1.3&gamma=0.7&time=2019-11-01%7C2020-05-30&atmFilter=&showDates=false'
snowpatch_name='An_Riabhachan'
url='https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=57.36876671642763&lng=-5.095174310845323&zoom=16&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=99&gain=1.3&gamma=0.7&time=2017-12-01%7C2018-06-05&atmFilter=&showDates=false'

x=url.split('=')
lat=x[2]
lng=x[3]




final=None
final_extrapolated=None


prediction = CustomImagePrediction()



for year in year_range:
    
    
    stringyear=str(year)
    
    dir = os.path.join('Area_Under_Curve/')
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    dir = os.path.join(snowpatch_name)
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    dir = os.path.join(snowpatch_name + '/Bluebird/')
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    dir = os.path.join(snowpatch_name + '/Bluebird/' + stringyear + '/')
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    directory= snowpatch_name + '/Bluebird/' + stringyear + '/'
        
    dir = os.path.join(snowpatch_name + '/Bluebird/' + stringyear + '/' + "Cropped/")
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    dir = os.path.join(snowpatch_name + '/Bluebird/' + stringyear + '/' + "Cropped/Masks/")
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    dir = os.path.join(snowpatch_name + '/Bluebird/' + stringyear + '/' + "Cropped/Masks/MachineLearning")
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    area_under_directory='Area_Under_Curve/'
    cropped_directory= snowpatch_name + '/Bluebird/' + stringyear + '/' + "Cropped/"
    masked_directory= snowpatch_name + '/Bluebird/' + stringyear + '/' + "Cropped/Masks/"
    machinelearning_directory= snowpatch_name + '/Bluebird/' + stringyear + '/' + "Cropped/Masks//MachineLearning/"
        
   
    
    
    '''
    

    dates=[]

    def daterange(date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + timedelta(n)
            
    from datetime import date

    start_dt = date(year, 4, 1)
    #end_dt = date(year, 5, 5)
    end_dt = date(year, 9, 30)
    for dt in daterange(start_dt, end_dt):
        dates.append(dt.strftime("%Y-%m-%d"))


    class Patch:

        def __init__(self, date):
            self.date= date
        def getscreen(date):
            DRIVER = 'chromedriver'
            driver = webdriver.Chrome('chromedriver.exe')
            #driver.get('https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=57.12112444253996&lng=-3.632369040569756&zoom=16&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=90&gain=1.0&gamma=1.0&time=2016-11-01%7C' + date + '&atmFilter=&showDates=false')
            driver.get('https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat='+ lat + '=' + lng + '=16&preset=CUSTOM&layers=B01,B04,B11&maxcc=90&gain=1.0&gamma=1.0&time=2016-11-01%7C' + date + '&atmFilter=&showDates=false&evalscript=cmV0dXJuIFtCMDEqMi41LEIwNCoyLjUsQjExKjIuNV0%3D')
            time.sleep(10) 
            screenshot = driver.save_screenshot(directory + date + '.png')
            driver.quit()

    

    for date in dates:
        Patch.getscreen(date)
        
    
      
    


    directory = directory

    for filename in os.listdir(directory):
        identity=str(filename)
        identity=identity.strip('.png')
        #print(identity)
        if filename != 'Cropped':
            Img = Image.open(directory + filename)
            Img2=Img.crop((600,600,1300,1300))
            Img2
            Img2= Img2.save(cropped_directory + identity + ".png") 
        else:
            pass

   
    '''


    directory = cropped_directory

    dates=[]
    areas=[]
    
    extrapol_area=[]
    extrapol_delta=range(0,175,1)

    for filename in os.listdir(directory):
        if filename != 'Masks':
            identity=str(filename)
            identity=identity.strip('.png')
            
            

            prediction.setModelTypeAsResNet()
            prediction.setModelPath("Snow_ML_3/models/model_ex-047_acc-0.975000.h5")
            prediction.setJsonPath("Snow_ML_3/json/model_class.json")
            prediction.loadModel(num_objects=2)

            predictions, probabilities = prediction.predictImage(directory + filename, result_count=3)

            print(predictions , ":" , probabilities)

            if predictions[0] == 'Snow':



                img = cv2.imread(directory + filename)


                if filename != 'Masks':

                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    lower_range = np.array([20, 30, 0],np.uint8)
                    upper_range = np.array([90, 255,255],np.uint8)
                    mask = cv2.inRange(hsv, lower_range, upper_range)
                    #cv2.imwrite(masked_directory+identity+'.png', mask)
                    cv2.imwrite(machinelearning_directory+snowpatch_name+identity+'AI_sorted.png', img)
                    snow = cv2.countNonZero(mask)
                    areas.append(snow)
                    dates.append(identity)

                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    lower_range = np.array([100, 30, 0],np.uint8)
                    upper_range = np.array([140, 255,255],np.uint8)
                    bluemask = cv2.inRange(hsv, lower_range, upper_range)
                    detectground= cv2.countNonZero(bluemask)
                    #cv2.imwrite(masked_directory+identity+'_blue.png', bluemask)

                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    lower_range = np.array([0, 0, 0])
                    upper_range = np.array([360, 30,255])
                    cloudmask = cv2.inRange(hsv, lower_range, upper_range)
                    detectcloudcover= cv2.countNonZero(cloudmask)
                    #cv2.imwrite(masked_directory+identity+'_clouds.png', cloudmask)

                    

                else:
                    pass

            else:
                pass
        else:
            pass

    df = pd.DataFrame(list(zip(dates, areas)), 
                   columns =['Dates', 'Areas']) 

    
    df=df.drop_duplicates(subset=['Areas'])
    
    
    
    df['Diff']=df['Areas'].diff()
    correction=df.head(1)
    df=df.where(df.Diff<0)
    df=df.dropna()
    
    df=pd.concat([correction,df])
    
    '''
    
    
    df['Diff_2']=df['Areas'].diff()
    correction=df.head(1)
    df=df.where(df['Diff_2']<0)
    df=df.dropna()
    
    df=pd.concat([correction,df])
    
    df['Diff_3']=df['Areas'].diff()
    correction=df.head(1)
    df=df.where(df['Diff_3']<0)
    df=df.dropna()
    
    df=pd.concat([correction,df])
    
    df['Diff_4']=df['Areas'].diff()
    correction=df.head(1)
    df=df.where(df['Diff_4']<0)
    df=df.dropna()
    
    df=pd.concat([correction,df])
    
    df['Diff_5']=df['Areas'].diff()
    correction=df.head(1)
    df=df.where(df['Diff_5']<0)
    df=df.dropna()
    
    df=pd.concat([correction,df])
    
    '''
   
    
   
    from datetime import date

    df['Year']=stringyear
    df["Datetime"]= pd.to_datetime(df["Dates"]) 
    df['year'] = pd.DatetimeIndex(df["Datetime"]).year
    df['month'] = pd.DatetimeIndex(df["Datetime"]).month
    df['day'] = pd.DatetimeIndex(df["Datetime"]).day
    df['daymonth'] = df['Dates'].str[5:]
    df['Snowpatch']=snowpatch_name
    df['Approximate Area (m^2)']=np.sqrt(df['Areas']/1.15)

    d0 = date(year, 4, 1)

    year=list(df['year'])
    month=list(df['month'])
    day=list(df['day'])

    datesclean=[]

    for x, y, z in zip(year, month, day):
        holder=date(x, y, z)
        datesclean.append(holder)

    datesdelta=[]

    for item in datesclean:
        delta= item - d0
        datesdelta.append(delta.days)

    datesdelta

    df['Delta']= datesdelta
    df
    
    y=df['Approximate Area (m^2)'].values.tolist()
    x=df['Delta'].values.tolist()
    
    y=df['Approximate Area (m^2)'].values.tolist()


    model = np.poly1d(np.polyfit(x, y, 2))
    xaxis=range(0,175,1)
    yaxis=model(xaxis)
    
    extrapolated=pd.DataFrame(list(zip(xaxis, yaxis)), 
                   columns =['Delta', 'Areas']) 
    extrapolated['Year']=stringyear
    extrapolated['Snowpatch']=snowpatch_name
    
    extrapolated=extrapolated.where(extrapolated['Areas']>0)
    extrapolated=extrapolated.dropna()
    
    extrapolated['Diff']=extrapolated['Areas'].diff()
    correction=extrapolated.head(1)
    extrapolated=extrapolated.where(extrapolated['Diff']<0)
    extrapolated=extrapolated.dropna()    
    extrapolated=pd.concat([correction,extrapolated])


    
    
    yearly_area=trapz(yaxis,xaxis)
    area_under_curve.append(yearly_area)
    
    yearly_area_2=simps(yaxis,xaxis)
    area_under_curve2.append(yearly_area_2)
    
    
    
    
    
    if year == 2016:
        final=df
        
    else:
        final=pd.concat([final,df])
        
    if year == 2016:
        final_extrapolated=extrapolated
        
    else:
        final_extrapolated=pd.concat([final_extrapolated,extrapolated])
        

        

AUC=pd.DataFrame(area_under_curve2,columns =['AUC'])
AUC['Year']=year_range
AUC['Snow_Patch']=snowpatch_name
AUC.to_csv(area_under_directory+snowpatch_name+'.csv',index=False)

final.to_csv(snowpatch_name + '/Bluebird/' +snowpatch_name+'.csv',index=False)

    
    
lat=lat.strip('&lng')
lng=lng.strip('&zoom')

coords= 'lat: ' + lat + ' , lng: ' + lng

plt.figure(figsize=(14, 9))


sns.set(font_scale=1.2)
sns.set_style("whitegrid")
ax = sns.lineplot(x="Delta", y='Areas', data=final_extrapolated,hue="Year",legend="full", palette="deep")
ax.lines[0].set_linestyle(":")
ax.lines[1].set_linestyle(":")
ax.lines[2].set_linestyle(":")
ax.lines[3].set_linestyle(":")
ax.lines[4].set_linestyle(":")
ax = sns.lineplot(x="Delta", y='Approximate Area (m^2)', data=final,hue="year",legend=None, palette="deep")
ax = sns.scatterplot(x="Delta", y='Approximate Area (m^2)', data=final,hue="year",legend=None, palette="deep")

ax.set_xticks([0,30,60,90,120,150])
ax.set_xticklabels(['April','May','June','July','August','September'])

ax.set(xlabel='Month (Spring-Summer)', ylabel='Approximate Area (m^2)')

plt.title(coords,fontsize=12)
plt.suptitle(snowpatch_name, fontsize=20)


plt.savefig(snowpatch_name + '/Bluebird/' +snowpatch_name + '.png')
        
   
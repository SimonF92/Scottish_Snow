#---------------------------------BLUEBIRD------------------------------------#


import os
from datetime import timedelta, date
from selenium import webdriver
import time




lat=None
lng=None


url="https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=69.20038412441527&lng=-49.45838928222656&zoom=11&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2020-04-01%7C2020-10-06&atmFilter=&showDates=false"
feature_name="Jakobshavn_Glacier"

x=url.split('=')
lat=x[2]
lng=x[3]

zoom=url.split('zoom')
zoom=zoom[1]
zoom=zoom.lstrip('=')
zoom=zoom[:2]




year_range=[2017,2018,2019,2020]
for year in year_range:
    
    
    stringyear=str(year)
    

    dir = os.path.join(feature_name)
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    dir = os.path.join(feature_name + '/Bluebird/')
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    dir = os.path.join(feature_name + '/Bluebird/' + stringyear + '/')
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir = os.path.join(feature_name + '/Bluebird/' + stringyear + '/' + "Cropped/")
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    directory= feature_name + '/Bluebird/' + stringyear + '/'

    cropped_directory= feature_name + '/Bluebird/' + stringyear + '/' + "Cropped/"
        
 
 

    dates=[]

    def daterange(date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + timedelta(n)
            
    from datetime import date

    start_dt = date(year, 4, 1)
    end_dt = date(year, 9, 30)
    for dt in daterange(start_dt, end_dt):
        dates.append(dt.strftime("%Y-%m-%d"))


  
        
    class Patch:

        def __init__(self, date):
            self.date= date
        def getscreen(date):
            DRIVER = 'chromedriver'
            driver = webdriver.Chrome('chromedriver.exe')           
            driver.get('https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat='+ lat + '=' + lng + '&zoom=' + zoom + '&preset=1-NATURAL-COLOR&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2016-11-01%7C' + date + '&atmFilter=&showDates=false&evalscript=cmV0dXJuIFtCMDEqMi41LEIwNCoyLjUsQjExKjIuNV0%3D')
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
        



    

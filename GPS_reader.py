import matplotlib.pyplot as plt
from datetime import datetime
from geopy import distance
from math import sqrt, floor
import numpy as np
import pandas as pd

###########################################    
# the data is writen as follow:           #
#    - 8 bytes: size of the header        #
#    - 34 bytes : header                  #
#    - 8 bytes : data size                #
#    - 48 bytes : data: - time stamp      #
#                       - latitude        #
#                       - longitude       #
#                       - altitude        #
#                       - velocity        #
#                       - heading         #
###########################################

def Process_GPS_data(file,count):
        # ignore the header
    with open(file,'br') as f:
        header_size=np.frombuffer(f.read(8),dtype='int64')
        hs=header_size.astype(np.int)
        header=np.frombuffer(f.read(34),dtype='int8')
        #Get the data 
        data_length=[0]
        file1 = open("media/801GPS/14/801GPS-14.txt","a+") 
        while len(data_length)>0:

            count+=1
            data_length=np.frombuffer(f.read(8),dtype='int64')
            if(len(data_length>0)):
                time_stamp=np.frombuffer(f.read(8),dtype='int64')[0]-3600000000*4 
                time_stamps_str=pd.to_datetime(time_stamp,unit='us')
                lat=np.frombuffer(f.read(8),dtype='float64')[0]
                lng=np.frombuffer(f.read(8),dtype='float64')[0]
                altitude=np.frombuffer(f.read(8),dtype='float64')[0]
                velocity=np.frombuffer(f.read(8),dtype='float64')[0]
                heading=np.frombuffer(f.read(8),dtype='float64')[0]
                
                data_string= str(count)+' : '+str(time_stamps_str)+' => '+ 'lat :'+str(lat)+' ,long :'+str(lng)+' ,alt :'+str(altitude)+', vel :'+str(velocity)+' ,heading :'+str(heading)
                data_txt=str(time_stamps_str)+'$'+str(lat)+'$'+str(lng)+'$'+str(altitude)+'$'+str(velocity)+'$'+str(heading)+'\n'
                file1.writelines(data_txt)
                print(data_string)
    file1.close() 
    return count
        

if __name__=="__main__":

    count=0
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-00-43 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-05-39 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-10-34 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-15-30 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-20-25 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-25-21 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-30-17 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-35-12 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-40-08 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-45-03 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-49-59 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-54-54 PixHawk4.gps',count)
    count=Process_GPS_data('media/801GPS/14/2019-06-17 14-59-50 PixHawk4.gps',count)
  
    

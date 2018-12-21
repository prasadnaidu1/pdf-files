file_access = open('geocode_health_centre.csv','r')
file_raw_data = file_access.read() # the whole data in the file is stored in file_raw_data
file_data_lines_list = file_raw_data.split("\n") #splitted the data by new line character
health_center = { }
for each_line in range(len(file_data_lines_list)-1):
    file_each_line_data = file_data_lines_list[each_line].split(',')  #each line again splitted with ','
    key_dist = file_each_line_data[1]
    if(file_each_line_data[1] not in health_center.keys()):
        
        health_center[file_each_line_data[1]] = []
        health_center[key_dist].append([x for x in file_each_line_data])
    else:
        health_center[key_dist].append([y for y in file_each_line_data])

#print(health_center['Srikakulam'])

pincode_access = open('All_India_pincode_data_18082017.csv','r')
pincode_raw_data = pincode_access.read()
pincode_lines = pincode_raw_data.split('\n')
pincode_dict = {}
for i in range(1,len(pincode_lines)-1):
    try:
        li = []
        pincode_details = pincode_lines[i].split(',')
        if pincode_details[1] not in pincode_dict.keys():
            pincode_dict[pincode_details[1]] = []
            li=[pincode_details[7],pincode_details[8],pincode_details[9]]
            pincode_dict[pincode_details[1]].append(li)
        else:
            li = [pincode_details[7],pincode_details[8],pincode_details[9]]
            pincode_dict[pincode_details[1]].append(li)
    except:
        continue
#print(pincode_dict)
try:
    user_input_pincode = input("Enter pincode: ")
    pincode_data_list = pincode_dict[user_input_pincode]
    print(pincode_data_list)
    #dist_hospital_list = health_center[pincode_data_list[1]]
    #print(dist_hospital_list)
    #print(health_center[pincode_data_list[1]])
    #for item in pincode_data_list:
        
    
    
    #print(pincode_data_list)
except Exception as inst:
    print(inst,type(inst))
#len(pincode_lines)-1

'''
from math import radians, sin, cos, acos
import os

#method to calculate distance between source and destination which return the distance between two points
def distance_two_latlongs(slatlon,dlatlon1):
    dist = 6371.01 * acos(sin(slatlon[0])*sin(dlatlon1[0]) + cos(slatlon[0])*cos(dlatlon1[0])*cos(slatlon[1] - dlatlon1[1]))
    return dist
distance_list = []
health_center = { }

#External file accessing and storing the data in a dictionary 
file_access = open('geocode_health_centre.csv','r')
file_raw_data = file_access.read() # the whole data in the file is stored in file_raw_data
file_data_lines_list = file_raw_data.split("\n") #splitted the data by new line character
for each_line in range(len(file_data_lines_list)-1):
    file_each_line_data = file_data_lines_list[each_line].split(',')  #each line again splitted with ','
    key_dist = file_each_line_data[1]
    li_temp =[]
    
    if(file_each_line_data[1] not in health_center.keys()):
        
        health_center[file_each_line_data[1]] = []
        li_temp.append(file_each_line_data[4])
        li_temp.append(file_each_line_data[6])
        li_temp.append(file_each_line_data[7])
        health_center[key_dist].append(li_temp)       
    else:
        
        li_temp.append(file_each_line_data[4])
        li_temp.append(file_each_line_data[6])
        li_temp.append(file_each_line_data[7])
        health_center[key_dist].append(li_temp)
#User interaction part
try:
    dist_name = input("Enter district name: ").title()
    #print(dist_name)
    
    if(dist_name in health_center.keys()):
        latitude = float(input("Enter Latitude: "))
        longitude = float(input("Enter Longitude: "))
        slatlon = [latitude,longitude]
        hospital_list = health_center[dist_name]
        for i in range(len(hospital_list)):
            try:
                lat = float(hospital_list[i][1])
                lon = float(hospital_list[i][2])
            except ValueError:
                continue
            dlatlon1 = [lat,lon]
            distance = distance_two_latlongs(slatlon,dlatlon1)
            distance_list.append(distance)
        
        minimum = min(distance_list)
        
        min_index = distance_list.index(minimum)
        #print(len(distance_list),minimum,min_index)
        print("Nearest Hospital: ",hospital_list[min_index][0],hospital_list[min_index][1],hospital_list[min_index][2])
    else:
        print("district name not found")
    #print(hospital_list[i])
except Exception as inst:
    print("Exception: ",type(inst),inst)
else:
    print("Thank you")
finally:
    file_access.close()
#print(health_center['Vishakapatnam'])
'''
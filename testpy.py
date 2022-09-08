mile = 1.69
time_m = 42
time_s = 42
distance_m= 10/mile
speed=(time_m*60+time_s)/distance_m
speed_m=int(speed // 60)
speed_s= speed % 60
time_in_hour=(42*60+60)/3600
print ("distance = ", distance_m)
print ("speed = ", speed)
print ("speed in minutes and seconds = ", speed_m, "m and ", speed_s, "seconds per mile")
print ("the average speed in miles per hour is ", distance_m/time_in_hour, "miles per hour")



#How many seconds are there in 42 minutes 42 secons?
secconds = ((42 * 60) + 42) * 60
print("There are " + str(secconds) + " seconds in " + "42 minutes 42 seconds" )


#miles in 10KM, if 1M = 1.61km
xm = 10 / 1.61
print("There are " + str(xm) + " miles in 10KM" )

#If you run a 10Km race in 42minutes 42seconds, 
# what is your average pace (time per mile in minutes and seconds)
#What is your average speed in miles per hour?

hour = secconds / 3600
#Find AvgPace & AvgSpeed
AvgPace = secconds / xm
AvgSpeed = xm / hour
print("Your Average Pace is " + str(AvgPace))
print("Your Average Speed is " + str(AvgSpeed))
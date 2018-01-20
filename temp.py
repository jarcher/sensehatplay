from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
tempf = (temp * 1.8) + 32
print("Temperature: %s C" % temp)
print("Temperature: %s F" % tempf) 

# alternatives
print(sense.temp)
print(tempf)


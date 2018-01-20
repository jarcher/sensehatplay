from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
red = (255, 0, 0)
sense.show_message("Red Hat IoT Pilot for XOM!", text_colour=red)
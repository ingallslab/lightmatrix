"""
This program maps out the config file to be ordered in the form of (r,g,b)

it remaps the original scheme to instead have it so that
each slot in the matrix to be arranged as such:

	 R
   G   B 

it then takes the settings in rgbvalues.in and writes it into config.in
this loses purpose if other LED's are used.
"""

def use_rgb():
	light_settings=open("RGBvalues.in","r")
	config=open("config.in","w")
	config.write("slot, l1, l2, l3")
	lines = light_settings.readlines()
	lines.pop(0)
	newlines = []
	red = []
	green = []
	blue = []
	for i in lines:
		 newlines.append(i.rstrip('\n').split(","))
	for i in range(len(newlines)):
		red.append(newlines[i][1])
		green.append(newlines[i][2])
		blue.append(newlines[i][3])
	config.write("\n")
	config.write("0, %s, %s, %s \n" % (red[0],green[0],blue[0]))
	config.write("1, %s, %s, %s \n" % (blue[1],red[1],green[1]))
	config.write("2, %s, %s, %s \n" % (blue[2],red[2],green[2]))
	config.write("3, %s, %s, %s \n" % (green[3],blue[3],red[3]))
	config.write("4, %s, %s, %s \n" % (blue[4],red[4],green[4]))
	config.write("5, %s, %s, %s \n" % (green[5],blue[5],red[5]))
	config.write("6, %s, %s, %s \n" % (green[6],blue[6],red[6]))
	config.write("7, %s, %s, %s \n" % (green[7],blue[7],red[7]))
	config.write("8, %s, %s, %s \n" % (blue[8],red[8],green[8]))
	config.write("9, %s, %s, %s \n" % (blue[9],red[9],green[9]))
	config.write("10, %s, %s, %s \n" % (blue[10],red[10],green[10]))
	config.write("11, %s, %s, %s \n" % (blue[11],green[11],red[11]))
	config.write("12, %s, %s, %s \n" % (blue[12],red[12],green[12]))
	config.write("13, %s, %s, %s \n" % (green[13],blue[13],red[13]))
	config.write("14, %s, %s, %s \n" % (green[14],blue[14],red[14]))
	config.write("15, %s, %s, %s \n" % (green[15],blue[15],red[15]))
	light_settings.close()
	config.close() 

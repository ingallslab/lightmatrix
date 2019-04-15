import csv, sys, serial, time, sched

class LightArray:
    # class used to configure the light array built for the Brian Ingalls lab
    def __init__(self, serial_port="/dev/ttyACM0", filename="config.in"):
        self.serial_port = serial_port
        # light settings will be kept as a 3 tuple ranging from 0 to 4095
        self.light_settings = [(0, 0 ,0)] * 16
        self.settings_from_csv(filename)
        self.sync_arduino()
        self.s = sched.scheduler(time.time, time.sleep)
    
    def update_light_slot(self, num, new_values):
        # num -> int
        # new_values -> (x, y, z) : x, y, z == int and 0 <= x,y,z <= 4095
        if 0 <= num and num < 16:
            for i in new_values:
                if 0<= i <4096:
                    pass
                else:
                    raise Exception('ERROR: unacceptable light values. Values should be between 0 and 4095, received {}'.format(i))
            self.light_settings[num] = new_values
        else:
            raise Exception('ERROR: unacceptable light slot. Value of light slot should be between 0 and 16. received {}'.format(num))
    
    def update_and_sync(self, num, new_values):
        # num -> int
        # new_values -> (x, y, z) : x, y, z == int and 0 <= x,y,z <= 4095
        # updates the pwm values of LED's for a given tube and syncs with arduino
        self.update_light_slot(num, new_values)
        self.sync_arduino()

    def get_tube(self, tube):
        # tube -> x : 1 <= x < 16
        # prints the LED values of the selected tube.
        print(self.light_settings[tube])
        return self.light_settings[tube]

    def settings_from_csv(self, filename):
        # filename -> string
        # filename is the name of a file on the path
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                slot = 0
                for line in reader:
                    if slot != 0:
                        light_tuple = (int(line[1]), int(line[2]), int(line[3]))
                        self.update_light_slot(slot - 1, light_tuple)
                    slot += 1
        except:
            raise Exception("ERROR: could not properly parse out csv. Please check for errors")

    def sync_arduino(self):
        # sends current information stored in memory to the arduino via serial communication
        ard = serial.Serial()
        ard.baudrate = 9600
        ard.port = self.serial_port
        if ard.is_open == False:
            ard.open()
        ard.readline()
        print("Uploading to arduino")
        # take all settings from light_settings and convert them to a string and send to arduino
        for i in range(len(self.light_settings)):
            slot = self.light_settings[i]
            instr = bytes("<{},{},{},{}>".format(i, slot[0], slot[1], slot[2]), 'utf-8')
            ard.write(instr)
            # print(instr)
            ard.readline()
        print("upload complete")
        ard.close()

    def run_open_loop(self, filenames):
        # first will read in file named filename
        # file will have rows consisting of the following format
        # time, tube value
        # so lets construct a list of tuples (x,y) where 
        # x_i = 0 if time == 0
        # x_i == time - x_i-1 if time > 0
        # y = value
        for filename in filenames:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                line_num = 0
                priority = 1
                for line in reader:
                    print(line)
                    if line_num != 0:
                        self.s.enter(int(line[0]), 
                                priority, 
                                self.update_and_sync, 
                                (int(line[1]), (int(line[2]), int(line[3]), int(line[4]))))
                        priority += 1 # so that priority is never equal and one always goes first
                    line_num += 1
                print(self.s.queue)

        self.s.run()


    




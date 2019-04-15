# Ingalls Lab Light Matrix

This system was created by Cody Receno and Will Forrest to deliver light to optogenitically controlled systems.

The light matrix allows light delivery of up to 3 LED's simultaneously.

## Configuration

There are two ways to configure the light matrix. The first is to modify the `config.in` file directly. `config.in` is a csv file where the `slot` field represents the position in the light matrix. The `l1`, `l2`, `l3` fields represent the LED's that belong to the slot. They correspond to the numbers printed on the PCB in ascending order (`slot` * 3 + `1/2/3`).

The second way to configure the light matrix only works if the LED's used are only red green and blue and are arranged as followed

```
    R
  G   B

```

If this is the case then `rgbvalues.in` can be modified where `slot` is also the position in the light matrix and the `red`, `green`, `blue` fields correspond to the red, green, and blue LED's

## Usage

### Running the system 

To use this system the user will need to plug their device into the arduino then in the repository director execute the command `./run.sh`

### Single Level Light Control

For single level light control the `main.py` script will look as followed.

```python
import lightarray

light_array = lightarray.LightArray() # initialize a LightArray object
```

### Arduino Serial Ports

The serial port may have to be adjusted based on the system that the code is run on. For linux, serial port `/dev/ttyACM0` is used and no changes are necessary. Otherwise information regarding the serial port is dependent on the users device.

Users may have to be concerned with permissions for the serial port.If access to the serial port is denied, it can be accessed by running:

`sudo chmod a+rw /dev/ttyACM0`


### Open Loop Control

For open loop control a csv file consisting of the transition times and values needs to be created

```
time,tube,l1,l2,l3
0, 0, 4095, 4095, 0
10200, 0, 0, 4095, 0

```

It is similar to a `config.in` file with the addition of a time field.
This time field represents the delay in seconds in which the values should change.

After these files are created a line containing all the open loop control files to be used will need to be added as shown below.

```python
import lightarray

light_array = lightarray.LightArray()

filenames = [] # a list of filenames with the open loop control format.

light_array.run_open_loop(filenames)
```






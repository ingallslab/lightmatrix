# WIP

everything here will be updated soon with more viable information

\- Cody


# PI CONTROL for co-cultures

We want to create a system to control the input of light into the system. The light will cause a change in the population ratios, the output of which will be read in as a percentage of GFP producing cells to the total.


### Some forseeable issues

- how can we incorporate the delay differential effects? ... i.e. the system doesn't respond immediately to the input.
- We are also moderating growth rate of the system and thus it is dependent on initial conditions.
- - cells are doubling/exponentially increasing

### Some good things about PI Control

- easy to set up & low computational power required.
- 


## khammash lab PI control

```python3

class OptoPIControl:
	def __init__(self, setpoint, kp, ki)
		self.setpoint = setpoint
		self.errors = []
		self.num_points = 0
		self.integral_term = 0


	def error(t):
		if self.num_points < t:
			# throw error
		return self.errors[t]

	def update_integral_term(val):
		self.integral_term += val

	def get_integral_term():
		return min(max(self.ki * self.integral_term, 0), 60)

	def update_error(reading):
		self.errors += [setpoint - reading]
	def get_update_proportional_term(reading):
		return kp*self.errors[self.num_points]

	def get_green_light():
		return min(max())

	def calculate_output(reading):
		self.num_points += 1
		self.update_error(reading)
		get_update_proportional_term(reading)
		update_integral_term(self.errors[self.num_points])


while true:
	reading = input("Enter new value: ")
	# also need to keep track of time
	time_elapsed = input("Time elasped (mins): ")
	try:
		assert(reading.type() == int)
	except:
		# throw error/break + output results?
	calculate_output(reading)

```

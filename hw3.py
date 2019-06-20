#Michael Nguyen 54213398
#11/2/18
def main():
	import random
	laps = eval(input("Number of laps in the race (>1): "))
	distance = eval(input("Distance of a lap (>=10km): "))
	min_speed = eval(input("The minimum speed for each car (>=40km/h): "))
	max_speed = eval(input("The maximum speed for each car(>min_speed): "))
	values = 0
	medium_speed = (min_speed + max_speed)/2
	offset = (max_speed - min_speed) * 0.025
	low_range = medium_speed - offset
	high_range = medium_speed + offset
	print("You have set the speed range defined: [",min_speed,",",max_speed,"]")
	print("Engine failure speed ranged defined: [",low_range,",",high_range,"]")
	speeds = [0,0,0,0,0,0,0,0,0,0]
	standing = []
	total_times = []
	cars = [1,2,3,4,5,6,7,8,9,10]

	for i in range(laps):

		print ("---------------------------------------------------------------------------")

		print("After lap ", i+1,":")

		for car in cars:
			car_index = cars.index(car)
			if(i == 0):
				speeds[car_index] = (max_speed - min_speed) * random.random() + min_speed
				y = ((speeds[car_index])/distance)
			

			else:
				if(speeds[car_index] == -1):
					speeds[car_index] = -1
					y = -1
				else:
					speeds[car_index] = (max_speed - min_speed) * random.random() + min_speed
					y = (speeds[car_index]/distance)

			if ((low_range < speeds[car_index] < high_range) and (i+1)%2 == 0):
					print("Car", car, "failed at speed", speeds[car_index])
					speeds[car_index] = -1
					y = -1


			if(i == 0):
				total_times.append(y)

			else:
				total_times[car_index] = total_times[car_index] + y

				if (y == -1):
					total_times[car_index] = -1


	
		ordered_times = sorted(total_times)
		for i in ordered_times:
	
			for j in total_times:
				if(i == j and i!= -1):
					standing.append(total_times.index(j)+1)

			



		for i in range(len(cars)):
			speeds[i] = round(speeds[i],2)
			total_times[i] = round(total_times[i],2)


		print("Car speed:",speeds)

		#figure out how to compile total time together, rn prints 20 values of time for second lap
		print("Total time used (minutes):",total_times)

		#ultilize sort, for the times, then l.index(value) to find original index
		print("Current standing:",standing)

		
		




		standing = []

		
			

			


main() 
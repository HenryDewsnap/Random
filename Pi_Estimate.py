import random 
##PIxR^2 = Total points in circle (around a certain point) / the total points of a square of 2x the radius

##PI Est = 4 * (total_dots_in_circle / total_dots_in_square) 
## 4 * because we are using 1/4 of a circle

def Estimate_Pi(n):
	r = 1 ##Radius
	total_dots_in_square = 0
	total_dots_in_circle = 0

	for i in range(n):
		x = random.uniform(0,r)
		y = random.uniform(0,r)

		if x ** 2 + y ** 2 < r: ##x ** 2 + y ** 2 works out the distance from the middle where the dot is 
			total_dots_in_circle += 1
		total_dots_in_square += 1

	return 4 * (total_dots_in_circle / total_dots_in_square) * r




print(Estimate_Pi(int(input("-> "))))

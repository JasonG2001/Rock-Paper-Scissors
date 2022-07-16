#Shopping list

#a = cost_of_tomatoes
#b = cost_of_sponges
#c = cost_of_juice
#d = cost_of_foil
#e = cost_of_sugar

from cmath import pi

from cv2 import sqrt


a = 1
b = 1
c = 1
d = 1
e = 1

total = 5*(a + b + c + d + e)

print(total)

vat =  0.2*total

print(total + vat)



#Shape measurements

cuboid_h = 25/7
cuboid_w = 25/2
cuboid_l = 35

cone_h = 10
cone_r = 3

cuboid_V = cuboid_h * cuboid_l * cuboid_l
cuboid_SA = 2 * (cuboid_h*cuboid_l + cuboid_h*cuboid_w + cuboid_l*cuboid_w)
cone_V = pi * cone_r**2 * cone_h/3
cone_SA = pi * cone_r * (cone_r + sqrt(cone_h**2 + cone_r**2))

print(f"The volume of the cuboid is {cuboid_V} and its surface area is {cuboid_SA}")
print(f"The volume of the cone is {cone_V} and its surface area is {cone_SA}")



#String length

long_word = "Pneumonoultramicroscopisilicovolcanoconiosis"

print(long_word)

first_c = long_word[0]
last_c = long_word[-1]

print(first_c + last_c)



#Basic arithmetic

a = 42
b = 25

sum = a + b
difference = a - b
product = a * b
division = a / b

print(sum)
print(difference)
print(product)
print(division)

a = 4.2 

print(type(a + b)) #Prints type of a + b as float as it is a decimal



phrase = ("what is this")
list = phrase.split()
list.reverse()
print(list)


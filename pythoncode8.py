#input
var = int(input())
Area = 3.14 * var ** 2
#string formatting
sentence = "the area of circle with radius {radius} is {area} meters square".format(radius=var ,area= Area)
print(sentence)
# #Dictionary
# band = {
#     "Paul": 240,
#     "Neil" : 300,
#     "Mark" : 328  
# }
 
# print(band)

# band2 = dict( Paul = 248, Heil = 300, Mmark = 328)
# print(band2)

one = {1,2,3,4}
two = {1,3,2,5}
three = one.intersection(two)
one.intersection_update(two)
four = one.symmetric_difference(two)
print(four)
print(one)
print(three)
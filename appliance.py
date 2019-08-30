# Add 3 indispensable appliances to this tuple

# Help from Sydney
Appliances0 = ('oven', 'refrigerator', 'coffee maker', 'rice cooker')

new_appliance = list(Appliances0)
new_appliance.append('micowave')
new_appliance.append('zoodler')
new_appliance.append('instant pot')

new_new_appliances = tuple(new_appliance)
print(new_new_appliances)

# my way didn't work
# for str in new_appliance:
#     print(str)
#     str = tuple()
#     for new in str:
#         new += Appliances

# Joe's version, in this case appliances = is just a label, not the data itself
Appliances = ('oven', 'refrigerator', 'coffee maker', 'rice cooker')
# The above Appliances is a label, its not the data
Appliances = set(Appliances)
Appliances.update(['dishwasher', 'microwave', 'toaster oven'])
Appliances = tuple(Appliances)
# the origin reference of APpliances no longer exists from the beginning. If you still wanted Python to really see it, you would have changed the variables name
print(Appliances)

# Danny's version
Appliances2 = ('oven', 'refrigerator', 'coffee maker', 'rice cooker')
Appliances2 += ('stuff',)
print(Appliances2)
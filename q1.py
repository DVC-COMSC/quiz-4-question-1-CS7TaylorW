
# ******************************
# Make your Code
# ******************************
prev = 0
prev2 = 0
current = 0 
cluster = 0 

for i in range(10):
    current = (int(input('Please enter a number')))
    if i < 1:
        prev = current
    if i == 1:
        if prev % 2 == 0 and current % 2 == 0:
            prev2 = prev
            prev = current
            cluster = cluster + 1
    if i >= 2:
        if prev2 % 2 == 0 and prev % 2 == 0 and current % 2 == 0:
            prev2 = prev
            prev = current
        elif prev % 2 == 0 and current % 2 == 0:
            prev2 = prev
            prev = current
            cluster = cluster + 1
        else:
            prev2 = prev
            prev = current

print (cluster)


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

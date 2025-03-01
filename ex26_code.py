# Exercise 26_code

import ex26

#print("name:", ex26.name)
#print("height:", ex26.height)

# Step 2: Find the __dict__
from pprint import pprint

#pprint(ex26.__dict__)

#print("height is", ex26.height)
#print("height is also", ex26.__dict__['height'])

# Step 3: Change the __dict__
#print(f"I am currently {ex26.height} inches tall")

#ex26.__dict__['height'] = 1000
#print(f"I am now {ex26.height} inches tall.")

#ex26.height = 12
#print(f"Oops, now I'm {ex26.__dict__['height']} inches tall.")


#print(pprint.__doc__)
help(pprint)

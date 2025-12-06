#Clipping in pandas means restricting values within a specified minimum and maximum range.
# Any value below the minimum becomes the minimum, and any value above the maximum becomes the maximum.

#Example:
import pandas as pd

s = pd.Series([2, 5, 10, 15, 20])

# clip values between 5 and 15
clipped = s.clip(lower=5, upper=15)

print(clipped)

data = [10, None, 20, None, 30]

# Print null values
for value in data:
    if value is None:
        print("NULL")

# Position of null values
data = [10, None, 20, None, 30]

positions = []

for index, value in enumerate(data):
    if value is None:
        positions.append(index)

print("Positions of NULL:", positions)

# Remove null
data = [10, None, 20, None, 30]

clean_data = [x for x in data if x is not None]

print(clean_data)

# Count number of null from list
data = [10, None, 20, None, 30, None]

count_null = data.count(None)

print("Number of NULL values:", count_null)


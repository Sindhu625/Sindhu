# Sindhu
def counter():
    if not hasattr(counter, "count"):
        counter.count = 0
    counter.count += 1
    print("Called", counter.count, "times")

# Using it:
counter()  
counter()  
counter()


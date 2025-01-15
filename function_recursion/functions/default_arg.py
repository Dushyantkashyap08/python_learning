#default argument : by -default a value is provided to a param in a function while function call. this value is picked up when no value to that param is provided.

def goodDay(name, ending="Thank you"): #providing a default value to "ending" param
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry", "Thanks") #here we are providing a value, so it not use default value
goodDay("Rohan") #here it will pick a default value 
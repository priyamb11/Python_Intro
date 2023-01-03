name = input("What is your name? ")

time = ((input("What is the time (in 24 hour format)? ")))

if "00:00" <= time <= "11:59":
    print("Hi",name, "good morning, the current time is", time, "AM")
elif "12:00" <= time <= "16:59":
    print("Hi", name, "good afternoon, the current time is", time, "PM")
elif "17:00" <= time <= "19:59":
    print("Hi", name, "good evening, the current time is", time, "PM")
elif "20:00" <= time <= "23:59":
    print("Hi", name, "good night, the current time is", time, "PM")
else:
    print("Hi", name, "good day. You have entered the wrong time format of", time, "please enter in a valid format (HH24:MM)")
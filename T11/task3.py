#Defining the qualifying time
qualifying_time = 100

#Getting the athlete's event times
print(f"""
Thank you for participating in HyperionDev's triathlon! 
We will now ask for your event times to check if you are qualifying and getting an award today!
Note that the qualifying time is {qualifying_time} minutes.
""")
run_time = int(input("Type your run time in minutes: "))
cycle_time = int(input("Type your cycle time in minutes: "))
swim_time = int(input("Type your swim time in minutes: "))

#Calculating the athlete's total time
athlete_total_time = run_time + cycle_time + swim_time

#Checking if and which award the athlete is getting
if athlete_total_time < qualifying_time:
    print(f"""
Congratulations  your total time was: {athlete_total_time}
That is in inside the qualifying time, you are awarded Provincial Colors.
    """)
elif athlete_total_time <= (qualifying_time + 5):
    print(f"""
Your total time was: {athlete_total_time}
As your time is within 5 minutes of the qualifying time you are awarded Provincial Half Colors.
    """)
elif athlete_total_time <= (qualifying_time + 10):
    print(f"""
Your total time was: {athlete_total_time}
As your time is within 10 minutes of the qualifying time you are awarded Provincial Scroll.
    """)
else:
    print(f"""
Your total time was: {athlete_total_time}
Unfortunately you are not getting an award today.
Better luck next time!
    """)
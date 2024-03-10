def run_distance_calculator(start,end):
    days = 1
    while start < end:
        start *= 1.10
        days += 1
    print(days)
    





starting = float(input("What is your starting daily distance?: "))
ending = float(input("What is your end running goal distance?: "))
run_distance_calculator(starting,ending)
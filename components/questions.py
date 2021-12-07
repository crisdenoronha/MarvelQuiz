from components import variables


def result(status):
    # Question 1
    print("\n---------------------------------------------------\n")
    print("What musical style do you prefer?\n")
    q1 = input("rap, rock, jazz, heavy metal: ")

    if q1 == "rap":
        variables.Hulk += 1

    elif q1 == "rock":
        variables.IronMan += 1

    elif q1 == "jazz":
        variables.CaptainAmerica += 1

    elif q1 == "heavy metal":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Question 2
    print("\n---------------------------------------------------\n")
    print("What food do you prefer?\n")
    q2 = input("taco, cheeseburger, vegetable, candy: ")

    if q2 == "taco":
        variables.Hulk += 1

    elif q2 == "cheeseburger":
        variables.IronMan += 1

    elif q2 == "vegetable":
        variables.CaptainAmerica += 1

    elif q2 == "candy":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Question 3
    print("\n---------------------------------------------------\n")
    print("In your free time, what you prefer to do?\n")
    q3 = input("bowling, video game, dancing, play drums: ")

    if q3 == "bowling":
        variables.Hulk += 1

    elif q3 == "video game":
        variables.IronMan += 1

    elif q3 == "dancing":
        variables.CaptainAmerica += 1

    elif q3 == "play drums":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Question 4
    print("\n---------------------------------------------------\n")
    print("Which vehicle do you prefer?\n")
    q4 = input("monster truck, lamborghini, harley-davidson, hotwheels: ")

    if q4 == "monster truck":
        variables.Hulk += 1

    elif q4 == "lamborghini":
        variables.IronMan += 1

    elif q4 == "harley-davidson":
        variables.CaptainAmerica += 1

    elif q4 == "hotwheels":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Question 5
    print("\n---------------------------------------------------\n")
    print("Where would you prefer to travel on vacation?\n")
    q5 = input("Thailand, Monaco, Hawaii, San Francisco: ")

    if q5 == "Thailand":
        variables.Hulk += 1

    elif q5 == "Monaco":
        variables.IronMan += 1

    elif q5 == "Hawaii":
        variables.CaptainAmerica += 1

    elif q5 == "San Francisco":
        variables.AntMan += 1

    else:
        variables.DocStrange += 1

    print("\n---------------------------------------------------\n")

    # Result
    print("\n---------------------------------------------------\n")
    if variables.Hulk >= 3:
        answer = variables.Hulk
        print("You are Hulk")

    elif variables.IronMan >= 3:
        answer = variables.IronMan
        print("You are Iron Man")

    elif variables.CaptainAmerica >= 3:
        answer = variables.CaptainAmerica
        print("You are Captain America")

    elif variables.AntMan >= 3:
        answer = variables.AntMan
        print("You are Ant-Man")

    else:
        answer = variables.DocStrange
        print("You are strange, Doctor Strange")

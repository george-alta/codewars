
while (True):
    ans1 = input("\nis the car silent when you turn the key? (yes/no) ")
    if ans1 == "yes" or ans1 == "y":
        ans2 = input("are the battery terminals corroded? (yes/no) ")
        if ans2 == "yes" or ans2 == "y":
            print("\n ACTION -> Clean Terminals and try starting again")
        else:
            print("\n ACTION -> Replace cables and try again")
    else:
        ans3 = input("does the car makes a clicking noise? (yes/no) ")
        if ans3 == "yes" or ans3 == "y":
            print("\n ACTION -> Replace the battery")
        else:
            ans4 = input("does the car crank up but fails to start? (yes/no) ")
            if ans4 == "yes" or ans4 == "y":
                print("\n ACTION -> check the spark plug connectors")
            else:
                ans5 = input("Does the engine start and then die? (yes/no) ")
                if ans5 == "yes" or ans5 == "y":
                    ans6 = input("Does your car has fuel injection? (yes/no) ")
                    if ans6 == "yes" or ans6 == "y":
                        print("\n ACTION -> Get In to service")

                    else:
                        print("\n ACTION -> Check to ensure the choke is opening and closing")
                else:
                    print("ACTION -> you are out of luck")
    restart = input("\n END OF DIAGNOSTICS - do you want to start again? (yes/no) ")
    if restart == "no" or restart == "n":
        break

"""Definitions
Single Loss Expectancy (sle): cost to completely replace an asset once
Annual Rate of Occurance (aro): calculation of number of times a given risk
    will occur in a year
Annual Loss Expectancy (ale): total amount of loss in a year due to a specific
    event. ALE = SLE * ARO
"""
asset_name = str(input("What asset are you assessing?\n"))
risk_event = str(input("What event is this estimate addressing?\n"))
asset_value = float(input("What is asset value \n"))
aro = float(input("How many times do you think this will happen this year?\n"))


def ale():
    print("The SLE for {0} is {1}.".format(asset_name, asset_value))
    ale_amount = asset_value * aro
    print("The ALE for {0}(s) is ${1}.".format(risk_event, ale_amount))
    return(ale_amount)


ale()

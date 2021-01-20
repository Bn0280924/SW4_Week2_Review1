# A Program to determine employee eligability for advancement

# Created by: <your name here>

# Copyright CTHS Engineering, Inc., 2021
# This code or any portion fo this code can be be reused without 
#    previous approval from the company CIO or CEO, in writing.

empName = "Sam"

#Project1(P1) - New school wing
#TA - Task Accuracy
#EstBud - Estimated Budget
#ActBud - Actual Budget
#EstMP - Estimated Manpower
#ActMP - Actual Manpower
empP1TA = 92
empP1EstBud = 1285000
empP1ActBud = 1301346
empP1EstMP = 1625
empP1ActMP = 1650

#Project2 - Custom motorcycle company warehouse
empP2TA = 98
empP2EstBud = 650000
empP2ActBud = 624000
empP2EstMP = 525
empP2ActMP = 515

#Project3 - Minor Nascar training track
empP3TA = 96
empP3EstBud = 2500000
empP3ActBud = 3231325
empP3EstMP = 1050
empP3ActMP = 1250

#Project4 - Man cave warehouse and house
empP4TA = 92
empP4EstBud = 825000
empP4ActBud = 830000
empP4EstMP = 400
empP4ActMP = 375

#your code goes below
tenpercent1=empP1EstBud-empP1ActBud/empP1EstBud 
manpower1=empP1ActMP-empP1EstMP/empP1EstMP
if empP1TA >= 90 and tenpercent1 <= 0.10 and manpower1 <= 0.25:
    print("Everything is right ")
else:
    print("No one or more reason is wrong")

tenpercent2=empP2EstBud-empP2ActBud/empP2EstBud 
manpower2=empP2ActMP-empP2EstMP/empP2EstMP
if empP2TA >= 90 and tenpercent2 <= 0.10 and manpower2 <= 0.25:
    print("Everything is right ")
else:
    print("No one or more reason is wrong")

tenpercent3=empP3EstBud-empP3ActBud/empP3EstBud 
manpower3=empP3ActMP-empP3EstMP/empP3EstMP
if empP3TA >= 90 and tenpercent3 <= 0.10 and manpower3 <= 0.25:
    print("Everything is right ")
else:
    print("No one or more reason is wrong")

tenpercent4=empP4EstBud-empP4ActBud/empP4EstBud 
manpower4=empP4ActMP-empP4EstMP/empP4EstMP
if empP4TA >= 90 and tenpercent4 <= 0.10 and manpower4 <= 0.25:
    print("Everything is right ")
else:
    print("No one or more reason is wrong")
    
            





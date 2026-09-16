totalRegularHours = totalOT = 0

TimeIn = int(input("Enter time in as integer number "))
TimeOut = int(input("Enter time out as integer number"))

if TimeOut > 17:
    OT = TimeOut - 17
    
regularHours = TimeOut - TimeIn - OT
totalRegularHours = totalRegularHours + regularHours
totalOT = totalOT + OT

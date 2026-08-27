totalregularHours = totalOT = 0

TimeIn = input("Enter time in as integer number ")
TimeOut = input("Enter time out as integer number")

if TimeOut > 17:
    OT = TimeOut - 17
    
regularHours = TimeOut - TimeIn - OT
totalregularHours = totalregularHours + regularHours
totalOT = totalOT + OT

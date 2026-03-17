#Switch

#def day_of_week(day):
#    if day==1:
#        return "It is Sunday"
#    elif day==2:
#        return "It is Monday"
#    elif day==3:
#        return "It is Tuesday"
#    else:
#        return "It is invalid"

def day_of_week(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return  "It is Monday"
        case 3:
            return "It is tuesday"
        case _:
            return "It is invalid"

print(day_of_week(4))
from django.utils import timezone

import datetime

def GetFmt(time, fmt):
    for i, k in fmt.items():
        if time <= i:
            return k

    return None

def ToStr(time):
    cal = ["{} month", "{} weeks", "{} days", "{} hours", "{} minutes", "few minutes"]
    now = timezone.now()
    
    if time and not isinstance(time, datetime.datetime):
        raise ValueError("Argument time must be type(%s)" % (type(datetime.datetime)))

    # convert days to month and weeks, seconds to hours and minutes
    cnvrt = now - time
    time = cnvrt.days // 30, cnvrt.days // 7, cnvrt.days, cnvrt.seconds // 3600, cnvrt.seconds // 60 % 60, cnvrt.seconds
    

    for i, date in enumerate(time):
        if date:
            result = "%s ago" % cal[i].format(date)
            break

    return result


from naoqi import ALProxy

def func_connect(IP, PORT):
	global memory
	memory = ALProxy("ALMemory", IP, PORT)

def getTime():
    currentTime = datetime.datetime.now()
    aTime = currentTime.hour
    bTime = currentTime.minute
    if (bTime == 0):
        if (aTime > 12):
            aTime = aTime - 12
            amorpm = "PM"
        elif (aTime == 12):
            amorpm = "PM"
        else:
            amorpm = "AM"
        cTime = "The time is " + str(aTime) + " o clock " + amorpm
    elif (bTime == 15):
        if (aTime > 12):
            aTime = aTime - 12
            amorpm = "PM"
        elif (aTime == 12):
            amorpm = "PM"
        else:
            amorpm = "AM"
        cTime = "The time is quarter past " + str(aTime) + " " + amorpm
    elif (bTime == 30):
        if (aTime > 12):
            aTime = aTime - 12
            amorpm = "PM"
        elif (aTime == 12):
            amorpm = "PM"
        else:
            amorpm = "AM"
        cTime = "The time is half past " + str(aTime) + " " + amorpm
    elif (bTime == 45):
        nexthour = aTime + 1
        if (nexthour >= 12):
            nexthour = nexthour - 12
            amorpm = "PM"
        else:
            amorpm = "AM"
        cTime = "The time is quarter to " + str(nexthour) + " " + amorpm
    elif (bTime < 30):
        if (aTime > 12):
            aTime = aTime - 12
            amorpm = "PM"
        elif (aTime == 12):
            amorpm = "PM"
        else:
            amorpm = "AM"
        cTime = "The time is " + str(bTime) + " minutes past " + str(aTime) + " " + amorpm
    else:
        nexthour = aTime + 1
        if (nexthour >= 12):
            nexthour = nexthour - 12
            amorpm = "PM"
        else:
            amorpm = "AM"
        cTime = "The time is " + str(60 - bTime) + " minutes to " + str(nexthour) + " " + amorpm
    return cTime

def getDate():
    currentTime = datetime.datetime.now()
    datenum = currentTime.day
    monthnum = currentTime.month
    if (monthnum == 1):
        month = "January"
    elif (monthnum == 2):
        month = "February"
    elif (monthnum == 3):
        month = "March"
    elif (monthnum == 4):
        month = "April"
    elif (monthnum == 5):
        month = "May"
    elif (monthnum == 6):
        month = "June"
    elif (monthnum == 7):
        month = "July"
    elif (monthnum == 8):
        month = "August"
    elif (monthnum == 9):
        month = "September"
    elif (monthnum == 10):
        month = "October"
    elif (monthnum == 11):
        month = "November"
    elif (monthnum == 12):
        month = "December"
    daynum = datetime.datetime.today().weekday()
    if (daynum == 0):
        day = "Monday"
    elif (daynum == 1):
        day = "Tuesday"
    elif (daynum == 2):
        day = "Wednesday"
    elif (daynum == 3):
        day = "Thursday"
    elif (daynum == 4):
        day = "Friday"
    elif (daynum == 5):
        day = "Saturday"
    elif (daynum == 6):
        day = "Sunday"
    combined = "Today is " + day + " the " + str(datenum) + "th of " + month + " " + str(currentTime.year)
    return combined

def getTemp():
    sFullName = "Head processor"
    sName = sFullName
    if( "motor" in sName or "Battery" in sName ):
        sName = sName.split(" motor")[0]
    elif( "processor" in sName ):
        sName = sName.split(" processor")[0]
    else:
        self.logger.error("No temperature found for this hardware: " + str(sFullName))
    sTemplate = "Device/SubDeviceList/%s/Temperature/Sensor/Value"
    sKeyName = sTemplate % sName
    try:
        nTemperature = int( self.memory.getData(sKeyName) )
        return nTemperature
    except:
        print("No temperature found for this hardware: " + str(sFullName))

def batteryCheck():
	return(memory.getData("BatteryLowDetected")):

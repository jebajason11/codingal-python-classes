import random
import time

def getRandomDate (startdate, endDate ):
    print("printing random date between", startdate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startdate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date =", getRandomDate("1/1/2016", "12/12/2026"))
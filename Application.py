import Email
import LiveTable
import time


totalCases = 0
activeCases = 0
newCases = 0
totalDeaths = 0
newDeaths = 0
totalRecover = 0

print("Welcome, please enter your email")
userEmail = input("Email : ")

Email.USER_EMAIL = userEmail

print("Well done !")
print("Now, please enter the country name that you want to recieve email notification about.")
countryName = input("Country name : ")

timeInterval = float(input("Ok, notification time interval (hour) : "))
timeInterval = timeInterval * 3600

lowerName = countryName.lower()
if lowerName == "south korea":
    countryName = "S.Korea"
if lowerName == "world":
    countryName = "total:"
while (True):
    Dict = LiveTable.request()

    countriesDic = Dict.get('Country,Other')
    activeCasesDic = Dict.get('ActiveCases')
    totalCasesDic = Dict.get('TotalCases')
    newCasesDic = Dict.get('NewCases')
    newDeathsDic = Dict.get('NewDeaths')
    totalDeathsDic = Dict.get('TotalDeaths')
    totalRecoveredDic = Dict.get('TotalRecovered')
    countryIndex = 0

    for i in countriesDic:
        if i.lower() != countryName.lower():
            countryIndex = countryIndex + 1
        else:
            break

    totalCases = totalCasesDic[countryIndex]
    activeCases = activeCasesDic[countryIndex]
    newCases = newCasesDic[countryIndex]
    totalDeaths = totalDeathsDic[countryIndex]
    newDeaths = newDeathsDic[countryIndex]
    totalRecover = totalRecoveredDic[countryIndex]

    Email.SUBJECT = "New COVID-19 stats for " + lowerName.upper()
    Email.MESSAGE = "New Cases : " + str(newCases) + "\n" + "New Deaths : " + str(newDeaths) + "\n" + "Total Cases : " \
                    + str(totalCases) + "\n" + "Active Cases : " + str(activeCases) + "\n" + "Total Deaths : " \
                    + str(totalDeaths) + "\n" + "Total Recovered : " + str(totalRecover) + "\n"
    Email.send_email(Email.SUBJECT, Email.MESSAGE)
    time.sleep(timeInterval)

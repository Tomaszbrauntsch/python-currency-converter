#Created by TomaszBrauntsch
#CurrencyConverter
#USD2Currencies
def USD2Currencies():
    USDtocurrencies = {
    "Euro" : 0.87,
    "Zloty" : 3.72,
    "Pound" : 0.77,
	"Bitcoin" : 0.00015,
	"AUD" : 1.40,
	"Yen" : 114.36
    }
    convertprice = 0
    total = 0
    print ("USD to Currency Converter")
    print ("Only Avaliable Currencies to Convert: ")
    for key in USDtocurrencies:
        print (key)
    user_currency = raw_input("Enter a currency you want to convert: ")
    user_amount = int(raw_input("Enter the amount you want to convert: "))
    for key in USDtocurrencies:
    	if user_currency.lower() == key.lower():
    	    convertprice = USDtocurrencies[key]

    total = user_amount*convertprice
    print ("The Convertion of " + "$" + str(user_amount)  + " to " + user_currency + " is " + str(total))
#Currencies2USD
def Currencies2USD():
    CurrenciestoUSD = {
        "Euro" : 1.15,
        "Zloty" : 0.27,
        "Pound" : 1.30,
		"Bitcoin" : 6470,
		"AUD" : 0.71,
		"Yen" : 0.0087
    }
    convertprice = 0
    total = 0
    print ("Currency to USD Converter")
    print ("Only Avaliable Currencies for Convertion")
    for key in CurrenciestoUSD:
        print (key)
    user_currency = raw_input("Enter a currency you want to convert to USD: ")
    user_amount = int(raw_input("Enter the amount you want to convert to USD: "))
    for key in CurrenciestoUSD:
        if user_currency.lower() == key.lower():
            convertprice = CurrenciestoUSD[key]

    total = user_amount*convertprice
    print ("The Convertion of " + str(user_amount) + " " + str(user_currency) + "(s)" + " is " + "$" + str(total))

#First input
def initialsetup():
	print ("Would you like to Convert to USD to Currency(U2C) or Currency to USD(C2U): ")
	answer = input()
	if answer.lower() == "u2c".lower or answer.upper() == "U2C" :
		USD2Currencies()
	if answer.lower() == "c2u" or answer.upper() == "C2U":
		Currencies2USD()

initialsetup()
print ("Would you like to convert again (Yes or no?): ")
user_inputans = raw_input()
if user_inputans == "Yes" or user_inputans.lower() == "yes":
	initialsetup()
else:
	print ("Thank you for using the Convertion Program")

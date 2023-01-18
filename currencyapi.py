import requests
import json

class jaszczomp:

    def exchangeinput():
        res = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/")
        x = res.json()
        table=x[0]['rates']
        rate, currency = input('Please insert value and currency code, e.g. 1 USD\n').split()
        for i in table:
            if currency == i['code']:
                print(f"{rate} {currency} = {i['mid'] * float(rate):.2f} PLN")

    def exchangerate():
        res2 = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/")
        y = res2.json()
        table2 = y[0]['rates']
        currency2=input("Please insert currency code\n")
        for i in table2:
            if currency2 == i['code']:
                print(f"1 {currency2} = {i['mid']:.2f} PLN")
    while True:
        menu=int(input("What would You like to do? Insert: \n"
          "1 - if You want to convert any currency to PLN\n"
          "2 - if You want to see today's currency rate\n"
          "3 - exit\n"))
        if menu == 1:
            exchangeinput()
        elif menu == 2:
            exchangerate()
        elif menu == 3:
            break
        else:
            print(f"Do not recognize option, please insert correct value")
            continue
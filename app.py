import requests

# This scripts is getting data from CoinDesk API

url = "https://api.coindesk.com/v1/bpi/currentprice.json"


def showUsd():
    """
    This function sends GET request to CoinDesk API and show Bitcoin's current price in USD.
    """
    response = requests.get(url)  # sending request to url
    jsonResponse = response.json()  # saving response as JSON
    time = jsonResponse["time"]["updated"]  # getting time from response
    code = jsonResponse["bpi"]["USD"]["code"]  # getting currency code from response
    rate = jsonResponse["bpi"]["USD"]["rate"]  # getting price in USD from response.

    print(time, code, rate)


def showGbp():
    response = requests.get(url)  # sending request to url
    jsonResponse = response.json()  # saving response as JSON
    time = jsonResponse["time"]["updated"]  # getting time from response
    code = jsonResponse["bpi"]["GBP"]["code"]  # getting currency code from response
    rate = jsonResponse["bpi"]["GBP"]["rate"]  # getting price in USD from response.

    print(time, code, rate)


def showEuro():
    # Your code will go here, remove the pass once you are done editing your code
    pass


if __name__ == "__main__":
    while True:
        try:
            print("1. Show Bitcoin Price in USD.")
            print("2. Show Bitcoin Price in GBP.")
            print("3. Show Bitcoin Price in EUR.")
            userInput = int(input("Please Enter Your Choice: "))
            if userInput == 1:
                showUsd()
                break
            elif userInput == 2:
                showGbp()
                break
            elif userInput == 3:
                showEuro()
                break
            else:
                print("Something Went Wrong, Please Try Again...")
                continue
        except requests.RequestException:
            print("Something Went Wrong, Quitting...")
            break
        except KeyboardInterrupt:
            quit(0)
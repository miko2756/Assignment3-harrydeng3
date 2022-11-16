import requests


def show_current_price(currency_type):
    currency_types = {
        1: "USD",
        2: "GBP",
        3: "EUR"
    }

    if currency_type not in currency_types.keys():
        print("Something Went Wrong, Please Try Again...")

        return

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")  # sending request to url
    json_response = response.json()  # saving response as JSON

    time = json_response["time"]["updated"]
    code = json_response["bpi"][currency_types[currency_type]]["code"]  # getting currency code from response
    rate = json_response["bpi"][currency_types[currency_type]]["rate"]  # getting price in USD from response.

    print(time, code, rate)


if __name__ == "__main__":
    while True:
        try:
            print("1. Show Bitcoin Price in USD.")
            print("2. Show Bitcoin Price in GBP.")
            print("3. Show Bitcoin Price in EUR.")
            userInput = int(input("Please Enter Your Choice: "))
            show_current_price(userInput)
        except requests.RequestException:
            print("Something Went Wrong, Quitting...")
            break
        except KeyboardInterrupt:
            quit(0)

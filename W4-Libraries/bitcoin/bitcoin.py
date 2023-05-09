import sys
import requests

try:
    num_bitcoins = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    usd_rate = float(data["bpi"]["USD"]["rate_float"])
except (requests.RequestException, KeyError, ValueError):
    print("Error: Failed to get the current Bitcoin price from the CoinDesk API.")
    sys.exit(1)

total_cost_usd = num_bitcoins * usd_rate

# Print the total cost in USD to four decimal places with a thousands separator
print(f"${total_cost_usd:,.4f}")
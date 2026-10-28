import sys
import os
import requests


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Invalid argument")

try:
    api_key = os.getenv("COINCAP_API_KEY")
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin",
        params={"apiKey": api_key}
    )

    response.raise_for_status()
    price = float(response.json()["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("API error")

print(f"${bitcoin * price:,.4f}")

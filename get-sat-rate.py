import bitcoin_value
from datetime import datetime

print(datetime.now(), end='\n'*2)
usd_fetcher = bitcoin_value.currency("USD")
usd_per_btc = usd_fetcher.fetch()
print(f"1 BTC = {usd_per_btc} USD")
sat_per_btc = 100_000_000
quarter_in_sat = 0.25 / usd_per_btc * sat_per_btc
print(f"25¢ ≈ {round(quarter_in_sat,1)} SAT")
print(f"25¢/hour ≈ {round(quarter_in_sat / 60)} SAT/minute")

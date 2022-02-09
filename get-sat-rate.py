import bitcoin_value
from datetime import datetime

SAT_PER_BTC = 100_000_000

print(datetime.now(), end='\n'*2)
usd_per_btc = bitcoin_value.currency("USD").fetch()
print(f"1 BTC = {usd_per_btc} USD")
quarter_in_sat = 0.25 / usd_per_btc * SAT_PER_BTC
print(f"25¢ ≈ {round(quarter_in_sat,1)} SAT")
print(f"25¢/hour ≈ {round(quarter_in_sat / 60)} SAT/minute")

"""
Quick utility script for fetching current BTC value in USD
and computing the rate I want to use to reimburse podcasts
via the value-for-value feature.
"""
import datetime
import bitcoin_value

SAT_PER_BTC = 100_000_000

print(datetime.datetime.now(), end='\n'*2)
usd_per_btc = bitcoin_value.currency("USD").fetch()
print(f"1 BTC = {usd_per_btc} USD")
quarter_in_sat = 0.25 / usd_per_btc * SAT_PER_BTC
print(f"25¢ ≈ {round(quarter_in_sat,1)} SAT")
print(f"25¢/hour ≈ {round(quarter_in_sat / 60)} SAT/minute")

"""
Quick utility script for fetching current BTC value in USD
and computing the rate I want to use to reimburse podcasts
via the value-for-value feature.
"""
import datetime
import sys
import bitcoin_value

def format_usd(value):
    return f"{round(value*100)}¢" if value < 1 else f"${value:.2f}"

SAT_PER_BTC = 100_000_000

usd_per_hour = float(sys.argv[1]) if len(sys.argv) > 1 else 0.25

print(datetime.datetime.now(), end='\n'*2)
usd_per_btc = bitcoin_value.currency("USD").fetch()
print(f"1 BTC = {usd_per_btc} USD")
sat_per_hour = usd_per_hour / usd_per_btc * SAT_PER_BTC
usd_pretty = format_usd(usd_per_hour)
print(f"{usd_pretty} ≈ {round(sat_per_hour)} SAT")
print(f"{usd_pretty}/hour ≈ {round(sat_per_hour / 60)} SAT/minute")

# %Z
# "2021-07-05T03:24:57.000+00:00",
from datetime import datetime, timezone, timedelta

tz_utc = timezone(timedelta(hours=8))
print(datetime.now(tz=tz_utc).strftime('%Y-%m-%d %H:%M:%S %Z'))
print(datetime.now(tz=tz_utc).strftime('%Y-%m-%d %H:%M:%S %Z'))
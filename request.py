from urllib.request import urlopen, HTTPError
import json

# START
url = 'https://httpbin.org/ip'
try:
    fp = urlopen(url)
except HTTPError as err:
    raise SystemExit('error: cannot fetch {!r} - {}'.format(url, err))

try:
    reply = json.load(fp)
except ValueError as err:
    raise SystemExit('error: cannot parse reply - {}'.format(err))

print(reply['origin'])
# END

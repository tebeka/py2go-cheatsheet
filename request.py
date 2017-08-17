from urllib.request import urlopen, HTTPError
import json

# START
url = 'https://httpbin.org/ip'
try:
    fp = urlopen(url)
except HTTPError as err:
    msg = 'error: cannot get {!r} - {}'.format(url, err)
    raise SystemExit(msg)

try:
    reply = json.load(fp)
except ValueError as err:
    msg = 'error: cannot decode reply - {}'.format(err)
    raise SystemExit(msg)

print(reply['origin'])
# END

from pint import UnitRegistry
import common
import json

ureg = UnitRegistry()
units = ureg._units.keys()
suffixes = ureg._suffixes.keys()
prefixes = ureg._prefixes.keys()

def uni(str):
    return str.encode('utf-8')

result = {}
result["prefixes"] = []
result["suffixes"] = []
result["units"] = []

for p in prefixes:
    result["prefixes"].append(uni(p))

for s in suffixes:
    result["suffixes"].append(uni(s))

for u in units:
    result["units"].append(uni(u))

print json.dumps(result, indent=4, sort_keys=True)


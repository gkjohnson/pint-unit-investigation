from pint import UnitRegistry

ureg = UnitRegistry()
units = ureg._units.keys()
suffixes = ureg._suffixes.keys()
prefixes = ureg._prefixes.keys()

def uni(str):
    return str.encode('utf-8')


print '# All units available in pint'
for p in prefixes:
    for u in units:
        for s in suffixes:
            print uni(p) + uni(u) + uni(s)
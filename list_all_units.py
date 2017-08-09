from pint import UnitRegistry

ureg = UnitRegistry()
units = ureg._units.keys()
suffixes = ureg._suffixes.keys()
prefixes = ureg._prefixes.keys()

def uni(str):
    return str.encode('utf-8')

# Print all possible units by joining
# {prefix}{unit}{suffix}
print '# All Units in Pint'
print 'All suffixes, prefixes, and units in which are used to define all available units.'

print '## Prefixes'
for p in prefixes:
    print '`' + uni(p) + '`\n'

print '## Units'
for u in units:
    print '`' + uni(u) + '`\n'

print '## Suffixes'
for s in suffixes:
    print '`' + uni(s) + '`\n'

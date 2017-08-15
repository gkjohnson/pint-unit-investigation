from pint import UnitRegistry
import common

ureg = UnitRegistry()
sets = common.get_base_unit_sets(ureg)

# print out all units in each dimension group
print '# All Base Unit Sets'
print 'List of all units in each base_unit group defined in Pint.'
for bu in sets.keys():
    print '## ' + str(bu).encode('utf-8')
    dim = ureg.Quantity(1, bu).dimensionality
    print '_' + str(dim).encode('utf-8') + '_'
    print '\n'

    for u in sets[bu]:
        print '`' + u.encode('utf-8') + '`'
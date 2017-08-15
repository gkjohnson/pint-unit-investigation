from pint import UnitRegistry
import common

ureg = UnitRegistry()
sets = common.get_dimension_sets(ureg)

# print out all units in each dimension group
print '# All Dimensionality Sets'
print 'List of all units in each dimension group defined in Pint.'
for dim in sets.keys():
    print '## ' + str(dim).encode('utf-8')
    for u in sets[dim]:
        print '`' + u.encode('utf-8') + '`'
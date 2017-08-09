from pint import UnitRegistry
import common

ureg = UnitRegistry()

sets = common.get_unit_sets(ureg)

# print out all units in each dimension group
for dim in sets.keys():
    print '\n# ' + str(dim).encode('utf-8')
    for u in sets[dim]:
        print u.encode('utf-8')
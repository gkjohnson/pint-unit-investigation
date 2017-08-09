from pint import UnitRegistry
import common

ureg = UnitRegistry()
sets = common.get_unit_sets(ureg)

# guarantee that all units in each dimension
# group are convertible
for dim in sets.keys():
    for u1 in sets[dim]:
        for u2 in sets[dim]:
            res = ureg.Quantity(1, u1).to(u2)

print 'All units convertible!'

# TODO: I noticed some issues with temperatures when running
# the above with the following line:
#   res = ureg.Quantity(1, u1) + ureg.Quantity(1, u2)

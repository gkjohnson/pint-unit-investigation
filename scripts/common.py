def get_dimension_sets(ureg):
    units = ureg._units.keys()

    sets = {}

    # gather all units with common dimensions
    for u in units:
        dim = ureg.Quantity(1, u).dimensionality
        if not dim in sets:
            sets[dim] = []
        sets[dim].append(u)
    return sets

def get_base_unit_sets(ureg):
    units = ureg._units.keys()

    sets = {}

    # gather all units with common dimensions
    for u in units:
        bu = ureg.Quantity(1, u).to_base_units().units
        if not bu in sets:
            sets[bu] = []
        sets[bu].append(u)
    return sets
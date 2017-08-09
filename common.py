def get_unit_sets(ureg):
    units = ureg._units.keys()

    sets = {}

    # gather all units with common dimensions
    for u in units:
        dim = ureg.Quantity(1, u).dimensionality
        if not dim in sets:
            sets[dim] = []
        sets[dim].append(u)
    return sets
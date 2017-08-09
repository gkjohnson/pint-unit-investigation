# pint-unit-investigation

Some basic scripts to investigate the available data that can be extracted from [Pint](https://github.com/hgrecco/pint) for use in autocomplete UIs and the possible problems involved in custom unit definition.

## [list_all_units.py](scripts/list_all_units.py)

Lists all prefixes, suffixes, and units available in pint which can be combined to generate all possible available units.

The output of the script is available [here](outputs/all-units.md).

## [list_all_convertible_groups.py](scripts/list_all_convertible_groups.py)

Lists all unit dimensions and units within each category, all of which can be converted between.

The output of the script is available [here](outputs/convertible-units.md)

## [guarantee_convertible.py](scripts/guarantee_convertible.py)

Converts to and from every unit in every unit set to guarantee that they are all convertable using Pint's `Quantity.to` function.

#### Temperature Conversion Problem

Checking for unit compatibility using the expression `ureg.Quantity(1, unit1) + ureg.Quantity(1, unit2)` threw an error when converting between temperatures, even when the two units were the same:

```
pint.errors.OffsetUnitCalculusError: Ambiguous operation with offset unit (degF, degF)
```

[This issue](https://github.com/hgrecco/pint/issues/386) discusses a related problem with a possible solution being to create the registry with:
```python
ureg = UnitRegistry(autoconvert_offset_to_baseunit=True)
```

And [here](http://pint.readthedocs.io/en/latest/nonmult.html) is some other documentation on why.

## [custom_units.py](scripts/custom_units.py)

Script that imports custom unit definitions and defines a new unit dimension

#### Unicode Character Problem

It seems that library chokes on importing the unicode degree character (found in the custom units file) and gives the following error:

```
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 0: ordinal not in range(128)
```

A few options:
- This deserve some more investigation to understand how python handles strings and encodings and submit a PR or issue for Pint
- Avoid using special characters in unit definitions
- Do a special transform for display to convert to a string that pint understands

#### Token Characters Problem

Token characters like `+`, `-`, `%`, `*`, etc that python uses in expressions cannot be used as or in unit strings. The full list of token characters can be found [here](https://github.com/hgrecco/pint/blob/master/pint/compat/tokenize.py#L65). This is primarily a problem for the `%` character. If we feel strongly enough we can submit a PR or an issue.

This issue is about this same problem:
https://github.com/hgrecco/pint/issues/429

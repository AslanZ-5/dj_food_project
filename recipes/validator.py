from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError

# django Validators  documentation  https://docs.djangoproject.com/en/3.2/ref/validators/
valid_unit_measurements = ['pounds', 'lbs', 'oz', 'grom']


def validator_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f'{value} is not a valid unit of measure')
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f'{e}')
    except:
        raise ValidationError(f'{value} is not a valid unit of measure')

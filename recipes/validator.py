from django.core.exceptions import ValidationError
# django Validators  documentation  https://docs.djangoproject.com/en/3.2/ref/validators/
valid_unit_measurements = ['pounds','lbs','oz','grom']

def validator_unit_of_measure(value):
    if value not in valid_unit_measurements:
        raise ValidationError(f'{value} is not a valid unit of measure')
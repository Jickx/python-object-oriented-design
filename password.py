class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
    }

    # BEGIN (write your solution here)

    def __init__(self, contain_numbers=False):
        self.options = self.OPTIONS
        self.options['contain_numbers'] = contain_numbers
        self.error = {}

    def _is_length_long_enough(self, password):
        return len(password) >= self.options['min_len']

    def validate(self, password):
        self.error.clear()
        if not self._is_length_long_enough(password):
            self.error['min_len'] = 'too small'
        if not self._has_number(password) and self.options['contain_numbers']:
            self.error['contain_numbers'] = 'should contain at least one number'
        return self.error
    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)


def test_validate_with_options():
    validator = PasswordValidator(contain_numbers=True)
    errors1 = validator.validate('qwertya3sdf')
    assert not errors1

    errors2 = validator.validate('qwerty')
    assert errors2 == {
        'min_len': 'too small',
        'contain_numbers': 'should contain at least one number'
        }
    errors3 = validator.validate('q23ty')
    assert errors3 == {'min_len': 'too small'}

test_validate_with_options()

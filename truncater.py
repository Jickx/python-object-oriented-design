class Truncater:
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

    def __init__(self, **options):
        self.options = self.OPTIONS | options

    def truncate(self, phrase, **options):
        if options:
            options = self.options | options
        else:
            options = self.options
        separator = options['separator']
        length = options['length']
        if length >= len(phrase):
            separator = ''
        result = f'{phrase[:length]}{separator}'
        print(result)


truncater = Truncater(length=3)

truncater.truncate('one two', length=7)  # 'one two'


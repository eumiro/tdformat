import datetime


class Td(datetime.timedelta):
    def __format__(self, format_spec):
        return "hello"

import datetime
import re
from collections import namedtuple


class Td(datetime.timedelta):
    def __format__(self, format_spec):
        """Format timedelta"""
        if not isinstance(format_spec, str):
            raise TypeError(
                f"__format__() argument 1 must be str, "
                f"not {type(format_spec)}"
            )
        Field = namedtuple("Field", ["start", "end", "content"])
        fields = [Field(0, 0, "")]
        for m in re.finditer(r"%([^HMS%]*)([HMS%])", format_spec):
            if m[2] == "%":
                content = "%"
            elif m[2] == "H":
                content = f"{self.total_seconds() // 3600:.0f}"
            elif m[2] == "M":
                content = f"{self.total_seconds() // 60:.0f}"
            elif m[2] == "S":
                content = f"{self.total_seconds():.0f}"
            else:
                content = m[0]
            fields.append(Field(m.start(), m.end(), content))
        fields.append(Field(len(format_spec), len(format_spec), ""))
        parts = []
        for field0, field1 in zip(fields, fields[1:]):
            parts.append(field0.content)
            parts.append(format_spec[field0.end : field1.start])
        return "".join(parts)

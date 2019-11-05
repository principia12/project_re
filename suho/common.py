import enum


class MetaCharacter(enum.Enum):
    OP_OR = '|'
    WILDCARD = '.'
    ESCAPE = '\\'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

# coding: utf-8


OBJECT = dict
ARRAY = list
VALUE = {
    u"string": (unicode, str),
    u"number": (int, float),
    u"object": OBJECT,
    u"array": ARRAY,
    u"bool": bool
}
NULL = None
TYPE = [u'array', u'object', u'bool', u'string', u'number', u'null']


class JsonTypeError(StandardError):
    """ Inappropriate argument type. """

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(S, *more):  # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Value(object):
    def __init__(self, key, value, value_type):
        """
                     @type key: int, str
                     @type value: object
                     @type value_type: unicode
        """
        self.key = key
        self.value = value
        self.value_type = value_type

    def __repr__(self):
        if self.value in TYPE:
            self.value = u'''"{}"'''.format(self.value)
        return u'''{}'''.format(self.value)

    def __hash(self):
        if isinstance(self.key, int):
            return repr(self.value), self.value_type
        return self.key, repr(self.value), self.value_type

    def __hash__(self):
        return hash(self.__hash())

    def __eq__(self, other):
        if isinstance(other, Value):
            return self.__hash() == other.__hash()
        return other.__eq__(self)


def json_type(value):
    """
                 @type value: object
    """
    if value == NULL:
        return u"null"
    for i in VALUE:
        if isinstance(value, VALUE[i]):
            return i
    assert JsonTypeError(value)


def solve_object(value):
    """
          @type value: dict
    """
    json_value = {}
    for key in value:
        json_value[key.encode("utf-8")] = Value(key, traverse(value[key]), json_type(value[key]))
    return json_value


def solve_array(value):
    """
              @type value: list
    """
    json_value = []
    for index, v in enumerate(value):
        json_value.append(Value(index, traverse(v), json_type(v)))
    return list(set(json_value))


def traverse(value):
    """
             @type value: object
    """
    if isinstance(value, OBJECT):
        return solve_object(value)
    if isinstance(value, ARRAY):
        return solve_array(value)
    return json_type(value)

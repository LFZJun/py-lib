# coding: utf-8
r"""
    example:

    >> js_object = js(dict(foo="foo", bar="bar"))
    {'foo': 'foo', 'bar': 'bar'}
    >> print javascript_object
    {
        "foo": "foo",
        "bar": "bar"
    }
    >> js_object.foo
    foo
    >> js_object.foo = "bar"
    >> js_object.foo
    bar
"""
__all__ = ["js"]
import json


def js(_obj=None):
    """
            javascript_object() -> new empty javascript object
    """
    if _obj is None:
        return Js()
    if isinstance(_obj, (str, unicode)):
        try:
            _obj = json.loads(_obj)
        except:
            return None
    if isinstance(_obj, dict):
        return Js(_obj)
    if isinstance(_obj, list):
        return JsList(_obj)
    return None


class Js(dict):
    """
        Js() -> new empty dictionary
    """
    type = dict

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        _t = self.get(item, None)
        if isinstance(_t, dict):
            return Js(_t)
        if isinstance(_t, list):
            return JsList(_t)
        return _t

    def stringify(self, indent=None):
        return json.dumps(self, indent=indent, ensure_ascii=False)

    def __str__(self):
        _t = self.stringify(indent=4).encode("utf-8")
        return _t

    def origin(self):
        return dict(self)


class JsList(list):
    type = list

    def __str__(self):
        _t = self.stringify(indent=4).encode("utf-8")
        return _t

    def stringify(self, indent=None):
        return json.dumps(self, indent=indent, ensure_ascii=False)

    def __getitem__(self, item):
        return js(list(self)[item])

    def __iter__(self):
        n = self.__len__()
        it = list.__iter__(self)
        while n > 0:
            yield js(it.next())
            n -= 1

    def origin(self):
        return list(self)

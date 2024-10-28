import inspect


def introspection_info(obj):
    info = {'type': type(obj).__name__, 'attributes': [], 'methods': [], 'module': obj.__module__,
            'docstring': inspect.getdoc(obj)}

    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    return info


class MyClass:

    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value


my_object = MyClass(10)

object_info = introspection_info(my_object)
print(object_info)

import inspect


def introspection_info(obj: object) -> object:
    print('(type', type(obj))
    print('\nattributes -')
    for attr_name in dir(obj):
        # attr = getattr(obj, attr_name)
        print(attr_name)
    print('\nmethods -')
    print(inspect.getfullargspec(obj)[0])
    print(inspect.getmodule(obj))


number_info = introspection_info(list)

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1
print_params(b=25)
print_params(c=[1, 2, 3])

# 2
values_list = [1, '1', 1.0]
values_dict = {'a': 'abra', 'b': 'cadabra', 'c': 'vjuhhh'}

print_params(*values_list)
print_params(**values_dict)

# 3
more_values_list = [1, '1']
more_values_dict = {"a": 'urban', 'b': 'univer'}

print_params(*more_values_list, 128)
print_params(c=256, **more_values_dict)

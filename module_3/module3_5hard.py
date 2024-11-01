def calculate_structure_sum(struct):
    k = 0
    if isinstance(struct, int):
        k += struct
    elif isinstance(struct, str):
        k += len(struct)
    else:
        for elem in struct:
            if isinstance(elem, int):
                k += elem
            elif isinstance(elem, str):
                k += len(elem)
            elif isinstance(elem, dict):
                for key, val in elem.items():
                    k += calculate_structure_sum(key)
                    k += calculate_structure_sum(val)
            else:
                k += calculate_structure_sum(elem)
    return k

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


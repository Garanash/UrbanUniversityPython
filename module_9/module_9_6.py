def all_variants(text):
    for n in range(1, len(text) + 1):
        for j in range(len(text)):
            if n + j < len(text) + 1:
                yield text[j:n + j]
                continue


a = all_variants("abc")
for i in a:
    print(i)

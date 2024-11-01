from module2hard import password

test_dict = {}
with open("test.txt") as file:
    for line in file:
        test_dict[int(line.split(" - ")[0])] = line.split(" - ")[1].strip()
at = 0
for test in range(3, 21):
    if password(test) == test_dict[test]:
        print(f"test for {test} result: +")
        at += 1
    else:
        print(f"test for {test} result: -")
if at == 18:
    print("Great work")

data = open('day18.txt', 'r').read().splitlines()
sum_of_all = 0.0

#(2 + 7 + (6 + 8 + 8 + 6 * 4) + 4 + 3) + 2 + (4 * 3 + 2) + (6 * 4) * 8 + 3
def what_to_do(x, a, b):
    if x == '+':
        return a + b
    if x == '*':
        return a * b

for rekensom in data:
``
    rekensom = rekensom.replace(' ', '')
    dict_of_sums = {}
    c = 0

    for something in len(rekensom):
        if something == '(':
            while something != ')':
                group_ = group_ + ', ' + rekensom[something]

            print(group_)


import time
now = time.time()

def one():
    start_data = [13,16,0,12,15,1]
    x = 30000000 - len(start_data)

    while x != 0:

        iets = start_data[-1]
        iteration_pos = len(start_data) - 1

        for iets_anders in reversed(start_data[0:len(start_data)-1]):
            if iets == iets_anders:
                nieuwe_getal = len(start_data) - iteration_pos
                start_data.append(nieuwe_getal)
                break

            iteration_pos -= 1

            if iteration_pos == 0:
                start_data.append(0)

        x -= 1

    print(start_data[-1])
    print(time.time() - now)

def two():
    start_data = [13,16,0,12,15,1]
    x = (2020 - len(start_data))

    while x != 0:

        print(start_data)
        a = start_data[-1]
        z = start_data[0:len(start_data) - 1]

        if a in z:
            new = len(start_data) - start_data[0: len(start_data) - 1].index(a) -1
            start_data.append(new)
        else:
            start_data.append(0)

        x -= 1

    print(start_data[-1])


two()
print('tijd', now-time.time())

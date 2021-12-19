card_key, door_key = 10943862, 12721030

def encyptionKey(public, otherkey):

    loops, value, subject, mod = 0, 1, 7, 20201227
    while value != public:
        value = (value * subject) % mod
        loops += 1
    return pow(otherkey,loops,mod)

print(encyptionKey(card_key, door_key))
print(encyptionKey(card_key, door_key))

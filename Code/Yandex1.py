import timeit


def find_genre(genr):
    count = 0
    for a in name_genres:
        if a == genr:
            count += 1
    return count


def find_genre1(name):
    count = 0
    for i in range(len(name_genres)):
        if name_genres[i] == name:
            count += 1
    return count


name_genres = ['hip-hop', 'rock', 'alternative', 'hip-hop']
genre = 'hip-hop'

print(timeit.timeit("find_genre(genre)", setup="from __main__ import find_genre, genre", number=1))
# 1.4700000000145153e-05
print(timeit.timeit("find_genre1(genre)", setup="from __main__ import find_genre1, genre", number=1))
# 0.00011230000000006513
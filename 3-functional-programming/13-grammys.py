from functools import reduce


def longer_than_five_minutes(song):
    return song[1] > 5.0


def minutes_to_seconds(song):
    return song[1] * 60


def add_durations(x, y):
    return x + y


playlist = [
    ("What Was I Made For?", 3.42),
    ("Just Like That", 5.05),
    ("Song 3", 6.8),
    ("Leave The Door Open", 4.02),
    ("I Can't Breath", 4.47),
    ("Bad Guy", 3.14),
]

longer_than_five = filter(longer_than_five_minutes, playlist)
min_to_sec = map(minutes_to_seconds, playlist)
duration_sum = reduce(add_durations, playlist)

print(list(longer_than_five))
print(list(min_to_sec))
print(duration_sum)

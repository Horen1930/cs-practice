def count_items(values):
    d = {}

    for key in values:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    return d


def unique_sorted(values):
    d = set()

    for value in values:
        d.add(value)

    return sorted(list(d))


def common(first, second):
    d = set()

    for value in first:
        if value in second:
            d.add(value)

    return sorted(list(d))


def only_in_first(first, second):
    d = set()

    for value in first:
        if value not in second:
            d.add(value)

    return list(d)
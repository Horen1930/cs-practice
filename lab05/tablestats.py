def read_rows(lines : list[str]) -> list[dict]:
    l = []
    header = None

    for line in lines:
        if header is None:
                header = line.strip().split(',')
                continue
        l.append({
            header[0]: line.strip().split(',')[0],
            header[1]: line.strip().split(',')[1],
            header[2]: line.strip().split(',')[2]
        })

    return l


def count_types(rows : list[dict]) -> dict:
    d = {}

    for row in rows:
        if row['тип'] in d:
             d[row['тип']] += 1
        else:
            d[row['тип']] = 1

    return d
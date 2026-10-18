def read_rows(lines : list[str]) -> list[dict]:
    l = []
    header = None

    for line in lines:
        if not line.strip():
            continue

        if header is None:
                header = line.strip().split(',')
                continue

        values = line.strip().split(',')
        
        if len(values) != len(header):
            continue

        row = {}
        for i in range(len(header)):
            row[header[i].strip()] = values[i].strip()
        l.append(row)

    return l


def count_types(rows : list[dict]) -> dict:
    d = {}

    for row in rows:
        if row['тип'] in d:
             d[row['тип']] += 1
        else:
            d[row['тип']] = 1

    return d


def total_minutes(rows : list[dict], kind : str) -> float:
    time = 0.0

    for row in rows:
        if row['тип'] == kind:
            try:
                time += float(row['минуты'].replace(',', '.'))
            except ValueError:
                continue
    
    return round(time, 1)


def to_csv(counts : dict) -> str:
    s = 'тип,количество\n'

    for kind, count in sorted(counts.items()):
        s += f"{kind},{count}\n"

    return s

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

        l.append({
            header[0]: values[0].strip(),
            header[1]: values[1].strip(),
            header[2]: values[2].strip()
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


def total_minutes(rows : list[dict], kind : str) -> int:
    time = 0

    for row in rows:
        if row['тип'] == kind:
            time += float(row['минуты'])
    
    return round(time, 1)


def to_csv(counts : dict) -> str:
    s = 'тип,количество\n'

    for kind, count in sorted(counts.items()):
        s += f"{kind},{count}\n"

    return s

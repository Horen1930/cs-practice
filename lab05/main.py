from tablestats import *

def main():
    path = input()

    with open(path, encoding="utf-8") as table:
        rows = read_rows(table)


    with open('summary.csv', 'w', encoding='utf-8') as out:
        out.write(to_csv(count_types(rows)))


    count = len(rows)
    types = len(count_types(rows))
    time_error = total_minutes(rows, 'ошибка')

    return f"{count}\n{types}\n{time_error}"


if __name__ == "__main__":
    print(main())
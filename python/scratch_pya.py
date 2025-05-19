import pyarrow as pa

if __name__ == "__main__":
    days = pa.array([1, 12, 17, 23, 28], type=pa.int8())
    months = pa.array([1, 3, 5, 7, 1], type=pa.int8())
    years = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int16())
    birthdays = pa.table([days, months, years], names=["days", "months", "years"])

    print(f"days array, type: {type(days)}, is array: {isinstance(days, pa.Array)}, data: {days}")
    print(f"months array, type: {type(months)}, is array: {isinstance(months, pa.Array)}, data: {months}")
    print(f"years array, type: {type(years)}, is array: {isinstance(years, pa.Array)}, data: {years}")
    print(f"birthdays table, type: {type(birthdays)}, is table: {isinstance(birthdays, pa.Table)}, data: {birthdays}")

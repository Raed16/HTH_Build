import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

dogbite_data = pandas.read_csv("Dog_Bite_Data.csv")

print(dogbite_data)
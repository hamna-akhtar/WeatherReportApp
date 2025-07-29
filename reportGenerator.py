from utils import *

def get_year_report(input_dir_path, files, year):
    max_temp = float("-inf")
    min_temp = float("inf")
    max_humid = float("-inf")
    max_temp_row = None
    min_temp_row = None
    max_humid_row = None

    found = False
    for filepath in files:
        if year in filepath.split("_"):
            found = True
            df = csv_to_df(input_dir_path, filepath)

            if max_temp < df['Max TemperatureC'].max():
                max_temp = df['Max TemperatureC'].max()
                max_temp_row = df.iloc[df['Max TemperatureC'].idxmax()]
            if min_temp > df['Min TemperatureC'].min():
                min_temp = df['Min TemperatureC'].min()
                min_temp_row = df.iloc[df['Min TemperatureC'].idxmin()]
            if max_humid < df['Max Humidity'].max():
                max_humid = df['Max Humidity'].max()
                max_humid_row = df.iloc[df['Max Humidity'].idxmax()]

    if not found:
        print(f"No data found for year {year}")
        return

    if max_temp_row is not None:
        # highest temperature and day
        max_temp = str(int(max_temp_row['Max TemperatureC']))+'C'
        formatted_max_temp_date = max_temp_row['PKT'].strftime('%B %d')
        print(f"Highest: {max_temp} on {formatted_max_temp_date}")
    else:
        print(f"No Highest Temperature found for year {year}")

    if min_temp_row is not None:
        # lowest temperature and day
        min_temp = str(int(min_temp_row['Min TemperatureC']))+'C'
        formatted_min_temp_date = min_temp_row['PKT'].strftime('%B %d')
        print(f"Lowest: {min_temp} on {formatted_min_temp_date}")
    else:
        print(f"No Lowest Temperature found for year {year}")

    if max_humid_row is not None:
        # most humid day and humidity
        max_humid = str(int(max_humid_row['Max Humidity'])) + '%'
        formatted_max_humid_date= max_humid_row['PKT'].strftime('%B %d')
        print(f"Most Humid: {max_humid} on {formatted_max_humid_date}\n")
    else:
        print(f"No Max Humidity found for year {year}")



def get_year_month_report(input_dir_path, files, year, month):
    found = False
    for filepath in files:
        if year in filepath.split("_") and get_month_name(month) in filepath.split("_")[-1].split('.'):
            found = True

            df = csv_to_df(input_dir_path, filepath)
            avg_max_temp = int(df['Max TemperatureC'].mean())
            avg_min_temp = int(df['Min TemperatureC'].mean())
            avg_humid = int(df[' Mean Humidity'].mean())

            print(f"Highest Average: {avg_max_temp}C") if avg_max_temp is not None else print(f"No Highest Average found for {year}/{month}")
            print(f"Lowest Average: {avg_min_temp}C") if avg_min_temp is not None else print(f"No Lowest Average found for {year}/{month}")
            print(f"Average Humidity: {avg_humid}%") if avg_humid is not None else print(f"No Average Humidity found for {year}/{month}")

    if not found:
        print(f"No data for {year}/{month}")



def draw_bars(input_dir_path, files, year, month, option="two"):
    found = False
    for filepath in files:
        if year in filepath.split("_") and get_month_name(month) in filepath.split("_")[-1].split('.'):
            found = True
            df = csv_to_df(input_dir_path, filepath)[['PKT', 'Min TemperatureC', 'Max TemperatureC']]

            print(f"{get_month_name(month)} {year}")
            for i in range(len(df)):
                day = df['PKT'][i].day
                min_temp = int(df['Min TemperatureC'][i])
                max_temp = int(df['Max TemperatureC'][i])
                if option=='one':
                    print(f"{day}{blue('+' * min_temp)}{red('+' * max_temp)}{min_temp}C-{max_temp}C")
                else:
                    print(f"{day}{red('+'*max_temp)}{max_temp}C")
                    print(f"{day}{blue('+'*min_temp)}{min_temp}C")

    if not found:
        print(f"No data for {year}/{month}")
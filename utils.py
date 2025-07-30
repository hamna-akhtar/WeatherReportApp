import os
import pandas as pd
import calendar


class ReadCsv:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def csv_to_df(self, filepath):
        df = pd.read_csv(os.path.join(self.dir_path, filepath))

        if 'PKST' in df.columns:
            df.rename(columns={'PKST': 'PKT'}, inplace=True)

        if df.iloc[-1]['PKT'].startswith("<!--"):
            df = df.iloc[:-1]

        df['PKT'] = pd.to_datetime(df['PKT'], format='%Y-%m-%d', errors='coerce')
        df['Max TemperatureC'] = pd.to_numeric(df['Max TemperatureC'], errors='coerce')
        df['Min TemperatureC'] = pd.to_numeric(df['Min TemperatureC'], errors='coerce')
        df[' Mean Humidity'] = pd.to_numeric(df[' Mean Humidity'], errors='coerce')

        return df


class Util:
    @staticmethod
    def txt_to_csv(input_dir_path, files):
        for filepath in files:
            filename = os.path.splitext(filepath)[0]
            if filepath.endswith('.txt'):
                os.rename(os.path.join(input_dir_path, filepath), os.path.join(input_dir_path, filename + '.csv'))

    @staticmethod
    def get_month_name(month_no):
        return calendar.month_name[int(month_no)][:3]

    @staticmethod
    def red(s):
        return f"\033[91m{s}\033[00m"

    @staticmethod
    def blue(s):
        return f"\033[96m{s}\033[00m"

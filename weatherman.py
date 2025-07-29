import argparse
from reportGenerator import *

parser = argparse.ArgumentParser()
parser.add_argument("-e", help="Year for Report")
parser.add_argument("-a", help="Year/Month for Report")
parser.add_argument("-c", help="Year/Month for 2 bars")
parser.add_argument("-f", help="Year/Month for 1 bar")
parser.add_argument("d", help="Directory Path")
args = parser.parse_args()

input_dir_path = args.d
files = os.listdir(input_dir_path)
txt_to_csv(input_dir_path, files)

if args.a:
    try:
        year, month = args.a.split('/') if '/' in args.a else (args.a, None)
        if month:
            if len(year)>0:
                print(f"Report for {year}/{month}")
                get_year_month_report(input_dir_path, files, year, month)
            else:
                print("No year specified")
        else:
            print(f"Report for {year}")
            get_year_report(input_dir_path, files, year)
    except Exception as e:
        print(e)

elif args.e:
    try:
            year, month = args.e.split('/') if '/' in args.e else (args.e, None)
            if month:
                if len(year)>0:
                    print(f"Report for {year}/{month}")
                    get_year_month_report(input_dir_path, files, year, month)
                else:
                    print("No year specified")
            else:
                print(f"Report for {year}:")
                get_year_report(input_dir_path, files, year)
    except Exception as e:
        print(e)

elif args.c:
    try:
        year, month = args.c.split('/') if '/' in args.c else (args.c, None)
        if year and month:
            print(f"Two bars each day for {year}/{month}:")
            draw_bars(input_dir_path, files, year, month, "two")
        else:
            if not year:
                print("No year specified")
            if not month:
                print("No month specified")
    except Exception as e:
        print(e)

elif args.f:
    try:
        year, month = args.f.split('/') if '/' in args.f else (args.f, None)
        if year and month:
            print(f"Two bars each day for {year}/{month}:")
            draw_bars(input_dir_path, files, year, month, "one")
        else:
            if not year:
                print("No year specified")
            if not month:
                print("No month specified")
    except Exception as e:
        print(e)
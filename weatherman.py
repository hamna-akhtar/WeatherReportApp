import argparse
import sys
from reportGenerator import *


class HandleInputArgs:
    def __init__(self, input_dir_path, files):
        self.args = None
        self.dir_path = input_dir_path
        self.files = files
        self.genReport = ReportGenerator(dir_path=self.dir_path, files=self.files)

    def handle_args_for_report(self, args):
        self.args = args
        try:
            year, month = self.args.split('/') if '/' in self.args else (self.args, None)
            if month:
                if len(year) > 0:
                    print(f"Report for {year}/{month}\n")
                    self.genReport.get_year_month_report(year, month)
                else:
                    print("No year specified")
            else:
                print(f"Report for {year}\n")
                self.genReport.get_year_report(year)
        except Exception as e:
            print(e)


    def handle_args_for_bars(self, args, option):
        self.args = args
        try:
            year, month = self.args.split('/') if '/' in self.args else (self.args, None)
            if year and month:
                self.genReport.draw_bars(year, month, option)
            else:
                if not year:
                    print("No year specified")
                if not month:
                    print("No month specified")
        except Exception as e:
            print(e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help="Year for Report")
    parser.add_argument("-a", help="Year/Month for Report")
    parser.add_argument("-c", help="Year/Month for 2 bars")
    parser.add_argument("-f", help="Year/Month for 1 bar")
    parser.add_argument("d", help="Directory Path")
    args = parser.parse_args()

    input_dir_path = args.d
    files = os.listdir(input_dir_path)
    Util.txt_to_csv(input_dir_path, files)

    inputHandler = HandleInputArgs(input_dir_path, files)
    if args.a:
        inputHandler.handle_args_for_report(args.a)
    elif args.e:
        inputHandler.handle_args_for_report(args.e)
    elif args.c:
        inputHandler.handle_args_for_bars(args.c, "two")
    elif args.f:
        inputHandler.handle_args_for_bars(args.f, "one")
    else:
        print("Not enough arguments given")


if __name__ == '__main__':
    sys.exit(main())

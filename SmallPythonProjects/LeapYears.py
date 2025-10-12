#-----------imports------------------
import csv

# -------------functions------------------
class leapYearCalculations:

    def is_leap_year(year):
        # checks value is a leap year and returns boolean value
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False

    def rangeYears(start, end):
        leapYears = []
        count = 0
        # iterates over a range of years and calls is_leap_year()
        for i in range(start, end+1):
            if leapYearCalculations.is_leap_year(i) == True:
                print(i)
                leapYears.append(i)
                count += 1
        print("Number of leap years is: ", count)
        return leapYears

class CSVEdit:
    def __init__(self, filename):
        self.filename = filename

    def saveValues(self, leap_years):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Leap Years'])
            for year in leap_years:
                writer.writerow([year])



def checkValues(num):  # checks inputs are positive
    if num < 0:
        newNum = int(input("Enter positive year: "))
        return newNum
    else:
        return num


def menu():  # offers user options
    print('''
Options:
1. Check if year is a leap year
2. Output all leap years in given range
3. Export leap years to text file
4. Import leap years from text file
5. Leave program''')
    option = input('Enter number: ')

    if option == '1':
        print(leapYearCalculations.is_leap_year(checkValues(int(input('Enter year: ')))))

    elif option == '2':
        leapYearCalculations.rangeYears(checkValues(int(input('Start range year: '))),
                                         checkValues(int(input('End range year: '))))
        
    elif option == '3':
        print('Select range of years to export to csv file')
        leapYears = leapYearCalculations.rangeYears(checkValues(int(input('Start range year: '))),
                                         checkValues(int(input('End range year: '))))
        fileName = input('Enter file name to save to: ')
        csv_editor = CSVEdit(fileName + '.csv')
        csv_editor.saveValues(leapYears)
        print('Leap years saved! ')

    elif option == '4':
        fileName = input('Enter file name: ')
        try:
            with open(fileName + '.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                print("Leap Years from file:")
                for row in reader:
                    print(row[0])
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")

    elif option == '5':
        exit('Bye Bye')


# -------------main program------------------------

obj = leapYearCalculations()

while True:
    menu()

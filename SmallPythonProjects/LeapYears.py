#-------------functions------------------
class leapYearCalculations:
      def is_leap_year(year):                         # checks value is a leap year and returns boolean value
            if year % 100 == 0:
                  if year % 400 == 0:
                        return True
            else:
                  if year % 4 == 0:
                        return True
                  else:
                        return False

      def rangeYears(start, end):   
            count = 0
                                          # iterates over a range of years and calls is_leap_year()
            for i in range (start, end+1):
                  if leapYearCalculations.is_leap_year(i) == True:
                        print(i)
                        count = +1
                  print(count)


def checkValues(num):                           # checks inputs are positive
      if num < 0:
            newNum = int(input("Enter positive year: "))
            return newNum
      else:
            return num


def menu():                                           # offers user options
      print('''
Options:
1. Check if year is a leap year
2. Output all leap years in given range
3. Export leap years to text file
4. Leave program''')
      option = input('Enter number: ')

      if option == '1':
            year = checkValues(int(input('Enter year: ')))
            print(leapYearCalculations.is_leap_year(year))
      elif option == '2':
            rangeStart = checkValues(int(input('start range year: ')))
            rangeEnd = checkValues(int(input('end range year: ')))
            leapYearCalculations.rangeYears(rangeStart, rangeEnd)
      elif option == '3':
            saveValues()
      elif option == '4':
            exit('Bye Bye')

#-------------main program------------------------

while True:
      menu()

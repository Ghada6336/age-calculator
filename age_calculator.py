from datetime import datetime, timedelta, time


def check_birthdate(year, month, day):
        
        birthday = datetime(year, month, day)
        if birthday < datetime(2020, 2, 5):
                return True
        else: 
                return False
        
                        
def calculate_age(year, month, day):
        if check_birthdate(year, month, day)== True:
         
                years = 2020 - year -((2, 5) < (month, day))
                print("You are" ,years,"years old")
        elif check_birthdate(year, month, day)== False:
                print ("invalid")
                

def main():
        year = int(input('Enter year of birth:'))
        month = int(input('Enter month of birth: '))
        day = int(input('Enter day of birth: '))
        print (calculate_age(year, month, day))
       
         

if __name__ == '__main__':
	main()

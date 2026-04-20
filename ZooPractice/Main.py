# Main.py
# driver file for Zoo Keeper's Challenge
# last updated 4/20/26 by LA

from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear

from _datetime import date

#create lists of the species

list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

# This is needed for the calcuation for birthdays.

current_date=date.today()
current_year=current_date.year

def calc_birth_date(the_season, the_year):
        year_of_birthday = int(current_year)-int(the_year)
        the_birth_day=""

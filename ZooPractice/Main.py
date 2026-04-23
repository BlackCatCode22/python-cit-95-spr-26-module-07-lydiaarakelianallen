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

        if "spring" in the_season:
                the_birth_day = str(year_of_birthday) + "-03-21"

        elif "summer" in the_season:
                the_birth_day = str(year_of_birthday) + "-06-21"

        elif "fall" in the_season:
                the_birth_day = str(year_of_birthday) + "-09-21"

        elif "winter" in the_season:
                the_birth_day = str(year_of_birthday) + "-12-21"

        else:
                the_birth_day = str(year_of_birthday) + "-01-01"

        return the_birth_day

def process_one_line(one_line):
        #create variables to help parse arringAnimals.txt
        a_species = ""
        a_sex = ""
        age_in_years = 99
        season = ""
        color = ""
        weight = ""
        origin_01 = ""
        origin_02 = ""

        print(one_line)

        group_of_words = one_line.strip().split(",")
        print(group_of_words)

        single_words = group_of_words[0].strip().split(" ")
        age_in_years = single_words[0]
        a_sex = single_words[3]
        a_speech = single_words[4]
        single_words = group_of_words[1].strip().split(" ")
        season = single_words[2]
        color = single_words[2].strip();
        weight = single_words[3].strip();
        origin_01 = single_words[4].strip();
        origin_02 = single_words[5].strip();

        from zoo = origin_01 + ", " + origin_02

        birth_day = calc_birth_date(season, age_in_years)

        if "hyena" in a_species:
                # creat a hyena object.
                my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_hyena.name = Hyena.get_hyena_name(my_hyena)
                my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas).zfill(2)
                # add to the hyena list
                list_of_hyenas.append(my_hyena)


        if "lion" in a_species:
                # creat a lion object.
                my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_lion.name = Lion.get_lion_name(my_lion)
                my_lion.animal_id = "Li" + str(Lion.numOfLions).zfill(2)
                # add to the lion list
                list_of_lions.append(my_lion)


        if "tiger" in a_species:
                # creat a tiger object.
                my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_tiger.name = Tiger.get_tiger_name(my_tiger)
                my_tiger.animal_id = "Ti" + str(Tiger.numOfTigers).zfill(2)
                # add to the Tiger list
                list_of_tigers.append(my_tiger)


        if "Bear" in a_species:
                # creat a bear object.
                my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_bear.name = Bear.get_bear_name(my_bear)
                my_bear.animal_id = "Be" + str(Bear.numOfBears).zfill(2)
                # add to the bear list
                list_of_bears.append(my_bear)

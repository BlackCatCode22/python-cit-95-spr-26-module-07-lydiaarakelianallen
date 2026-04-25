# Main.py
# driver file for Zoo Keeper's Challenge
# last updated 4/20/26 by LA

from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear

from datetime import date

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

        # file.write(one_line)

        group_of_words = one_line.strip().split(",")
        # file.write(group_of_words)

        single_words = group_of_words[0].strip().split(" ")
        age_in_years = single_words[0]
        a_sex = single_words[3]
        a_species = single_words[4]


        season = group_of_words[1].strip().split(" ")[2]

        color = group_of_words[2].strip();
        weight = group_of_words[3].strip();

        origin_01 = group_of_words[4].strip();
        origin_02 = group_of_words[5].strip();
        from_zoo = origin_01 + ", " + origin_02

        birth_day = calc_birth_date(season, age_in_years)

        if "hyena" in a_species:
                # creat a hyena object.
                my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_hyena.name = Hyena.list_of_hyena_names.pop(3)
                my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas).zfill(2)
                # add to the hyena list
                list_of_hyenas.append(my_hyena)


        if "lion" in a_species:
                # creat a lion object.
                my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_lion.name = Lion.list_of_lion_names.pop(3)
                my_lion.animal_id = "Li" + str(Lion.numOfLions).zfill(2)
                # add to the lion list
                list_of_lions.append(my_lion)


        if "tiger" in a_species:
                # creat a tiger object.
                my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_tiger.name = Tiger.list_of_tiger_names.pop(3)
                my_tiger.animal_id = "Ti" + str(Tiger.numOfTigers).zfill(2)
                # add to the Tiger list
                list_of_tigers.append(my_tiger)


        if "bear" in a_species:
                # creat a bear object.
                my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
                #fill in name and ID
                my_bear.name = Bear.list_of_bear_names.pop(3)
                my_bear.animal_id = "Be" + str(Bear.numOfBears).zfill(2)
                # add to the bear list
                list_of_bears.append(my_bear)

file_path = r"C:\Users\lydia\Downloads\arrivingAnimals.txt"
with open(file_path, "r") as file:
        for line in file:
                process_one_line(line)

with open("zooPopulation.txt", "w") as file:
        print(f"Number of animals created: {Animal.numOfAnimals}")

        print(f"Number of Hyenas created: {Hyena.numOfHyenas}")

        print(f"Number of lions created: {Lion.numOfLions}")

        print(f"Number of tigers created: {Tiger.numOfTigers}")

        print(f"Number of Bears created: {Bear.numOfBears}")

        print("\nZookeeper's Challenge Zoo Population")

        print("\nHyena Habitat:")

        for hyena in list_of_hyenas:
                print(hyena.animal_id + "; " + hyena.name + "; birthdate:" + str(hyena.birth_date)+ "; "
                      +hyena.color+"; "+hyena.sex+"; "+hyena.weight+"; "+hyena.originating_zoo+"; arrived: "+str(hyena.date_arrival)+"")



        print("\nLion Habitat:")

        for lion in list_of_lions:
                print(lion.animal_id + "; " + lion.name + "; birthdate:" + str(lion.birth_date)+ "; "
                      +lion.color+"; "+lion.sex+"; "+lion.weight+"; "+lion.originating_zoo+"; arrived: "+str(lion.date_arrival)+"")



        print("\nTiger Habitat:")

        for tiger in list_of_tigers:
                print(tiger.animal_id + "; " + tiger.name + "; birthdate:" + str(tiger.birth_date)+ "; "
                      +tiger.color+"; "+tiger.sex+"; "+tiger.weight+"; "+tiger.originating_zoo+"; arrived: "+str(tiger.date_arrival)+"")



        print("\nBear Habitat:")

        for bear in list_of_bears:
                print(bear.animal_id + "; " + bear.name + "; birthdate:" + str(bear.birth_date)+ "; "
                      +bear.color+"; "+bear.sex+"; "+bear.weight+"; "+bear.originating_zoo+"; arrived: "+str(bear.date_arrival)+"")


        file.write("Zookeeper's Challenge Zoo Population\n")

        file.write("\n\nHyena Habitat:\n\n")

        for hyena in list_of_hyenas:
                file.write(hyena.animal_id + "; " + hyena.name + "; birthdate:" + str(hyena.birth_date)+ "; "
                      +hyena.color+"; "+hyena.sex+"; "+hyena.weight+"; "+hyena.originating_zoo+"; arrived: "+str(hyena.date_arrival)+"\n")



        file.write("\n\nLion Habitat:\n\n")

        for lion in list_of_lions:
                file.write(lion.animal_id + "; " + lion.name + "; birthdate:" + str(lion.birth_date)+ "; "
                      +lion.color+"; "+lion.sex+"; "+lion.weight+"; "+lion.originating_zoo+"; arrived: "+str(lion.date_arrival)+"\n")



        file.write("\n\nTiger Habitat:\n\n")

        for tiger in list_of_tigers:
                file.write(tiger.animal_id + "; " + tiger.name + "; birthdate:" + str(tiger.birth_date)+ "; "
                      +tiger.color+"; "+tiger.sex+"; "+tiger.weight+"; "+tiger.originating_zoo+"; arrived: "+str(tiger.date_arrival)+"\n")



        file.write("\n\nBear Habitat:\n\n")

        for bear in list_of_bears:
                file.write(bear.animal_id + "; " + bear.name + "; birthdate:" + str(bear.birth_date)+ "; "
                      +bear.color+"; "+bear.sex+"; "+bear.weight+"; "+bear.originating_zoo+"; arrived: "+str(bear.date_arrival)+"\n")


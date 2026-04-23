from ZooPractice.Animal import Animal

class Hyena(Animal):
    # create a static class variable to keep track of the number of hyenas created
    numOfHyenas = 0

    # create the hyena sound
    hyena_sound= "laugh... laugh"

    #create a list of hyena names.
    list_of_hyena_names = []

    file_path= r"C:\Users\lydia\Downloads\animalNames.txt"
    with open(file_path,'r') as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num == 3:
                list_of_hyena_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id",birth_date="2099-01-01", color="_color", sex="a_sex",weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # incriment the static variable numOfHyenas when a new Hyena object is created
        Hyena.numOfHyenas += 1

        #call the constructor of the parent class (Animal) with 'Hyena' as the species
        super().__init__("hyena", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

    def make_sound(self):
from Animal import Animal

class Lion(Animal):
    # create a static class variable to keep track of the number of hyenas created
    numOfLions = 0

    #create a list of hyena names.
    list_of_lion_names = []

    file_path= r"C:\Users\lydia\Downloads\animalNames.txt"
    with open(file_path,'r') as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num == 7:
                list_of_lion_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id",birth_date="2099-01-01", color="_color", sex="a_sex",weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # incriment the static variable numOflions when a new lion object is created
        Lion.numOfLions += 1

        #call the constructor of the parent class (Animal) with 'lion' as the species
        super().__init__("lion", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)


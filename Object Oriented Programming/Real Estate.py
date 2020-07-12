# Object inheritance practice... We have a Property object that is a
# superclass of an Apartment subclass and a House subclass. Every property gets a
# square footage, bedroom count and bathroom count (since both apartments and
# houses will want those. For the purposes of this application, only houses get
# multiple stories and garages.

def ask_question(q, resp_list):
    return input(q.format(', '.join(resp_list)))

class Property:
    def __init__(self, address, sq, bed_ct, br_ct):
        self.address = address
        self.square_feet = sq
        self.bedroom_count = bed_ct
        self.bathroom_count = br_ct

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.bedroom_count))
        print("bathrooms: {}".format(self.bathroom_count))
        print()

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds = input("Enter number of bedrooms: "),
                    baths = input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)

class Apartment(Property):
    valid_landlord_ratings = ['*' * n for n in range(1,6)]
    valid_laundry_status = ['In Unit','In Complex','Not on site']

    def __init__(self, landlord_rating, washer_dryer_status, furnished=False, rent, **kwargs):
        super().__init__(**kwargs)
        self.landlord_rating = landlord_rating
        self.washer_dryer_status = washer_dryer_status
        self.rent = rent
        self.furnished = furnished

    def prompt_init(self):
        parent_init = super().prompt_init()
        laundry, landlord_rating = '', ''
        while laundry.lower() not in Apartment.valid_laundry_status:
            laundry = ask_question("What laundry facilities does this have? {}", Apartment.valid_laundry_status)
        while landlord_rating not in Apartment.valid_landlord_ratings:
            laundry = ask_question("What is the landlord rating? {}", Apartment.valid_landlord_ratings)

class House(Property):
    def __init__(self, story_count, garage=False,  **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.story_count = story_count

class Agent:
    property_list = []

    def __init__(self, name='', company=''):
        self.name = name
        self.company = company

    def list_properties(self, show_all=False):

    def add_property(self, property_type, purchase_type):

    def remove_property(self):


if __name__ == '__main__':







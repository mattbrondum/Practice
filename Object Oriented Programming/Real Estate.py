# Object inheritance practice... We have a Property object that is a
# superclass of an Apartment subclass and a House subclass. Every property gets a
# square footage, bedroom count and bathroom count (since both apartments and
# houses will want those. For the purposes of this application, only houses get
# multiple stories and garages.

from random import randint


def ask_question(q, resp_list):
    return input(q.format(', '.join(resp_list)))

class Property:
    current_property_ids = []

    def __init__(self, address, sq, bed_ct, br_ct):
        # Generate a new random id that's not already taken
        new_id = randint(0,999999)
        while new_id in Property.current_property_ids:
            new_id = randint(0,999999)
        self.ID = new_id
        self.address = address
        self.square_feet = sq
        self.bedroom_count = bed_ct
        self.bathroom_count = br_ct

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("ID: {}".format(self.ID))
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.bedroom_count))
        print("bathrooms: {}".format(self.bathroom_count))

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds = input("Enter number of bedrooms: "),
                    baths = input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)

class Apartment(Property):
    valid_landlord_ratings = ['*' * n for n in range(1,6)]
    valid_laundry_status = ['In Unit','In Complex','Not on site']

    def __init__(self, landlord_rating, washer_dryer_status, furnished=False, rent=True, **kwargs):
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
    type_map = {('house', 'rental'): HouseRental
                ,('apartment', 'rental'): ApartmentRental
                ,('house', 'purchase'): HousePurchase
                ,('house', 'rental'): ApartmentRental}

    def __init__(self, name='', company=''):
        """Create a new agent with a name, company, blank property listing"""
        self.name = name
        self.company = company
        self.property_list = []
        self.list_properties()
        print("New agent named {} from company {}. No properties.")

    def list_properties(self, show_all=False):
        if len(self.property_list)>0:
            for prop in self.property_list:
                prop.display()
        else:
            print("This agent has no properties. Try adding one")
            
    def add_property(self):
        """Add a property to the agent's listing"""
        prop_type = ask_question("What kind of property do you want to add? {}", ['Apartment','House'])
        pay_type = ask_question("How do you want to pay for it? {}", ['Purchase','Rental'])
        PropertyClass = self.type_map[(prop_type, pay_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def remove_property(self):
        """Remove a property from an agent's listing"""
        self.list_properties()
        while True:
            prop_to_rm = input("Which property ID would you like to remove?")
            try:
                self.property_list.remove(prop_to_rm)
                break
            except:
                print("Invalid ID... try again")


if __name__ == '__main__':
    Agent()

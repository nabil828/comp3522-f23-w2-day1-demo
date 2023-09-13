# a class
class Cat:
    # a method
    def __init__(self, name, age, favorite_food):
        self.__age = age # _age is private
        self.name = name # name is public
        self._food_prefs = favorite_food
        # increment the number of cats
        Cat.num_cats += 1

    # def get_age(self):
    #     return self.__age
    
    def __repr__():
        return "Cat(name={}, age={})".format(self.name, self.__age)
    
    def __str__():
        return """My name is Tobias and I'm {} years old.
                love eating {}
                I have {} lives remaining"""
    
    # Accessors
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.name
    
    # Mutators
    def set_age(self, age):
      if(age < 0):
        print("Age cannot be negative")
      else:
        self.__age = age

    # properties
    age = property(get_age, set_age)

    # a static method
    @staticmethod
    def get_cat_sound():
        return "Meow"
    
    # a static variable 
    num_cats = 0

    # a class method
    def get_num_cats(cls):
        return cls.num_cats 

# objects
a_cat = Cat("Garfield", 40, "Lasagna")
a_cat._age = 50 # you are not supposed to do this
a_cat.name = "Garfield2"
print(a_cat.get_age())

# to actually overwrite the age
a_cat._Cat__age = 50
print(a_cat.get_age())

a_cat.age = 50 # this is the same as a_cat.set_age(50)
print(a_cat.age) # this is the same as a_cat.get_age()


another_cat = Cat("Sylvester", 50, "Tweety")

print(a_cat.get_cat_sound())
print(Cat.get_cat_sound())
print(another_cat.get_cat_sound())

print(Cat.num_cats)
print(a_cat.num_cats)
print(another_cat.num_cats)
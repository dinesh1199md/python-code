class Dog:
    def sound(self):
        return "Woof!"
class Cat:
    def sound(self):
        return "Meow!"
class Cow:
    def sound(self):
        return "Moo!"
def animal_sound(animal):
    print(animal.sound())
# Create instances of each animal
dog = Dog()
cat = Cat()
cow = Cow()

# Call the function with different animal instances
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(cow)  # Output: Moo!


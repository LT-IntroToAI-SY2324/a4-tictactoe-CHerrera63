# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    # functions that start with __ are not intended to be called directly; self = current relevant object
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
        """Creates an instance of the dog class and
        sets attributes"""
        self.name = n
        self.fur_color = fc
        self.age = a
        self.fav_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """return a string representation of a dog"""
        s = "Dog's name is " + self.name + "\n"
        s += "and age is " + str(self.age) + "\n"
        s += "and fur color is " + self.fur_color + "\n"
        s += "they have played fetch " + str(self.fetch_count) + " times\n"
        return s
        
    def play_fetch(self, num_times):
        self.fetch_count += num_times

    def paint_dog(self, color):
            self.fur_color = color

my_dog = Dog("logan", "black", 7, "salmon")
chrisdog = Dog("luna", "black and white", 6, "tortillas")

print(my_dog)
print(chrisdog)

my_dog.play_fetch(20)
chrisdog.play_fetch(3)

print(my_dog)
print(f"{chrisdog.name} has played fetch {chrisdog.fetch_count} times")

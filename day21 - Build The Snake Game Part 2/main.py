class Animal:
    def __init__(self):
        self.num_eyes = 2;
    
    def breathe(self):
        print("Inhale, Exhale");

# inheritance
class Fish(Animal):
    # allow this class to inheritate the all the attributes and method on super class(Animal)
    def __init__(self):
        super().__init__();
    
    # you can added extra modified code to the parent class(super class)'s method, with the same name
    def breathe(self):
        super().breathe();
        print("doing this under water");
        
    def swim(self):
        print("moving in water.");

nemo = Fish();
nemo.swim();

# after super.__init__() method is called, you can access the Animal method/properties from Fish
nemo.breathe();
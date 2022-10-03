from emoji import emojize

"""
say that you have a bathtub and the water when it reaches more than
the 50 centimeter(for example) level of bathtub, the water will drain by
the overflow(the hole which the water will sink automatically
when reaching the level of the bathtub height)
"""
waterLevel = 50;        # 50 cm

if waterLevel > 50:
    print("Drain water");
else:
    print("Continue");
    
"""
now maybe you're selling ticket for riding the rollercoaster.
you have rules that the person that would play, should be height
120cm long. if it's not, then the person won't allowed to play.
"""
print("Welcome to the rollercoaster!");
height = int(input("What is your height in cm? "));

if height >= 120:
    bill = 0;
    print(f"You can riding the {emojize('🎢')}");    
    """ 
    now you need to code the price problem. When the person age is
    less than 12 years old it should pay for 5$, less than 18, but
    more than 12 it should pay 12$, if the person more than 18 then
    it should pay for 15$ 
    """
    age = int(input("What's your age? "));
    
    if age < 12:
        bill = 5;
        print("Please pay 5$");
    elif age <= 18:
        bill = 12;
        print("Please pay 12$");
    else:
        bill = 15;
        print("Please pay 15$");
    
    """
    you can offer the person the memory when they playing the 🎢
    with charge only 3$.
    """
    wantsPhotos = input("Do you want a photo taken? Y or N.");
    
    if wantsPhotos == "Y":
        bill += 3;
    
    print(f"Your bill is {bill}$");
        
else:
    print(f"You can play the roller coaster {emojize('😔')}");


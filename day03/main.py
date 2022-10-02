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

if height > 120:
    print("you can ride the rollercoaster!");
else:
    print("you can't ride the rollercoaster")
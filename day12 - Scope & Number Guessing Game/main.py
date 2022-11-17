####### SCOPE #####

enemies = 1;

def increase_enemies():
    # local scope
    enemies = 2;
    print(f"enemies inside function: {enemies}");

increase_enemies();
print(f"enemies outside function: {enemies}");

# how to modify the global scope variable
def another_increase_enemies():
    global enemies;
    enemies += 1;
    print(f"enemies inside another function: {enemies}");

another_increase_enemies();
print(f"enemies after increase on another function: {enemies}");
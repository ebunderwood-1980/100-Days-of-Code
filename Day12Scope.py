# Namespaces - Local vs Global scope.

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function:  {enemies}") #Enemies = 2, has access to enemies inside of function

increase_enemies()
print(f"Enemies outside of function:  {enemies}") #Enemies = 1, does not have access to Enemies inside of function.

def is_prime(num):
    for devisor in range(2, num):
        if num % devisor == 0:
            return False
    return True


for i in range(1,25):
    print(f"{i} is prime:  {is_prime(i)}")


# Modifying Global Scope
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function:  {enemies}")

increase_enemies()
print(f"Enemies outside function:  {enemies}")

# Global scope is good to use for constantes.  Usually differentiated by using ALL CAPS

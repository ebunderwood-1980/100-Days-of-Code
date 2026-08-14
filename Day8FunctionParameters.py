def greet():
    print("Hello world")
    print("What what in the butt")
    print("Third line of stuff")


def greetWithName(name):
    print(f"Hello, {name}.")


greet()
greetWithName("Eric")


def lifeInWeeks(current_age):
    weeksLeft = (90 - current_age) * 52
    print(f"You have {weeksLeft} weeks to live")


lifeInWeeks(46)


def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}")


greet_with("Eric", "Gallup")
greet_with(location="Gallup", name="Sarah")

import random

randInt = random.randint(1, 5)
print(randInt)

randFloat = random.random()
print(randFloat)

randUniform = random.uniform(1, 10)
print(randUniform)

# Creates a program that prints heads or tails
flip = random.randint(0, 1)
if flip == 0:
    print("Heads")
else:
    print("Tails")

states = ["Delaware", "Texas"]
# Print entire list
print(states)
states.append("New Mexico")
states.extend(["Utah", "Arizona"])  # Adding a list to a pre-existing list

# Business card roulette
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
unluckyPerson = friends[random.randint(0, len(friends) - 1)]
print(f"The unlucky person is {unluckyPerson}")

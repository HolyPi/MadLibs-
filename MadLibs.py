
print ("Enter an Animal.")
Animal = [input()]

print ("Enter 2 PastVerbs.")
PastVerbs = [input(), input()]

print ("Enter a Verb.")
Verb = [input()]

def show():

    print("Alice was walking through the carved path of a densely packed forest,")
    print("when she suddenly saw a " + Animal[0],)
    print(" (What are you doing here? Did you lose your way?) ")
    print(" And it just disappeared into thin air with the most mischievous smile. ")
    print(" Walking further into the carved path led her into an even more obscure place, so she " + PastVerbs[0],
    "and " + PastVerbs[1] + " at full speed out of the forest. ")
    print(Verb[0] + " she finally came into a less densely and obscure place. ")
    print(" She felt a ray of light against her face, and looked up. ")
    print(" She saw the hole she probably fell into. ")
    print(" But it was too far away for her to reach. ")

show()

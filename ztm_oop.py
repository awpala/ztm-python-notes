from modules.ztm_oop_classes import *


# intro to OOP
obj = BigObject()


# encapsulation and abstraction
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player1.run()
PlayerCharacter.adding_things(1, 2)
PlayerCharacter.adding_more_things(1, 2)


# inheritance and polymorphism
is_subclass = issubclass(Wizard, User) # True - Wizard is a subclass of User
is_subclass = issubclass(User, object) # True - all objects in Python derive from `object`, which provides dunders`
wizard1 = Wizard('Merlin', 50)
is_instance = isinstance(wizard1, Wizard) # True
is_instance = isinstance(wizard1, User)   # True
is_instance = isinstance(wizard1, object) # True
wizard1.sign_in()
archer1 = Archer('Mitch', 60)
archer1.sign_in()
wizard1.attack()
archer1.attack()


# multiple inheritance & MRO
print('\nmro for class D:\n\t', D.mro())
print(D.num) # 1 - D inherits `num` from B

'EOF'

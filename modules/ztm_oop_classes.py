# intro to OOP
class BigObject:
  pass


# encapsulation and abstraction
class PlayerCharacter:
  # class object attribute - static across object instances
  membership: bool = True

  def __init__(self, name: str, age: int):
    if (self.membership): # class object attribute is available on self
      self.name = name
      self._age = age # private variable _age

  def run(self):
    if (PlayerCharacter.membership): # class object attribute is also available on class
      print(f'{self.name} is running')

  @classmethod # N.B. decorators are discussed in a later lesson
  def adding_things(cls, num1: int, num2: int) -> int:
    return num1 + num2
  
  @staticmethod
  def adding_more_things(num1: int, num2: int) -> int:
    return num1 + num2


# inheritance and polymorphism
class User:
  def __init__(self, name: str, weapon: str):
    self.name = name
    self.weapon = weapon

  def sign_in(self) -> None:
    print(f'{self.name} logged in')
  
  def attack(self, attacks: int) -> None:
    attacks -= 1
    print(f'attacking, {attacks} {self.weapon} left')


class Wizard(User):
  def __init__(self, name: str, power: int):
    super().__init__(name, 'spells') # `super()` accesses the base class (e.g., `User`)
    self.power = power
  
  def attack(self) -> None:
    super().attack(self.power)


class Archer(User):
  def __init__(self, name: str, arrows: int):
    super().__init__(name, 'arrows')
    self.arrows = arrows

  def attack(self) -> None:
    super().attack(self.arrows)


# multiple inheritance & MRO
'''
class hierarchy:
    A
  /   \ 
 B     C
  \   /
    D 
'''
class A:
  num = 10

class B(A):
  pass

class C(A):
  num = 1

# MRO: D -> B -> C -> A
class D(B, C):
  pass

# more complex examples:
# https://data-flair.training/blogs/python-multiple-inheritance/

# N.B. Python MRO algorithm is based on DFS

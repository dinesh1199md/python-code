"""Python Dataclasses
Python Classes used for storing data objects are called Dataclasses. They have certain features like:

Comparison with other objects of the same type is possible.
Stores data, representing a particular data type."""

from dataclasses import dataclass
from typing import Any
"""Note: It is compulsory to specify the datatype of each variable declared. 
If at any point we don’t want to specify the type, set the type as typing.Any."""

@dataclass #annotation indicates that it is a dataclass module
class Self:
   x: str
   name: Any
   age: Any=18
ob = Self("One","dinesh",100)
print(ob.x)
print(ob.name)
print(ob.age)
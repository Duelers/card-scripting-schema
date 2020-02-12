Overview
-
This is all the code and documentation related to developing a json-schema for Duelers card
 scripting.

While the schema itself looks like EBNF, it's mostly being drafted as nested pydantic models, to
automate things like enheritance.

 
 
This process has several parts.
 - Designing the schema theoretically, to be easy to write and understand, while avoiding
  explosive complexity.
 - Using Python's Pydantic to generate the actual json-schema.
 
Examples
 -  
 ```python
from typing import Union, Literal

NumberOperator = Union[Literal['+'], #A number operator is one of the listed strings.
                       Literal['-'],
                       Literal['*'],
                       Literal['/']]
Operator = Union[NumberOperator] #An operator is any of the listed operator types.
# Something typehinted as an Operator could be +, -, *, or /. All other values will raise.
```
 
 ```python
import typing
from typing import Union

import pydantic
from pydantic import BaseModel

import properties, operators, events

InstantaneousEffect = Union[None]  # An effect cannot have a duration, such as killing a minion.
#This is just a stand in to be developed later. Looking for a better solution than None.

class DurationEffectModel(BaseModel): # Ending its name with 'Model' means its abstract. 
    """An continuous effect."""
    end_when_this_leaves_play: bool = False #Since it is given a default, it's optional.
    until: typing.Optional[events.Event] = None 


# An object in the schema with some properties.
class ChangeProperty(DurationEffectModel): #This inherits the fields in DurationEffectModel
    name: str = pydantic.Field('change_property', const=True)
    # property_owner: ? = 'this'  # Still working on a good way to type this. 
    property: properties.UnitProperty  # todo Only allow properties property_owner has? Or just ignore?
    operator: operators.NumberOperator
    by_value: int


DurationEffect = Union[ChangeProperty]
Effect = Union[InstantaneousEffect, DurationEffect]
```



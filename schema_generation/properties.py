import typing

import base
import objects

damage = 'damage'
DamageDealtProperty = typing.Union[
    typing.Literal[damage]
]


class GetVarNumber(base.BaseModel):
    name: typing.Literal['get_var_number']
    var: str
    initial: int = 1


cost = 'cost'

tribes = 'tribes'
faction = 'faction'
abilities = 'abilities'
effects = 'effects'

attack = 'attack'  # A unit's attack value.
max_health = 'max_health'
cur_health = 'cur_health'

cur_mana = 'cur_mana'
max_mana = 'max_mana'

MinionProperty = typing.Union[
    typing.Literal[attack],
    typing.Literal[max_health],
    typing.Literal[cur_health],
    typing.Literal[abilities],

    typing.Literal[faction],

    typing.Literal[cost],
    typing.Literal[tribes]
]

GeneralProperty = typing.Union[
    typing.Literal[attack],
    typing.Literal[max_health],
    typing.Literal[cur_health],
    typing.Literal[abilities],
    typing.Literal[faction],

    typing.Literal[cur_mana],
    typing.Literal[max_mana]
]

UnitProperty = typing.Union[
    typing.Literal[attack],
    typing.Literal[max_health],
    typing.Literal[cur_health],
    typing.Literal[faction],
    typing.Literal[abilities],
]  # A trait something has, such as a minion's attack or a card's cost.

SpellProperty = typing.Union[
    typing.Literal[faction],
    typing.Literal[cost],
    typing.Literal[effects]
]

ArtifactProperty = typing.Union[
    typing.Literal[faction],
    typing.Literal[cost],
    typing.Literal[abilities]
]

Property = typing.Union[MinionProperty, GeneralProperty, UnitProperty,
                        SpellProperty, ArtifactProperty, DamageDealtProperty]


class GetPropertyModel(base.BaseModel):
    """Modify a property of an object."""
    name: typing.Literal['change_property']
    property_owner: objects.Objects = 'this'


class GetProperty(base.BaseModel):
    """Modify a property of an object."""
    property: Property


PropertyOwnerType = typing.TypeVar('PropertyOwnerType')
PropertyType = typing.TypeVar('PropertyType')

Number = typing.Union[GetProperty, GetVarNumber, int]

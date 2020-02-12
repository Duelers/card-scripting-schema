from __future__ import annotations

import typing
from typing import Union

import objects
import players
import base

import properties
import operators
import events


class EffectModel(base.BaseModel):
    description: str = None


class DrawCards(EffectModel):
    """Add cards from the player's deck to their hand."""
    name: typing.Literal['draw_cards']
    player: players.Player = players.you
    num_cards: int = 1


class SetVarObject(EffectModel):
    """Define a scripting variables to the given value."""
    name: typing.Literal['set_var_object']
    var: str
    value: objects.Object


class SetVarNumber(EffectModel):
    """Define a scripting variables to the given value."""
    name: typing.Literal['set_var_number']
    var: str
    value: int


# An effect cannot have a duration, such as killing a minion.
InstantaneousEffect = Union[DrawCards, SetVarObject, SetVarNumber]


class DurationEffectModel(EffectModel):  # model in the name indicates it's abstract.
    """An continuous effect."""
    until: typing.Optional[events.Event] = None


class ChangeProperty(DurationEffectModel):
    """Modify a property of an object."""
    name: typing.Literal['change_property']
    property_owner: objects.Object = "this"
    property: properties.Property  # todo Only allow properties property_owner has? Or just ignore?
    operator: operators.NumberOperator = operators.plus
    by_value: int


# IF YOU USE THE abilities MODULE YOU MUST update_forward_refs() UNDER THE abilities IMPORT.

class AddAbility(DurationEffectModel):
    name: typing.Literal['add_ability']
    to: objects.Object = objects.this
    ability: abilities.Ability


DurationEffect = Union[ChangeProperty, AddAbility]
Effect = Union[InstantaneousEffect, DurationEffect]

import abilities

AddAbility.update_forward_refs()

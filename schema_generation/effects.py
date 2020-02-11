from __future__ import annotations

import typing
from typing import Union

import pydantic

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


# An effect cannot have a duration, such as killing a minion.
InstantaneousEffect = Union[DrawCards]


class DurationEffectModel(EffectModel):  # model in the name indicates it's abstract.
    """An continuous effect."""
    end_when_this_leaves_play: bool = False
    until: typing.Optional[events.Event] = None


class ChangeProperty(DurationEffectModel):
    """Modify a property of an object."""
    name: typing.Literal['change_property']
    property_owner: objects.Object = "this"
    property: properties.Property  # todo Only allow properties property_owner has? Or just ignore?
    operator: operators.NumberOperator
    by_value: int


class AddAbility(DurationEffectModel):
    name: typing.Literal['add_ability']
    to: objects.Object = objects.this
    ability: abilities.Ability


DurationEffect = Union[ChangeProperty, AddAbility]
Effect = Union[InstantaneousEffect, DurationEffect]

import abilities

AddAbility.update_forward_refs()

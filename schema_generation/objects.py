from __future__ import annotations

import typing

import card_types
import generals
import players
import base

import zones

this = "this"
trigger = "trigger"  # The event which causes a triggered effect


class CardSelectionModel(base.BaseModel):
    """Selects cards from out-of-play zones, such as a player's hand."""
    from_zones: typing.Union[
        zones.CardZone,
        typing.List[zones.CardZone]
    ] = zones.hand

    types: typing.Union[
        card_types.CardType,
        typing.List[card_types.CardType]
    ]

    owner: typing.Optional[players.Player] = None


class ChooseCard(CardSelectionModel):
    name: typing.Literal['choose_card']


class ChooseCards(CardSelectionModel):
    name: typing.Literal['choose_cards']
    choose_at_least: typing.Optional[int] = 1
    choose_at_most: typing.Optional[int] = 1


class AllCards(CardSelectionModel):
    name: typing.Literal['all_cards']
    from_zones: typing.Union[
        zones.CardZone,
        typing.List[zones.CardZone]
    ] = zones.in_play
    types: typing.Union[
        card_types.CardType,
        typing.List[card_types.CardType]
    ]
    owner: typing.Optional[players.Player] = None


# Choose unit

class UnitSelectionModel(base.BaseModel):
    types: typing.Union[
        card_types.CardType,
        typing.List[card_types.CardType]
    ] = card_types.minion

    owner: typing.Optional[players.Player] = None
    from_squares: locations.Locations = "everywhere"  # todo this is terrible. Should be locations.everywhere but I
    # can't figure out how to import that without a circular dependency.


class ChooseUnit(UnitSelectionModel):
    name: typing.Literal['choose_unit']


class GetVarObject(base.BaseModel):
    name: typing.Literal['get_var_object']
    var: str


Minion = typing.Union[typing.Literal[this], ChooseCard, ChooseUnit, GetVarObject]  # todo type card selection methods

General = typing.Union[generals.Generals, typing.Literal[this], ChooseCard, ChooseUnit, GetVarObject]  # todo

Spell = typing.Union[typing.Literal[this], ChooseCard, GetVarObject]  # todo

Artifact = typing.Union[typing.Literal[this], ChooseCard, GetVarObject]  # todo

Unit = typing.Union[generals.Generals, typing.Literal[this], ChooseCard, ChooseUnit, GetVarObject]  # todo
Units = typing.Union[Unit, ChooseCards]

Object = typing.Union[typing.Literal[this],
                      typing.Literal[trigger],
                      Minion,
                      General,
                      Spell,
                      Artifact,
                      ChooseCard,
                      GetVarObject]

Objects = typing.Union[
    Object,
    ChooseCards,
    AllCards,
]

import locations

ChooseUnit.update_forward_refs()

# clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
# print(clsmembers)

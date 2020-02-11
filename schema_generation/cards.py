import typing

import card_types
import factions
from base import BaseModel
import abilities as _abilities
import effect as _effects


class CardModel(BaseModel):
    name: str
    cost: int
    faction: factions.Faction = factions.neutral


class MinionCard(CardModel):
    type: typing.Literal[card_types.minion]
    attack: int
    max_health: int
    tribes: typing.List[str] = []
    abilities: typing.Union[
        _abilities.Ability,
        typing.List[_abilities.Ability]
    ]


class SpellCard(CardModel):
    type: typing.Literal[card_types.spell]
    effects: typing.Union[
        _effects.Effect,
        typing.List[_effects.Effect]
    ]


class ArifactCard(CardModel):
    type: typing.Literal[card_types.artifact]
    abilities: typing.Union[
        _abilities.Ability,
        typing.List[_abilities.Ability]
    ]


Card = typing.Union[SpellCard, MinionCard, ArifactCard]

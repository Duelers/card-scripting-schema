import typing
import factions
from base import BaseModel
import abilities as _abilities
import effect as _effects


class CardModel(BaseModel):
    name: str
    cost: int
    faction: factions.Faction = factions.neutral


class MinionCard(CardModel):
    attack: int
    max_health: int
    tribes: typing.List[str] = []
    abilities: typing.Union[
        _abilities.Ability,
        typing.List[_abilities.Ability]
    ]


class SpellCard(CardModel):
    effects: typing.Union[
        _effects.Effect,
        typing.List[_effects.Effect]
    ]


Card = typing.Union[SpellCard, MinionCard]

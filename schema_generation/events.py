from typing import Union

from pydantic import BaseModel


class Summon(BaseModel):
    """On Play"""
    pass  # TODO Clarify this. How to say "when this is played" vs "when a thing is played"?


Event = Union[Summon]  # A thing that happens, such as a turn ending.

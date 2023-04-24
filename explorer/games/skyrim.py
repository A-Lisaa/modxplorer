from dataclasses import dataclass

from ..file_system import Mod


@dataclass
class Findable:
    location: str


@dataclass
class Craftable:
    book: str
    skill: str


@dataclass
class FollowerMod(Mod, Findable):
    ...


@dataclass
class ArmorMod(Mod, Findable, Craftable):
    ...

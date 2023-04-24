from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass
class Attribute:
    name: str


@dataclass
class TextAttribute(Attribute):
    maxlength: int = 256


@dataclass
class TextAreaAttribute(TextAttribute):
    cols: int = 20
    rows: int = 2


@dataclass
class SelectAttribute(Attribute):
    multiple: bool = False


class Mod:
    def __init__(self, name: str, link: str, category: ...):
        self.name = name
        self.link = link
        self.category = category

        self.attrs: list[Attribute] = []


@dataclass
class Folder:
    name: str
    contents: list[Mod | Folder]

    def __init__(self):
        self.minimized = False

    def serialize(self):
        serialized_folder = {}
        for name, value in self.__dict__.items():
            if name == "contents":
                serialized_contents = []
                for element in value:
                    if isinstance(element, Folder):
                        serialized = element.serialize()
                    else:
                        serialized = element.__dict__
                        serialized.update({"__class__": element.__class__.__name__})
                    serialized_contents.append(serialized)
                value = serialized_contents
            serialized_folder[name] = value
        return serialized_folder

    @classmethod
    def from_serialized(cls, serialized: dict[str, Any]):
        deserialized_folder = {}
        for name, value in serialized.items():
            if name == "contents":
                deserialized_contents = []
                for element in value:
                    if "contents" in element:
                        deserialized = cls.from_serialized(element)
                    else:
                        klass = globals()[element.pop("__class__")]
                        deserialized = klass(**element)
                        #exec("deserialized = element['__class__']()")
                    deserialized_contents.append(deserialized)
                value = deserialized_contents
            deserialized_folder[name] = value
        return cls(**deserialized_folder)


@dataclass
class Modpack(Folder):
    description: str

    def to_json(self) -> str:
        return json.dumps(self.serialize())

    @classmethod
    def from_json(cls, data: str):
        return cls.from_serialized(json.loads(data))

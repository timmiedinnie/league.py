from dataclasses import dataclass

@dataclass
class Character():
    cid: int
    name: str
    title: str
    desc: str
    partype: str
    tags: list
    info: dict
    stats: dict
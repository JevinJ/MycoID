from enum import Enum, auto


class EdibilityType(Enum):
    choice = auto()
    edible = auto()
    inedible = auto()
    unpalatable = auto()
    caution = auto()
    psychoactive = auto()
    poisonous = auto()
    allergenic = auto()
    deadly = auto()
    unknown = auto()


class CapShape(Enum):
    campanulate = auto()
    conical = auto()
    convex = auto()
    cylindrical = auto()
    depressed = auto()
    flat = auto()
    infundibuliform = auto()
    kidney = auto()
    offset = auto()
    ovate = auto()
    ovoid = auto()
    umbilicate = auto()
    umbonate = auto()

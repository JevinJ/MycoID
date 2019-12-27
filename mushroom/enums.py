from enum import Enum, Flag, auto


class EcologyType(Flag):
    mycorrhizal = auto()
    saprobic = auto()
    parasitic = auto()


class GrowthHabit(Flag):
    singular = auto()
    gregarious = auto()
    troop = auto()
    caespitose = auto()


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

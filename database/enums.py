from enum import Enum, auto


class EcologyType(Enum):
    mycorrhizal = auto()
    saprobic = auto()
    parasitic = auto()


class ClusteringHabit(Enum):
    singular = auto()
    gregarious = auto()
    troop = auto()
    caespitose = auto()


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


class GillAttachmentType(Enum):
    adnate = auto()
    adnexed = auto()
    decurrent = auto()
    emarginate = auto()
    free = auto()
    seceding = auto()
    sinuate = auto()
    subdecurrent = auto()


class GillSpacingType(Enum):
    distant = auto()
    subdistant = auto()
    close = auto()
    crowded = auto()


class GillForkingType(Enum):
    forking = auto()
    anatomosing = auto()


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

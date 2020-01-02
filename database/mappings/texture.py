from database.mappings import Tag


class Texture(Tag):
    __mapper_args___ = {'polymorphic_identity': 'texture'}

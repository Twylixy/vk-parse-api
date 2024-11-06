from neomodel import (
    StructuredNode,
    StringProperty,
    RelationshipTo,
    RelationshipFrom,
    IntegerProperty,
)


class User(StructuredNode):
    user_id = IntegerProperty(unique_index=True)
    name = StringProperty()
    sex = StringProperty()
    home_town = StringProperty()

    follows = RelationshipTo("User", "Follow")
    subscribes = RelationshipTo("Group", "Subscribe")


class Group(StructuredNode):
    group_id = IntegerProperty(unique_index=True)
    name = StringProperty()

    subscribers = RelationshipFrom("User", "Subscribe")

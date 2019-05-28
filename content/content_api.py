from drawer.text_drawer import TextDrawer
from drawer.animation_drawer import AnimationDrawer
from drawer.image_drawer import ImageDrawer

from recv_protocols.text_protocol import TextProtocol

from content.content_type import ContentType


class ContentAPI:
    _arg_map = {"text": (TextDrawer, TextProtocol),  # TODO add protocols
                "image": (ImageDrawer, None),
                "animation": (AnimationDrawer, None)}

    @classmethod
    def get_content_type(cls, id):
        args = cls._arg_map[id]
        return ContentType(*args)

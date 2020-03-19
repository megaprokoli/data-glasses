from drawer.text_drawer import TextDrawer
from drawer.animation_drawer import AnimationDrawer
from drawer.image_drawer import ImageDrawer

from recv_protocols.text_protocol import TextProtocol
from recv_protocols.img_protocol import ImageProtocol

from content.content_type import ContentType


class ContentAPI:
    _arg_map = {"text": (TextDrawer, TextProtocol),  # TODO add protocols
                "image": (ImageDrawer, ImageProtocol),
                "animation": (AnimationDrawer, None)}

    @classmethod
    def get_content_type(cls, id):
        args = cls._arg_map[id]
        return ContentType(*args)

    @classmethod
    def available_content_types(cls):
        return list(cls._arg_map.keys())

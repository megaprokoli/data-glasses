from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from drawer.drawer import Drawer


class TextDrawer(Drawer):
    def __init__(self, content):
        super().__init__(content)

    def draw(self, disp):
        print("drawing text ({})".format(self._content))

        disp.clear()
        disp.display()

        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = -2
        top = padding
        bottom = height - padding
        # Move left to right keeping track of the current x position for drawing shapes.
        x = 0

        # Load default font.
        font = ImageFont.load_default()

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Write two lines of text.
        draw.text((x, top), self._content, font=font, fill=255)

        # Display image.
        disp.image(image)
        disp.display()

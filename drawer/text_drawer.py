from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from drawer.drawer import Drawer


class TextDrawer(Drawer):
    def __init__(self, content):
        super().__init__(content)

        self._row_len = 21
        self._max_rows = 4
        self._y_axis_threshold = 20
        self._line_padding = 1
        self._prepared = None

    def _prepare(self):
        content = self._content
        result = []
        cont_pointer = self._row_len
        last_pointer = 0

        for i in range(0, self._max_rows):
            result.append(content[last_pointer:cont_pointer])

            last_pointer = cont_pointer + 1     # TODO fail maybe here
            cont_pointer += self._row_len

        self._prepared = result

    def _get_line(self, line):  # TODO dynamic
        # if line > self._max_rows:
        #     line = self._max_rows

        m = {1: 0,
             2: 8,
             3: 15,
             4: 22}
        x = 0
        y = m[line]# ((self._y_axis_threshold - self._max_rows * self._line_padding) / self._max_rows) * line

        return x, int(y)

    def draw(self, disp):
        print("drawing text ({})".format(self._content))

        if self._prepared is None:  # if somehow prepared before
            self._prepare()

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

        for i, text in enumerate(self._prepared):
            line = self._get_line(i)
            draw.text(line, text, font=font, fill=255)

        # Display image.
        disp.image(image)
        disp.display()

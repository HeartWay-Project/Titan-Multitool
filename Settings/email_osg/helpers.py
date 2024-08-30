"""
The 'Color' class is made to create a gradient from one color to another predefined one, so here:
- start = #FE0000 ~ Red
- end = #FFFFFF ~ White
"""

class Color:
    invalid: int
    valid: int
    primary: int

    @classmethod
    def from_hex(cls, hex: str):

        # Check if the input is a valid hex color code
        if not (hex.startswith("#") and len(hex) == 7):
            raise ValueError("Invalid hex color code")

        # Extract R, G, B components
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:7], 16)

        # Ensure the values are in the range 0 to 255
        return cls(
            max(0, min(r, 255)),
            max(0, min(g, 255)),
            max(0, min(b, 255))
        )

    def __init__(self, r: int, g: int, b: int) -> None:
        self.invalid = r
        self.valid = g
        self.primary = b

    # lerp ~ Linear interpolation
    @staticmethod
    def lerp(start, end, alpha: float):

        r = float(start.invalid)
        g = float(start.valid)
        b = float(start.primary)

        r_d = float(end.invalid) - r
        g_d = float(end.valid) - g
        b_d = float(end.primary) - b

        r += (r_d * alpha)
        g += (g_d * alpha)
        b += (b_d * alpha)

        return Color(int(r), int(g), int(b))

def print_banner(banner: str, start: Color, end: Color) -> None:
    banner_split = banner.split('\n')
    lines = []

    for index, banner_line in enumerate(banner_split):

        alpha = float(index) / float(len(banner_split) - 1)

        color = Color.lerp(start=start, end=end, alpha=alpha)
        # print(index, alpha, color.invalid, color.valid, color.primary)

        color = f"\033[38;2;{color.invalid};{color.valid};{color.primary}m"
        line = color + banner_line + "\033[0m" # reset

        lines.append(line)

    banner = '\n'.join(lines)

    print(f"{banner}\n\r")


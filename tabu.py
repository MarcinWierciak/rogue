"""PRESET_COLORS = {
"gold":'#ffd700',
"springgreen": '#00ff7f',
"floralwhite": 'fffaf0',
"lightgrey": '#d3d3d3'}


def parse_color(color):
    if color.lower() in PRESET_COLORS:
        color = PRESET_COLORS[color.lower()]
    color_value = color[1:] if len(color) == 7 else "".join([i*2 for i in color[1:]])
    try:
        result = {
            'r': int(color_value[:2], 16),
            'g': int(color_value[2:4], 16),
            'b': int(color_value[4:], 16)}
        return result
    except ValueError:
        return {}


if __name__ == "__main__":
        print(parse_color("lightgrey"))
        print(parse_color("#445520"))
        print(parse_color("lightgrey"))


"""
PRESET_COLORS = {
    'gold': '#ffd700',
    'springgreen': '#00ff7f',
    'floralwhite': '#fffaf0',
    'lightgray': '#d3d3d3'
}

def parse_color(color):
    if color.lower() in PRESET_COLORS:
        color = PRESET_COLORS[color.lower()]

    color_value = color[1:] if len(color) == 7 else "".join([i * 2 for i in color[1:]])
    try:
        result = {
            'r': int(color_value[:2], 16),
            'g': int(color_value[2:4], 16),
            'b': int(color_value[4:], 16)
        }

        return result
    except ValueError:
        return {}

if __name__ == "__main__":
	print(parse_color('lightgray'))
	print(parse_color('#445520'))
	print(parse_color('lightgray'))

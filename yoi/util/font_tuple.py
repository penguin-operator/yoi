def font_tuple(font: str) -> tuple[str, int, str | None]:
    if not font:
        return ("TkDefaultFont", 10, None)
    data = font.split(' ')
    last = -1 if data[-1].isnumeric() else -2
    size = int(data[last])
    name = ' '.join(data[:last]).replace('{', '').replace('}', '')
    return (name, size, None if data[-1].isnumeric() else data[-1])

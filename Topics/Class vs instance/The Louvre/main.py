class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, creation):
        self.title = title
        self.painter = painter
        self.creation = creation


p = Painting(input(), input(), input())
print(f'"{p.title}" by {p.painter} ({p.creation}) hangs in the {p.museum}.')

class RoundHole:
    def __init__(self, r):
        self.radius = r

    def fits(self, peg):
        return self.radius >= peg.get_radius()


class RoundPeg:
    def __init__(self, r):
        self.radius = r

    def get_radius(self):
        return self.radius


class SquarePeg:
    def __init__(self, width):
        self.width = width


class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg):
        self.peg = square_peg

    def get_radius(self):
        return self.peg.width * 0.707


if __name__ == "__main__":
    hole = RoundHole(5)

    round_peg = RoundPeg(5)
    assert hole.fits(round_peg) == True

    small_square_peg_adapter = SquarePegAdapter(SquarePeg(5))
    large_square_peg_adapter = SquarePegAdapter(SquarePeg(10))
    assert hole.fits(small_square_peg_adapter) == True
    assert hole.fits(large_square_peg_adapter) == False

class Band:
    """Band class to manage a list of musicians."""

    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string representing each musician playing their instruments or needing one."""
        result = []
        for musician in self.musicians:
            if musician.instruments:
                for instrument in musician.instruments:
                    result.append(f"{musician.name} is playing: {instrument}")
            else:
                result.append(f"{musician.name} needs an instrument!")
        return "\n".join(result)
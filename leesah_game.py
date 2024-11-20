"""Spill Leesah-game

1. Hent ned sertifikater, og sikre deg at de ligger i filen leesah-certs.yaml
2. Sett 'LAGNAVN' til ditt valgte lagnavn
3. Sett 'HEXKODE' til din valgte farge
"""
import leesah

LAGNAVN = "grønnskollingene"
HEXKODE = "0x00cccc"


class Rapid(leesah.QuizRapid):
    """Klassen som svarer på spørsmålene."""

    def kjør(self):
        """Start quizen!

        Vi anbefaler at du bruker funksjoner til å svare på spørsmålene.
        """
        while True:
            melding = self.hent_spørsmål()
            if melding.kategori == "team-registration":
                self.behandle_lagregistrering(melding.spørsmål)
            if melding.kategori == "ping-pong":
                self.behandle_pingpong()
            if melding.kategori == "aritmetikk":
                self.behandle_aritmetikk(melding.spørsmål)

    def behandle_lagregistrering(self, spørsmål):
        self.publiser_svar(HEXKODE)

    def behandle_pingpong(self):
        self.publiser_svar("pong")

    def behandle_aritmetikk(self, regnestykke):
        self.publiser_svar(str(eval(regnestykke)))


def read_config():
    # reads the client configuration from client.properties
    # and returns it as a key-value map
    config = {}
    with open("client.properties") as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                config[parameter] = value.strip()
    return config


if __name__ == "__main__":
    config = read_config()
    rapid = Rapid(lagnavn=LAGNAVN, topic="leesha_game", ignorerte_kategorier=[
        # "team-registration",
    ], config=config)

    try:
        rapid.kjør()
    except (KeyboardInterrupt, SystemExit):
        rapid.avslutt()

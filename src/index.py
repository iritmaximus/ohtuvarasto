from varasto import Varasto


# näitä funktioita ei ole mielekästä paloitella enää pienemmäksi,
# näin tekeminen vain monimutkaistaisi aivan turhaan tiedostoa.
# koko index.py tarkoitus tuntuu olevan vain tulostella kovakoodatuilla
# tiedoilla sovellusta, eikä siksi mielestäni pitäisi joutua refaktoroimaan
# ainakaan max-statements rajan takia

# jo nyt tulosteiden järjestys on hieman eri, ilman sitä refaktorointi olisi
# hyvin turhaa ja aivan liian monimutkaista suhteessa siihen, mitä koodi tekee
def main():
    mehu_varasto()
    olut_varasto()
    huono_varasto()


def huono_varasto():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


# pylint: disable-next=too-many-statements
def mehu_varasto():
    mehua = Varasto(100.0)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")

    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

# pylint: disable-next=too-many-statements
def olut_varasto():
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Olutvarasto: {olutta}")

    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

if __name__ == "__main__":
    main()

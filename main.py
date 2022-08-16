import random


def choice(*args):
    for n in sorted(args, key=lambda x: random.random()):
        return n


def kok_colors():
    return choice("Groen", "Geel", "Blauw", "Rood", "Oranje", "****")


def kok_numbers():
    return choice(1, 2, 3, 4, 5, "*")


def kok_special():
    return choice("3 op een rij",
                  "Bommetje",
                  "Hartje",
                  "Hartje",
                  "Alles van 1 kleur",
                  "2 sterren")


if __name__ == '__main__':
    for n in range(0, 30):
        print("Worp %s" % (n + 1))
        print("%s | %s | %s" % (kok_colors(), kok_colors(), kok_colors()))
        print("%s | %s | %s" % (kok_numbers(), kok_numbers(), kok_numbers()))
        print("%s" % kok_special())

        input("Next...")
        print("")

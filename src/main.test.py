from cergen import *

def test_fundamental_functionalities():
    boyut = ()
    aralik = (31, 91)
    dagilim = 'uniform'
    print(rastgele_dogal(boyut, aralik, dagilim))

    print()

    boyut = (2, 3)
    aralik = (1, 8)
    dagilim = 'uniform'
    print(rastgele_dogal(boyut, aralik, dagilim))

    print()

    boyut = (4, 3, 4)
    aralik = (1, 8)
    dagilim = 'uniform'
    print(rastgele_dogal(boyut, aralik, dagilim))

    boyut = ()
    aralik = (31.0, 91.0)
    dagilim = 'uniform'
    print(rastgele_gercek(boyut, aralik, dagilim))

    print()

    boyut = (2, 3)
    aralik = (1.0, 8.0)
    dagilim = 'uniform'
    print(rastgele_gercek(boyut, aralik, dagilim))

    print()

    boyut = (4, 3, 4)
    aralik = (1.0, 8.0)
    dagilim = 'uniform'
    print(rastgele_gercek(boyut, aralik, dagilim))


def test():
    test_fundamental_functionalities()


if __name__ == "__main__":
    test()

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 11)
    
    def test_uudella_varastolla_vaara_tilavuus_ja_saldo(self):
        self.varasto = Varasto(-1,-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_saldo_pienempi_ja_isompi_kuin_tilavuus(self):
        self.varasto1 = Varasto(1,3)
        self.varasto2 = Varasto(3,1)
        self.assertAlmostEqual(self.varasto1.tilavuus, 1)
        self.assertAlmostEqual(self.varasto2.tilavuus, 3)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)
        saatu_maara = self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(saatu_maara, 6)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_string(self):
        joo = self.varasto.__str__()
        self.assertEqual(joo, "saldo = 0, vielä tilaa 10")

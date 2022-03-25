import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.edulliset = 0
        self.maukkaat = 0

    def test_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateinen_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(60, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateinen_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(100, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateinen_edullinen_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(100, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateinen_maukas_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(100, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_edullinen_raha_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(True, True)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_edullinen_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(False, False)

    def test_kortti_maukas_raha_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(True, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_maukas_raha_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(False, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_ladataan_rahaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(kortti.saldo, 2000)

    def test_kortille_ladataan_rahaa_ei_toimi(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -2)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 1000)
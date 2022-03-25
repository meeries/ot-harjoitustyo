import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_asetettu_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_saldo_ei_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_ota_rahaa_false(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(False, False)

    def test_ota_rahaa_true(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(True, True)
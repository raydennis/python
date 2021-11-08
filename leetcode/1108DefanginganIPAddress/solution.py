import unittest


def defang_address(address):
    address = address.replace(".", "[.]")
    return(address)


class TestDefangIPAddress(unittest.TestCase):

    def test_defang_ip_address1(self):
        self.assertEqual(defang_address(
            "1.1.1.1"), "1[.]1[.]1[.]1")

    def test_defang_ip_address2(self):
        self.assertEqual(defang_address(
            "255.100.50.0"), "255[.]100[.]50[.]0")

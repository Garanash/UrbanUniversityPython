import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Usain', 10)
        self.andrey = Runner('Andrey', 9)
        self.nick = Runner('Nick', 3)

    def test_Usain_Nick(self):
        result = Tournament(90, self.usain, self.nick).start()
        TournamentTest.all_results[1] = result
        self.assertTrue(result[2] == self.nick)

    def test_Andrey_Nick(self):
        result = Tournament(90, self.andrey, self.nick).start()
        TournamentTest.all_results[2] = result
        self.assertTrue(result[2] == self.nick)

    def test_all(self):
        result = Tournament(90, self.usain, self.andrey, self.nick).start()
        TournamentTest.all_results[3] = result
        self.assertTrue(result[3] == self.nick)

    def test_short_dist(self):
        result = Tournament(6, self.usain, self.andrey, self.nick).start()
        TournamentTest.all_results[4] = result
        self.assertTrue(result[3] == self.nick)

    def test_short_dist_reversed_order(self):
        result = Tournament(6, self.nick, self.andrey, self.usain).start()
        TournamentTest.all_results[5] = result
        self.assertTrue(result[3] == self.nick)

    @classmethod
    def tearDownClass(cls):
        for v in dict(sorted(cls.all_results.items())).values():
            print(v)


if __name__ == "__main__":
    unittest.main()

import unittest


class Runner:
    def __init__(self, name='Vasya'):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walking_runner = Runner()
        for _ in range(10):
            walking_runner.walk()
        self.assertEqual(walking_runner.distance, 50)

    def test_run(self):
        running_runner = Runner()
        for _ in range(10):
            running_runner.run()
        self.assertEqual(running_runner.distance, 100)

    def test_challenge(self):
        slow_runner = Runner()
        fast_runner = Runner()
        for _ in range(10):
            slow_runner.walk()
            fast_runner.run()
        self.assertNotEqual(slow_runner.distance, fast_runner.distance)


if __name__ == "__main__":
    unittest.main()

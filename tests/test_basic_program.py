import unittest

from basic_program import add, divide, multiply, run, subtract


class TestBasicProgram(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 2), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_run_dispatches_supported_operations(self):
        self.assertEqual(run("add", 1, 2), 3)
        self.assertEqual(run("subtract", 5, 1), 4)
        self.assertEqual(run("multiply", 3, 4), 12)
        self.assertEqual(run("divide", 9, 3), 3)

    def test_run_rejects_unsupported_operation(self):
        with self.assertRaises(ValueError):
            run("mod", 9, 2)


if __name__ == "__main__":
    unittest.main()

import unittest
import ipynb.fs.full.exercises as ex

class TestAssignmentThree(unittest.TestCase):
    def test_01_square_negatives_from_args(self):
        self.assertEqual(ex.square_negatives_from_args(-3, -2, -1, 0, 1, 2, 3), [9, 4, 1])
        self.assertEqual(ex.square_negatives_from_args(-3, -2, -1, 0, 1, 2, 3, '4', '5'), [9, 4, 1])
        self.assertEqual(ex.square_negatives_from_args(-3, -2, -1, False, True, 2, 3, '4', '5'), [9, 4, 1])
        self.assertEqual(ex.square_negatives_from_args(-2, -1, 0), [4, 1])
    def test_02_filter_positives_from_args(self):
        self.assertEqual(ex.filter_positives_from_args(-3, -2, -1, 0, 1, 2, 3), [0, 1, 2, 3])
        self.assertEqual(ex.filter_positives_from_args(-3, -2, -1, 0, 1, 2, 3, '4', '5'), [0, 1, 2, 3])
        self.assertEqual(ex.filter_positives_from_args(-3, -2, -1, False, True, 2, 3, '4', '5'), [False, True, 2, 3])
    def test_03_uppercase_keys_from_kwargs(self):
        self.assertEqual(ex.uppercase_keys_from_kwargs(twn='Taiwan'), ['TWN'])
        self.assertEqual(ex.uppercase_keys_from_kwargs(twn='Taiwan', jpn='Japan'), ['TWN', 'JPN'])
        self.assertEqual(ex.uppercase_keys_from_kwargs(twn='Taiwan', jpn='Japan', ltu="Lithuania"), ['TWN', 'JPN', 'LTU'])
        self.assertEqual(ex.uppercase_keys_from_kwargs(twn='Taiwan', jpn='Japan', ltu="Lithuania", svn='Slovenia'), ['TWN', 'JPN', 'LTU', 'SVN'])
        self.assertEqual(ex.uppercase_keys_from_kwargs(usa='United States'), ['USA'])
    def test_04_count_number_of_each_vowel(self):
        self.assertEqual(ex.count_number_of_each_vowel("Python"), {'o': 1})
        self.assertEqual(ex.count_number_of_each_vowel("Anaconda"), {'a': 3, 'o': 1})
        self.assertEqual(ex.count_number_of_each_vowel("Programming and Data Analysis"), {'o': 1, 'a': 6, 'i': 2})
        self.assertEqual(ex.count_number_of_each_vowel("National Taiwan University"), {'a': 4, 'i': 4, 'o': 1, 'u': 1, 'e': 1})
    def test_05_palindrome(self):
        eye = ex.Palindrome('eye')
        dye = ex.Palindrome('dye')
        anna = ex.Palindrome('anna')
        emma = ex.Palindrome('emma')
        self.assertEqual(eye.original_text, 'eye')
        self.assertEqual(eye.reversed_text, 'eye')
        self.assertTrue(eye.is_palindrome())
        self.assertEqual(dye.original_text, 'dye')
        self.assertEqual(dye.reversed_text, 'eyd')
        self.assertFalse(dye.is_palindrome())
        self.assertTrue(anna.is_palindrome())
        self.assertFalse(emma.is_palindrome())
    def test_06_common_divisors(self):
        cd = ex.CommonDivisors(3, 6)
        self.assertEqual(cd.x_divisors, {1, 3})
        self.assertEqual(cd.y_divisors, {1, 2, 3, 6})
        self.assertEqual(cd.get_common_divisors(), {1, 3})
        cd = ex.CommonDivisors(4, 8)
        self.assertEqual(cd.x_divisors, {1, 2, 4})
        self.assertEqual(cd.y_divisors, {1, 2, 4, 8})
        self.assertEqual(cd.get_common_divisors(), {1, 2, 4})
        cd = ex.CommonDivisors(4, 10)
        self.assertEqual(cd.x_divisors, {1, 2, 4})
        self.assertEqual(cd.y_divisors, {1, 2, 5, 10})
        self.assertEqual(cd.get_common_divisors(), {1, 2})
    def test_07_prime_judgement(self):
        one = ex.PrimeJudgement(1)
        two = ex.PrimeJudgement(2)
        three = ex.PrimeJudgement(3)
        four = ex.PrimeJudgement(4)
        five = ex.PrimeJudgement(5)
        self.assertEqual(one.get_divisors(), {1})
        self.assertFalse(one.is_prime())
        self.assertEqual(two.get_divisors(), {1, 2})
        self.assertTrue(two.is_prime())
        self.assertEqual(four.get_divisors(), {1, 2, 4})
        self.assertFalse(one.is_prime())
        self.assertTrue(three.is_prime())
        self.assertTrue(five.is_prime())
    def test_08_load_teams_json(self):
        teams = ex.load_teams_json('teams.json')
        self.assertIsInstance(teams, dict)
        self.assertEqual(len(teams), 2)
        self.assertIn('_internal', teams.keys())
        self.assertIn('league', teams.keys())
    def test_09_find_team_full_names(self):
        team_full_names = ex.find_team_full_names('teams.json')
        self.assertIsInstance(team_full_names, list)
        self.assertEqual(len(team_full_names), 30)
        self.assertIn('Boston Celtics', team_full_names)
        self.assertIn('Brooklyn Nets', team_full_names)
        self.assertIn('Chicago Bulls', team_full_names)
        self.assertIn('Utah Jazz', team_full_names)
    def test_10_find_teams_with_special_tricodes(self):
        teams_with_special_tricodes = ex.find_teams_with_special_tricodes('teams.json')
        self.assertIsInstance(teams_with_special_tricodes, dict)
        self.assertEqual(teams_with_special_tricodes['BKN'], 'Brooklyn Nets')
        self.assertEqual(teams_with_special_tricodes['SAS'], 'San Antonio Spurs')

suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentThree)
runner = unittest.TextTestRunner(verbosity=2)
if __name__ == '__main__':
    test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))
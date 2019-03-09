import os
import unittest

from app import app

from app.models import FormulaOneDNFParser


class FormulaOneDNFParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = FormulaOneDNFParser()

    def test_type_1_wikitable(self):
        """Test data based on 2011 season with first type of wikitable."""
        data_file_path = os.path.join(app.root_path, 'tests/test_data/wikitable_type1')
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as file:
                for line in file:
                    self.parser.feed(line)
            season_data = self.parser.get_dnf_stats_json()
            self.assertEqual(season_data['ret'], 74)
            self.assertEqual(season_data['nc'], 2)
            self.assertEqual(season_data['dnq'], 2)
            self.assertEqual(season_data['dnpq'], 0)
            self.assertEqual(season_data['dsq'], 2)
            self.assertEqual(season_data['dns'], 2)
            self.assertEqual(season_data['dnp'], 0)
            self.assertEqual(season_data['ex'], 0)
            self.assertEqual(season_data['wd'], 1)
            self.assertEqual(season_data['total_dnf'], 83)
            self.assertEqual(season_data['total_classified_finish'], 374)
            self.assertEqual(season_data['total_race_entries'], 457)

    def test_type_2_wikitable(self):
        """Test data based on 2012 season with second type of wikitable."""
        data_file_path = os.path.join(app.root_path, 'tests/test_data/wikitable_type2')
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as file:
                for line in file:
                    self.parser.feed(line)
            season_data = self.parser.get_dnf_stats_json()
            self.assertEqual(season_data['ret'], 75)
            self.assertEqual(season_data['nc'], 0)
            self.assertEqual(season_data['dnq'], 2)
            self.assertEqual(season_data['dnpq'], 0)
            self.assertEqual(season_data['dsq'], 0)
            self.assertEqual(season_data['dns'], 2)
            self.assertEqual(season_data['dnp'], 0)
            self.assertEqual(season_data['ex'], 0)
            self.assertEqual(season_data['wd'], 0)
            self.assertEqual(season_data['total_dnf'], 79)
            self.assertEqual(season_data['total_classified_finish'], 401)
            self.assertEqual(season_data['total_race_entries'], 480)

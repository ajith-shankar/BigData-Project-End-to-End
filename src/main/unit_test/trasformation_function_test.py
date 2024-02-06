import unittest
import os, sys

from src.main.python.bin.presc_run_data_transform import city_report

sys.path.insert(0, "/home/hadoop/Projects/BigData-Project-End-to-End/src/main/python/bin")

class TransformTest(unittest.TestCase):
    def test_city_report_zip_tnx_cnt(self):
        spark = SparkSession.builder() \
                .master('local') \
                .appName('Unit test') \
                .getOrCreate()



from houseclassifier.utils.common import read_yaml
from pyspark.sql import SparkSession

class spark_sessiontools():
    def start_sparksession():
        sparkconfig = read_yaml('config/spark_config.yaml')
        return sparkconfig
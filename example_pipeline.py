import json
import pandas as pd

from numeric_conversion.convert_numeric import convert_numeric
from validation_rules.validate_age import validate_age
from validation_rules.validate_salary import validate_salary
from validation_rules.validate_department import validate_department
from logging.file_logger import write_log


with open("config_examples/config.json") as f:
    config = json.load(f)

df = pd.read_csv("datasets/sample_dirty_data.csv")

write_log("INFO", "Pipeline started")

df = convert_numeric(df)
df = validate_age(df, config)
df = validate_salary(df, config)
df = validate_department(df, config)

write_log("INFO", "Pipeline completed")

df.to_csv("datasets/cleaned_data.csv", index=False)

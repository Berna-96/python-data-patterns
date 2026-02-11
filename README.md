# Python Data Patterns

Reusable data processing and cleaning patterns built with Python and pandas.

This repository contains small, focused utilities designed while learning practical
data cleaning, validation, and preprocessing techniques used in real-world workflows.

---

## 📌 Purpose

The goal of this repository is to collect reusable and easy-to-understand patterns for:

- Numeric conversion
- Data validation rules
- Handling missing / invalid values
- Logging system examples
- Config-driven data rules

Instead of building isolated scripts, this repo focuses on modular and reusable logic.

---

## 🧱 Project Structure

numeric_conversion/  
Utilities for safe numeric conversion.

validation_rules/  
Independent validation functions (age, salary, categories).

logging/  
Simple file-based logging system with timestamps and log levels.

config_examples/  
External configuration examples (JSON-driven rules).

datasets/  
Sample datasets for testing and experimentation.

example_pipeline.py  
Demonstrates how all modules work together.

---

## ⚙️ Example Pipeline Logic

The example pipeline follows a typical data processing workflow:

1. Load configuration
2. Load dataset
3. Convert dirty numeric values
4. Apply validation rules
5. Log anomalies
6. Save cleaned dataset

Example:

```python
df = convert_numeric(df)
df = validate_age(df, config)
df = validate_salary(df, config)
df = validate_department(df, config)

---

## 🧠 Key Concepts Demonstrated

- Separation of responsibilities  
- Config-driven validation rules  
- Safe numeric conversion  
- Missing value handling  
- Basic production-style logging  

---

## 🚀 Why This Repository Exists

This repository is part of a hands-on learning process focused on understanding:

- How real data breaks  
- How validation systems work  
- How to design reusable code  
- How to structure small Python utilities  

---

## 📚 Technologies Used

- Python  
- pandas  
- JSON configuration patterns  

---

## ✅ Status

Active learning repository.  
Continuously expanded with new patterns and utilities.

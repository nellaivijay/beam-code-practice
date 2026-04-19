# Lab 0: Sample Data Setup

## Overview

This lab guides you through generating and loading sample data that will be used throughout the Apache Beam learning labs. Having realistic sample data is essential for understanding pipeline concepts and practicing data transformations.

## Learning Objectives

- Generate realistic sample data for pipeline processing
- Understand data formats suitable for Apache Beam pipelines
- Set up data directory structure
- Validate data integrity

## Prerequisites

- Python 3.8+
- Basic understanding of CSV and JSON formats

## Setup Instructions

### 1. Generate Sample Data

Run the sample data generation script:

```bash
python scripts/generate_sample_data.py
```

This script creates several datasets in the `data/` directory:

- `sample_sales.csv` - Sales transaction data
- `customer_data.csv` - Customer information
- `product_data.csv` - Product catalog
- `streaming_events.csv` - Simulated streaming events
- `sensor_readings.csv` - IoT sensor data

### 2. Data Structure

The generated data follows this structure:

```
data/
├── sample_sales.csv          # Sales transactions
├── customer_data.csv          # Customer information
├── product_data.csv           # Product catalog
├── streaming_events.csv       # Streaming event data
└── sensor_readings.csv        # Sensor readings
```

### 3. Data Validation

Validate that the data has been generated correctly:

```python
import pandas as pd
import os

# Check if files exist
data_dir = 'data/'
files = os.listdir(data_dir)
print(f"Generated files: {files}")

# Load and inspect sales data
sales_df = pd.read_csv('data/sample_sales.csv')
print(f"Sales records: {len(sales_df)}")
print(sales_df.head())
```

## Data Formats

### CSV Format

Most sample data is provided in CSV format for easy loading:

```python
import pandas as pd

df = pd.read_csv('data/sample_sales.csv')
```

### JSON Format

Some data is available in JSON format for flexibility:

```python
import json

with open('data/config.json', 'r') as f:
    config = json.load(f)
```

## Using Sample Data in Pipelines

### Loading Data

```python
import apache_beam as beam
import pandas as pd

# Load CSV data
df = pd.read_csv('data/sample_sales.csv')
data = df.to_dict('records')

# Use in pipeline
with beam.Pipeline() as pipeline:
    (pipeline
     | 'Create data' >> beam.Create(data)
     | 'Process' >> beam.Map(lambda x: x['quantity'] * x['price'])
     | 'Print' >> beam.Map(print))
```

### Streaming Data

For streaming exercises, use the streaming events data:

```python
streaming_df = pd.read_csv('data/streaming_events.csv')
streaming_data = streaming_df.to_dict('records')
```

## Custom Data Generation

You can generate custom data for specific scenarios:

```python
import pandas as pd
import random
from datetime import datetime, timedelta

# Generate custom sales data
custom_data = []
for i in range(100):
    record = {
        'transaction_id': f'txn_{i}',
        'customer_id': f'customer_{random.randint(1, 20)}',
        'product_id': f'product_{random.randint(1, 10)}',
        'quantity': random.randint(1, 5),
        'price': random.uniform(10, 100),
        'timestamp': datetime.now().isoformat()
    }
    custom_data.append(record)

df = pd.DataFrame(custom_data)
df.to_csv('data/custom_sales.csv', index=False)
```

## Troubleshooting

### Data Not Generated

If the data generation script fails:

1. Check that you have write permissions to the `data/` directory
2. Ensure all required Python packages are installed
3. Check for error messages in the script output

### Data Loading Errors

If you encounter errors loading data:

1. Verify file paths are correct
2. Check that files are not corrupted
3. Ensure CSV files have proper headers
4. Validate data types match expectations

## Next Steps

After completing this lab:

1. Verify all sample data files are present
2. Inspect the data structure and content
3. Proceed to [Lab 1: Environment Setup](Lab-1-Environment-Setup)

## Additional Resources

- [Apache Beam I/O Documentation](https://beam.apache.org/documentation/io/io-templates/)
- [Data Formats Guide](https://beam.apache.org/documentation/programming-guide/#reading-input-data)
- [Sample Data Best Practices](https://beam.apache.org/documentation/programming-guide/#creating-a-pcollection)
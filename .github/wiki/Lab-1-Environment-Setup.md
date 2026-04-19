# Lab 1: Environment Setup

## Overview

This lab guides you through setting up your Apache Beam development environment. A properly configured environment is essential for developing and testing data pipelines effectively.

## Learning Objectives

- Install Apache Beam and required dependencies
- Set up Python virtual environment
- Configure pipeline runners (DirectRunner, DataflowRunner)
- Validate installation with test pipeline
- Understand runner options and trade-offs

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Basic command line familiarity

## Installation Steps

### 1. Check Python Version

```bash
python --version
# Should show Python 3.8 or higher
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv beam_env

# Activate virtual environment
# On Linux/Mac:
source beam_env/bin/activate
# On Windows:
beam_env\Scripts\activate
```

### 3. Install Dependencies

Install Apache Beam and required packages:

```bash
pip install -r requirements.txt
```

The requirements file includes:
- `apache-beam[gcp]` - Apache Beam with Google Cloud extras
- `pandas` - Data manipulation
- `pytest` - Testing framework

### 4. Verify Installation

```python
import apache_beam as beam
print(f"Apache Beam version: {beam.__version__}")
```

## Pipeline Runners

### DirectRunner

The DirectRunner executes pipelines locally for development and testing:

```python
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions

options = PipelineOptions()
options.view_as(StandardOptions).runner = 'DirectRunner'

with beam.Pipeline(options=options) as pipeline:
    # Your pipeline logic
    pass
```

**Use Cases:**
- Development and testing
- Small to medium datasets
- Quick iteration
- Local debugging

**Limitations:**
- Limited to single machine
- Not suitable for production
- Limited scalability

### DataflowRunner

For production workloads on Google Cloud:

```python
options = PipelineOptions()
options.view_as(StandardOptions).runner = 'DataflowRunner'
options.view_as(StandardOptions).project = 'your-project-id'
options.view_as(StandardOptions).region = 'us-central1'
```

**Requirements:**
- Google Cloud project
- Service account credentials
- Billing enabled

### SparkRunner

For running on Apache Spark clusters:

```python
options = PipelineOptions()
options.view_as(StandardOptions).runner = 'SparkRunner'
```

### FlinkRunner

For streaming-focused workloads on Apache Flink:

```python
options = PipelineOptions()
options.view_as(StandardOptions).runner = 'FlinkRunner'
```

## Test Pipeline

Create a simple test pipeline to verify your setup:

```python
import apache_beam as beam

def test_pipeline():
    with beam.Pipeline() as pipeline:
        (pipeline
         | 'Create numbers' >> beam.Create([1, 2, 3, 4, 5])
         | 'Double' >> beam.Map(lambda x: x * 2)
         | 'Print' >> beam.Map(print))

test_pipeline()
```

Expected output:
```
2
4
6
8
10
```

## Environment Variables

Set environment variables for pipeline configuration:

```bash
# Set default runner
export BEAM_RUNNER=DirectRunner

# Set pipeline options
export BEAM_PIPELINE=test_pipeline
```

## Common Issues and Solutions

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'apache_beam'`

**Solution:**
```bash
pip install apache-beam[gcp]
```

### Memory Errors

**Problem:** Pipeline runs out of memory

**Solution:**
```bash
export BEAM_DIRECT-runner_memory=4g
```

### Version Conflicts

**Problem:** Dependency version conflicts

**Solution:**
```bash
pip install --upgrade pip
pip install --upgrade apache-beam[gcp]
```

## IDE Setup

### VS Code

Install recommended extensions:
- Python
- Jupyter
- Pylance

Configure Python interpreter:
```json
{
    "python.defaultInterpreterPath": "./beam_env/bin/python"
}
```

### PyCharm

1. Open project
2. Configure Python interpreter
3. Install required packages
4. Set up run configurations

## Jupyter Notebook Setup

For running the lab notebooks:

```bash
pip install jupyter notebook
jupyter notebook
```

Navigate to the `notebooks/` directory and open lab notebooks.

## Next Steps

After completing this lab:

1. Verify Apache Beam is installed correctly
2. Test a simple pipeline
3. Configure your preferred runner
4. Proceed to [Lab 2: Pipeline Fundamentals](Lab-2-Pipeline-Fundamentals)

## Additional Resources

- [Apache Beam Installation Guide](https://beam.apache.org/get-started/quickstart/)
- [Pipeline Options Reference](https://beam.apache.org/documentation/programming-guide/#pipeline-options)
- [Runner Documentation](https://beam.apache.org/documentation/runners/capability-matrix/)
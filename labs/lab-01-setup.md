# Lab 1: Environment Setup

## 🎯 Learning Objectives

- Install Apache Beam and dependencies
- Test pipeline execution locally
- Validate runner configurations
- Explore different SDKs (Python, Java)

## 📋 Prerequisites

- Python 3.8+ installed
- pip (Python package manager)
- Basic understanding of data pipeline concepts

## ⏱️ Estimated Time

30-45 minutes

## 🎓 Conceptual Background

Apache Beam can be used through multiple interfaces:

1. **Python SDK**: Programmatic pipeline development
2. **Java SDK**: Enterprise pipeline development
3. **SQL Support**: Beam SQL for declarative pipelines
4. **Multiple Runners**: DirectRunner, Dataflow, Spark, Flink

Each interface has its strengths and use cases. In this lab, you'll explore the Python SDK.

## 🚀 Step-by-Step Instructions

### Step 1: Install Apache Beam

Install Apache Beam with Google Cloud extras:

```bash
pip install apache-beam[gcp]
```

For additional runner support:

```bash
# For Spark
pip install apache-beam[spark]

# For Flink
pip install apache-beam[flink]
```

### Step 2: Test Python SDK

Test basic Apache Beam functionality:

```python
import apache_beam as beam

# Create a simple pipeline
with beam.Pipeline() as pipeline:
    (pipeline
     | 'Create Data' >> beam.Create([1, 2, 3, 4, 5])
     | 'Multiply by 2' >> beam.Map(lambda x: x * 2)
     | 'Print Results' >> beam.Map(print)
    )
```

### Step 3: Validate Runner Configuration

Test different runner configurations:

```python
# DirectRunner (local execution)
pipeline_options = {
    'runner': 'DirectRunner'
}

# Dataflow (cloud execution - requires GCP setup)
pipeline_options = {
    'runner': 'DataflowRunner',
    'project': 'your-project-id',
    'region': 'us-central1',
    'temp_location': 'gs://your-bucket/temp'
}
```

## ✅ Expected Results

After completing this lab, you should:

1. ✅ Have Apache Beam properly installed and configured
2. ✅ Be able to execute basic pipelines locally
3. ✅ Understand different runner configurations
4. ✅ Be ready to proceed to Lab 2

## 🆘 Troubleshooting

### Issue: Apache Beam import fails

**Solution**: Install Apache Beam:
```bash
pip install apache-beam[gcp]
```

### Issue: Pipeline execution fails

**Solution**: Check runner configuration and dependencies:
```bash
# Verify installation
python -c "import apache_beam; print(beam.__version__)"
```

## 📚 Next Steps

After completing this lab:

1. **Proceed to Lab 2**: Pipeline Fundamentals
2. **Read Apache Beam documentation**: https://beam.apache.org/documentation/
3. **Practice pipelines**: Try different pipeline operations

---

**Your Apache Beam environment is now fully configured and ready for learning!**
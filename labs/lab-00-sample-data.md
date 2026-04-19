# Lab 0: Sample Data Setup

## 🎯 Learning Objectives

- Generate realistic sample data for Apache Beam pipelines
- Load sample data for pipeline processing
- Understand the sample data schema
- Practice basic pipeline operations on sample data

## 📋 Prerequisites

- Python 3.8+ installed
- Apache Beam Python package installed
- Completed environment setup

## ⏱️ Estimated Time

20-30 minutes

## 🎓 Conceptual Background

The sample data provides realistic business data for learning Apache Beam pipeline concepts. It includes:
- **Sales Transactions**: Transaction data for batch processing
- **User Events**: Event data for streaming pipelines
- **Log Data**: Server logs for ETL patterns
- **User Behavior**: User activity data for analytics

This data allows you to practice real-world pipeline scenarios without dealing with sensitive data.

## 🚀 Step-by-Step Instructions

### Step 1: Generate Sample Data

Generate sample data using the provided script:

```bash
python3 scripts/generate_sample_data.py
```

By default, this generates:
- 10,000 sales transactions
- 50,000 user events
- 100,000 log entries
- 5,000 user profiles

You can customize the size:

```bash
# Small dataset
python3 scripts/generate_sample_data.py --size small

# Large dataset
python3 scripts/generate_sample_data.py --size large
```

### Step 2: Verify Data Generation

Check that sample data files were created:

```bash
ls -la data/sample/
```

Expected files:
- sales_transactions.csv
- user_events.json
- server_logs.csv
- user_profiles.parquet

## ✅ Expected Results

After completing this lab, you should:

1. ✅ Have sample data files in `data/sample/` directory
2. ✅ Understand the sample data schema
3. ✅ Be ready to proceed to Lab 1

## 🆘 Troubleshooting

### Issue: Sample data generation fails

**Solution**: Ensure you have pandas and numpy installed:
```bash
pip install pandas numpy
```

## 📚 Next Steps

After completing this lab:

1. **Proceed to Lab 1**: Environment Setup and Validation
2. **Read Apache Beam documentation**: https://beam.apache.org/documentation/
3. **Practice pipelines**: Try different pipeline operations on sample data

---

**Your sample data is now ready for learning Apache Beam!**
# Apache Beam Code Practice

## 🎯 Educational Mission

A comprehensive, vendor-independent Apache Beam learning environment designed for developers, data engineers, and analysts who want to master modern data pipeline engineering through hands-on practice.

**15 progressive labs with 120+ exercises covering Apache Beam fundamentals, pipeline development, streaming processing, and production deployment. Completely free and open source. Built for learners, by learners.**

## 🎓 Why This Repository?

This educational resource fills the gap between theoretical knowledge and practical skills in Apache Beam and modern data pipeline engineering:

- **Learn by Doing**: Progressive hands-on labs build real skills
- **Vendor Independent**: Master concepts that apply across all runners
- **Unified Model**: Learn the Beam model for batch and streaming
- **Production Patterns**: Learn deployment, monitoring, and operations
- **Multi-Language Experience**: Work with Python, Java, and SQL
- **Community Driven**: Built and improved by the data engineering community

## 🎓 Learning Approach

### Progressive Complexity

Our labs are designed to build knowledge progressively:

- **Beginner (Labs 0-2)**: Foundation and basic pipeline concepts
- **Intermediate (Labs 3-6)**: Advanced transforms and I/O
- **Advanced (Labs 7-10)**: Streaming, state, and production deployment

### Hands-On Learning

Each lab includes:
- **Clear Learning Objectives**: Know what you'll achieve
- **Step-by-Step Instructions**: Guided exercises
- **Real-World Scenarios**: Practical pipeline use cases
- **Solution Notebooks**: Reference implementations
- **Conceptual Guides**: Deep-dive explanations

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Apache Beam Code Practice                │
│                  Data Pipeline Learning Environment         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Apache Beam Unified Model                 │  │
│  │         - PCollection abstraction               │  │
│  │         - Transform functions                   │  │
│  │         - Pipeline I/O connectors                │  │
│  │         - Windowing and triggers                 │  │
│  └──────────────────────────────────────────────────────┘  │
│                              ↓                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Pipeline Development                     │  │
│  │         - Batch processing patterns              │  │
│  │         - Streaming processing patterns           │  │
│  │         - State management                       │  │
│  │         - Windowing strategies                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                              ↓                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Execution Runners                        │  │
│  │         - DirectRunner (local)                   │  │
│  │         - Dataflow (cloud)                      │  │
│  │         - Spark (cluster)                        │  │
│  │         - Flink (streaming)                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                              ↓                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Data Sources & Sinks                     │  │
│  │         - File systems (GCS, S3, HDFS)           │  │
│  │         - Pub/Sub, Kafka (streaming)              │  │
│  │         - Databases (BigQuery, Spanner)           │  │
│  │         - Custom I/O connectors                  │  │
│  └──────────────────────────────────────────────────────┘  │
│                              ↓                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Production Operations                   │  │
│  │         - Pipeline deployment                   │  │
│  │         - Monitoring and logging                 │  │
│  │         - Testing and debugging                  │  │
│  │         - Performance optimization               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Core Stack

### Apache Beam
- **Apache Beam**: Unified model for batch and streaming
- **Python SDK**: Pipeline development with Python
- **Java SDK**: Pipeline development with Java
- **SQL Support**: Beam SQL for declarative pipelines

### Execution Runners
- **DirectRunner**: Local execution for development
- **Dataflow**: Managed cloud execution
- **Spark**: Cluster execution
- **Flink**: Streaming execution

### Data Connectors
- **File Systems**: GCS, S3, HDFS, local files
- **Streaming**: Pub/Sub, Kafka
- **Databases**: BigQuery, Spanner, JDBC
- **Custom I/O**: Extensible connector framework

## 🎓 Lab Structure

### Lab Difficulty & Time Estimates

| Level | Labs | Time per Lab | What It Tests |
|-------|------|--------------|---------------|
| Beginner | Labs 0-2 | 30-60 min | Basic setup, pipeline concepts, simple transforms |
| Intermediate | Labs 3-6 | 45-75 min | Advanced transforms, I/O, windowing, state |
| Advanced | Labs 7-10 | 60-120 min | Streaming, production, deployment, monitoring |

### Lab 0: Environment Setup
- Install Apache Beam and dependencies
- Test pipeline execution locally
- Validate runner configurations
- Explore different SDKs

### Lab 1: Introduction to Apache Beam
- Understand Apache Beam fundamentals
- Learn the Beam model and concepts
- Explore PCollection and transforms
- Build your first pipeline

### Lab 2: Pipeline Fundamentals
- Create and execute basic pipelines
- Understand pipeline I/O
- Practice common transforms
- Work with schema and data types

### Lab 3: Core Transforms
- ParDo, Map, Filter, GroupByKey
- Combine, Flatten, CoGroupByKey
- Custom transforms and DoFns
- Pipeline optimization basics

### Lab 4: I/O Connectors
- File system I/O (GCS, S3, local)
- Database I/O (BigQuery, JDBC)
- Streaming I/O (Pub/Sub, Kafka)
- Custom I/O connectors

### Lab 5: Windowing and Triggers
- Fixed and sliding windows
- Session windows
- Trigger strategies
- Late data handling

### Lab 6: State and Timers
- Stateful processing
- Timers and user state
- State persistence
- Checkpointing

### Lab 7: Streaming Pipelines
- Streaming fundamentals
- Watermarks and event time
- Streaming I/O patterns
- Streaming aggregation

### Lab 8: Pipeline Testing
- Unit testing transforms
- Integration testing pipelines
- Testing streaming pipelines
- Test data and fixtures

### Lab 9: Production Deployment
- Dataflow deployment
- Spark deployment
- Flink deployment
- Pipeline templates

### Lab 10: Monitoring and Operations
- Pipeline monitoring
- Logging and debugging
- Performance optimization
- Error handling

## 💾 Sample Data

The environment includes comprehensive sample datasets for hands-on learning:

### Sample Datasets
- **Sample Sales Data**: Transaction records for pipeline processing
- **Sample Streaming Data**: Event data for streaming pipelines
- **Sample Log Data**: Server logs for ETL patterns
- **Sample User Data**: User behavior data for analytics

### Loading Sample Data
```bash
# Generate and load sample data
python3 scripts/generate_sample_data.py
python3 scripts/load_sample_data.py
```

## 🚀 Quick Start

### 🎓 New to Apache Beam?

Follow our recommended learning path:

1. **Start with Fundamentals**: Read [Apache Beam Fundamentals](https://github.com/nellaivijay/beam-code-practice/wiki/Apache-Beam-Fundamentals) wiki page
2. **Set Up Environment**: Follow [Getting Started Guide](https://github.com/nellaivijay/beam-code-practice/wiki/Getting-Started)
3. **Begin Lab 0**: Load sample data with [Lab 0](https://github.com/nellaivijay/beam-code-practice/blob/main/labs/lab-00-sample-data.md)
4. **Progress Through Labs**: Follow the [Learning Path](https://github.com/nellaivijay/beam-code-practice/wiki/Learning-Path)

### 📋 Setup Options

### Option 1: Python Environment (Recommended)
```bash
cd beam-code-practice
pip install -r requirements.txt
python3 scripts/setup.py
```

### Option 2: Docker Environment
```bash
cd beam-code-practice
docker-compose up -d
```

## 📋 Requirements

- Python 3.8+ (for Python SDK)
- Java 11+ (for Java SDK)
- pip (Python package manager)
- 4GB RAM minimum (8GB recommended)
- 2GB disk space minimum

## 🔧 Configuration

### Python Environment Setup
```bash
# Install Apache Beam
pip install apache-beam[gcp]

# Install additional runners
pip install apache-beam[gcp]  # For Dataflow
pip install apache-beam[spark]  # For Spark
```

### Beam Configuration
```python
import apache_beam as beam

# Set pipeline options
pipeline_options = {
    'runner': 'DirectRunner',
    'project': 'your-project',
    'region': 'us-central1',
    'temp_location': 'gs://your-bucket/temp'
}
```

## 📚 Documentation

### 🎓 Educational Resources

**Wiki Guides** (Comprehensive learning materials):
- [Wiki Home](https://github.com/nellaivijay/beam-code-practice/wiki) - Main wiki page with all guides
- [Getting Started Guide](https://github.com/nellaivijay/beam-code-practice/wiki/Getting-Started) - Complete setup and first steps
- [Apache Beam Fundamentals](https://github.com/nellaivijay/beam-code-practice/wiki/Apache-Beam-Fundamentals) - Core concepts and architecture
- [Lab Guides](https://github.com/nellaivijay/beam-code-practice/wiki/Lab-Guides) - Detailed lab walkthroughs
- [Learning Path](https://github.com/nellaivijay/beam-code-practice/wiki/Learning-Path) - Recommended learning sequence
- [Best Practices](https://github.com/nellaivijay/beam-code-practice/wiki/Best-Practices) - Production-ready patterns
- [Troubleshooting](https://github.com/nellaivijay/beam-code-practice/wiki/Troubleshooting) - Common issues and solutions

### Core Documentation
- [Setup Guide](docs/SETUP_GUIDE.md) - Detailed setup instructions for Python and Java
- [Architecture Overview](docs/ARCHITECTURE.md) - System architecture and component details
- [Pipeline Patterns](docs/PIPELINE_PATTERNS.md) - Common pipeline patterns and use cases
- [Streaming Guide](docs/STREAMING_GUIDE.md) - Streaming processing concepts
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md) - Production deployment strategies
- [Lab Guide](docs/LAB_GUIDE.md) - Complete lab sequence and learning path
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions

### Lab Materials
- [Lab 0: Sample Data Setup](labs/lab-00-sample-data.md) - Generate and load sample data
- [Lab 1: Environment Setup](labs/lab-01-setup.md) - Component verification and first pipeline
- [Lab 2: Pipeline Fundamentals](labs/lab-02-pipeline-fundamentals.md) - Basic pipeline development
- [Lab 3: Core Transforms](labs/lab-03-core-transforms.md) - Transform functions and patterns
- [Lab 4: I/O Connectors](labs/lab-04-io-connectors.md) - Data sources and sinks
- [Lab 5: Windowing and Triggers](labs/lab-05-windowing-triggers.md) - Windowing strategies
- [Lab 6: State and Timers](labs/lab-06-state-timers.md) - Stateful processing
- [Lab 7: Streaming Pipelines](labs/lab-07-streaming-pipelines.md) - Streaming fundamentals
- [Lab 8: Pipeline Testing](labs/lab-08-testing.md) - Testing strategies
- [Lab 9: Production Deployment](labs/lab-09-deployment.md) - Deployment to runners
- [Lab 10: Monitoring and Operations](labs/lab-10-monitoring.md) - Production operations

### 💡 Jupyter Notebooks
Interactive Jupyter notebooks for hands-on learning:

- [Lab Notebooks](notebooks/) - Student notebooks with exercises
- [Solution Helper](notebooks/SOLUTION_HELPER_INSTRUCTIONS.md) - How to use the solution helper
- [Notebook Helper](notebooks/NOTEBOOK_HELPER.md) - Guide for using notebooks effectively

### 🤖 Automation Scripts
- [Setup Script](scripts/setup.py) - Environment validation and setup
- [Generate Sample Data](scripts/generate_sample_data.py) - Generate realistic pipeline data
- [Load Sample Data](scripts/load_sample_data.py) - Load sample data for pipelines

## 🔗 Related Practice Repositories

Continue your learning journey with these related repositories:

### AI/ML Practice
- [🤖 DSPy Code Practice](https://github.com/nellaivijay/dspy-code-practice) - Declarative LLM programming
- [🧠 LLM Fine-Tuning Practice](https://github.com/nellaivijay/llm-fine-tuning-practice) - Model fine-tuning techniques

### Data Engineering Practice
- [🦆 DuckDB Code Practice](https://github.com/nellaivijay/duckdb-code-practice) - Analytics & SQL optimization
- [⚡ Apache Spark Code Practice](https://github.com/nellaivijay/spark-code-practice) - Big data processing
- [🏔️ Apache Iceberg Code Practice](https://github.com/nellaivijay/iceberg-code-practice) - Lakehouse architecture

### Programming Practice
- [⚙️ Scala Data Analysis Practice](https://github.com/nellaivijay/scala-dataanalysis-code-practice) - Functional programming

### Resource Hub
- [📚 Awesome My Notes](https://github.com/nellaivijay/awesome-my-notes) - Comprehensive technical notes and learning resources

## 🆘 Vendor Independence

This environment uses only Apache 2.0 licensed tools:
- Apache Beam (Apache 2.0)
- Python packages (various open source licenses)
- Jupyter (BSD)
- Pandas (BSD)

No proprietary cloud services or consoles required.

## 🤝 Contributing

This is a practice environment for learning. Feel free to extend labs, add examples, or improve the setup process.

> **Disclaimer**: This is an independent educational resource for learning Apache Beam and modern data pipeline engineering. It is not affiliated with, endorsed by, or sponsored by Apache Beam or any vendor.

## 👥 Community and Learning

This repository is an open educational resource built for the data engineering community. We believe in learning together and sharing knowledge.

### 🤝 Learning Together

- **📖 Comprehensive Wiki**: Detailed guides and tutorials for all skill levels
- **💬 GitHub Discussions**: Ask questions and share insights with fellow learners
- **🐛 Issue Tracking**: Report bugs and suggest improvements
- **🔄 Pull Requests**: Contribute labs, fixes, and enhancements
- **⭐ Star the Repo**: Show your support and help others discover this resource

### 🎓 Contributing to Learning

We welcome contributions that improve the educational value:
- **New Labs**: Suggest new lab topics and exercises
- **Better Explanations**: Improve clarity of existing content
- **Additional Examples**: Add more practical examples
- **Translation**: Help translate content for global learners
- **Bug Fixes**: Report and fix issues in labs or documentation

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

### 📚 Additional Learning Resources

- **Official Apache Beam Documentation**: [https://beam.apache.org/documentation/](https://beam.apache.org/documentation/)
- **Apache Beam Blog**: Latest updates and articles
- **Conference Talks**: Learn from industry experts

## 📄 License

Apache License 2.0
#!/usr/bin/env python3
"""
Generate Sample Data for Apache Beam Practice

This script generates realistic sample data for Apache Beam pipeline learning.
"""

import pandas as pd
import numpy as np
import json
import argparse
import os

def generate_sales_data(size='medium'):
    """Generate sales transaction data."""
    sizes = {'small': 1000, 'medium': 10000, 'large': 100000}
    n = sizes.get(size, 10000)
    
    data = {
        'transaction_id': range(1, n + 1),
        'customer_id': np.random.randint(1, 1000, n),
        'product_id': np.random.randint(1, 100, n),
        'amount': np.random.uniform(10, 500, n),
        'transaction_date': pd.date_range('2023-01-01', periods=n, freq='H'),
        'status': np.random.choice(['completed', 'pending', 'failed'], n)
    }
    
    df = pd.DataFrame(data)
    os.makedirs('data/sample', exist_ok=True)
    df.to_csv('data/sample/sales_transactions.csv', index=False)
    print(f"Generated {n} sales transactions")

def generate_user_events(size='medium'):
    """Generate user event data for streaming."""
    sizes = {'small': 5000, 'medium': 50000, 'large': 500000}
    n = sizes.get(size, 50000)
    
    events = ['page_view', 'click', 'add_to_cart', 'purchase', 'logout']
    data = {
        'event_id': range(1, n + 1),
        'user_id': np.random.randint(1, 1000, n),
        'event_type': np.random.choice(events, n),
        'timestamp': pd.date_range('2023-01-01', periods=n, freq='min'),
        'page_url': f'/page{np.random.randint(1, 100)}',
        'session_id': [f'session_{i % 100}' for i in range(n)]
    }
    
    df = pd.DataFrame(data)
    df.to_json('data/sample/user_events.json', orient='records', lines=True)
    print(f"Generated {n} user events")

def generate_log_data(size='medium'):
    """Generate server log data."""
    sizes = {'small': 10000, 'medium': 100000, 'large': 1000000}
    n = sizes.get(size, 100000)
    
    log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
    data = {
        'timestamp': pd.date_range('2023-01-01', periods=n, freq='S'),
        'level': np.random.choice(log_levels, n),
        'service': np.random.choice(['api', 'web', 'database', 'cache'], n),
        'message': [f'Log message {i}' for i in range(n)],
        'request_id': [f'req_{i}' for i in range(n)]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('data/sample/server_logs.csv', index=False)
    print(f"Generated {n} log entries")

def generate_user_profiles(size='medium'):
    """Generate user profile data."""
    sizes = {'small': 500, 'medium': 5000, 'large': 50000}
    n = sizes.get(size, 5000)
    
    data = {
        'user_id': range(1, n + 1),
        'username': [f'user_{i}' for i in range(1, n + 1)],
        'email': [f'user{i}@example.com' for i in range(1, n + 1)],
        'signup_date': pd.date_range('2023-01-01', periods=n, freq='D'),
        'activity_score': np.random.randint(0, 100, n),
        'subscription_tier': np.random.choice(['free', 'premium', 'enterprise'], n)
    }
    
    df = pd.DataFrame(data)
    df.to_parquet('data/sample/user_profiles.parquet', index=False)
    print(f"Generated {n} user profiles")

def main():
    parser = argparse.ArgumentParser(description='Generate sample data for Apache Beam practice')
    parser.add_argument('--size', choices=['small', 'medium', 'large'], default='medium',
                        help='Size of dataset to generate')
    args = parser.parse_args()
    
    print(f"Generating {args.size} sample data...")
    generate_sales_data(args.size)
    generate_user_events(args.size)
    generate_log_data(args.size)
    generate_user_profiles(args.size)
    print("\n✓ Sample data generation complete!")

if __name__ == "__main__":
    main()
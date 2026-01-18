"""
Sales Data Generator for Sales Intelligence Dashboard
Generates realistic synthetic sales data for analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from faker import Faker
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)
fake = Faker()
Faker.seed(42)

print("Starting sales data generation...")

# Configuration
NUM_CUSTOMERS = 10000
NUM_TRANSACTIONS = 50000
NUM_PRODUCTS = 25
NUM_SALES_REPS = 15
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Product Categories and Products
PRODUCT_CATEGORIES = {
    'Software': ['CRM Pro', 'Analytics Suite', 'Security Package', 'Cloud Storage', 'AI Tools'],
    'Hardware': ['Laptop', 'Desktop', 'Server', 'Router', 'Switch'],
    'Services': ['Consulting', 'Training', 'Support Gold', 'Support Platinum', 'Implementation'],
    'Subscriptions': ['Monthly Plan', 'Annual Plan', 'Enterprise Plan', 'Startup Plan', 'Premium Plan'],
    'Add-ons': ['Extra Users', 'API Access', 'Custom Reports', 'Priority Support', 'Data Export']
}

# Price ranges by category (min, max)
PRICE_RANGES = {
    'Software': (500, 5000),
    'Hardware': (800, 8000),
    'Services': (1000, 15000),
    'Subscriptions': (100, 2000),
    'Add-ons': (50, 500)
}

# Customer segments
CUSTOMER_SEGMENTS = ['Enterprise', 'Mid-Market', 'Small Business', 'Startup']
SEGMENT_WEIGHTS = [0.15, 0.25, 0.40, 0.20]

# Industries
INDUSTRIES = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Manufacturing',
              'Education', 'Media', 'Consulting', 'Real Estate', 'Logistics']

# US States
STATES = ['CA', 'NY', 'TX', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI',
          'NJ', 'VA', 'WA', 'AZ', 'MA', 'TN', 'IN', 'MO', 'MD', 'WI']

print("Generating customers...")

# Generate Customers
customers = []
for i in range(NUM_CUSTOMERS):
    customer_id = f"CUST{i+1:05d}"
    segment = np.random.choice(CUSTOMER_SEGMENTS, p=SEGMENT_WEIGHTS)

    # Segment affects company size and revenue potential
    if segment == 'Enterprise':
        employees = np.random.randint(1000, 10000)
        revenue_potential = np.random.randint(50000, 200000)
    elif segment == 'Mid-Market':
        employees = np.random.randint(100, 1000)
        revenue_potential = np.random.randint(20000, 80000)
    elif segment == 'Small Business':
        employees = np.random.randint(10, 100)
        revenue_potential = np.random.randint(5000, 30000)
    else:  # Startup
        employees = np.random.randint(5, 50)
        revenue_potential = np.random.randint(2000, 15000)

    customer = {
        'customer_id': customer_id,
        'company_name': fake.company(),
        'segment': segment,
        'industry': np.random.choice(INDUSTRIES),
        'state': np.random.choice(STATES),
        'city': fake.city(),
        'employees': employees,
        'revenue_potential': revenue_potential,
        'signup_date': fake.date_between(start_date=START_DATE, end_date=END_DATE),
        'contact_name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number()
    }
    customers.append(customer)

customers_df = pd.DataFrame(customers)
print(f"Generated {len(customers_df)} customers")

print("Generating products...")

# Generate Products
products = []
product_id = 1
for category, product_names in PRODUCT_CATEGORIES.items():
    for product_name in product_names:
        min_price, max_price = PRICE_RANGES[category]
        base_price = np.random.randint(min_price, max_price)

        product = {
            'product_id': f"PROD{product_id:03d}",
            'product_name': product_name,
            'category': category,
            'base_price': base_price,
            'cost': base_price * 0.4,  # 60% margin
            'is_recurring': category == 'Subscriptions'
        }
        products.append(product)
        product_id += 1

products_df = pd.DataFrame(products)
print(f"Generated {len(products_df)} products")

print("Generating sales representatives...")

# Generate Sales Reps
sales_reps = []
for i in range(NUM_SALES_REPS):
    rep = {
        'rep_id': f"REP{i+1:03d}",
        'rep_name': fake.name(),
        'region': np.random.choice(['East', 'West', 'Central', 'North', 'South']),
        'experience_years': np.random.randint(1, 15),
        'hire_date': fake.date_between(start_date=datetime(2015, 1, 1), end_date=datetime(2023, 12, 31))
    }
    sales_reps.append(rep)

sales_reps_df = pd.DataFrame(sales_reps)
print(f"Generated {len(sales_reps_df)} sales representatives")

print("Generating transactions (this may take a moment)...")

# Generate Transactions
transactions = []
for i in range(NUM_TRANSACTIONS):
    # Select random customer
    customer = customers_df.sample(1).iloc[0]

    # Transaction date (weighted towards more recent dates)
    days_range = (END_DATE - START_DATE).days
    # Use beta distribution to weight towards recent dates
    date_weight = np.random.beta(2, 5)
    transaction_date = START_DATE + \
        timedelta(days=int(date_weight * days_range))

    # Select product
    product = products_df.sample(1).iloc[0]

    # Quantity (influenced by customer segment)
    if customer['segment'] == 'Enterprise':
        quantity = np.random.randint(5, 50)
    elif customer['segment'] == 'Mid-Market':
        quantity = np.random.randint(2, 20)
    else:
        quantity = np.random.randint(1, 10)

    # Discount (larger customers get bigger discounts)
    segment_discount = {
        'Enterprise': np.random.uniform(0.10, 0.25),
        'Mid-Market': np.random.uniform(0.05, 0.15),
        'Small Business': np.random.uniform(0.02, 0.10),
        'Startup': np.random.uniform(0, 0.08)
    }
    discount = segment_discount[customer['segment']]

    # Calculate amounts
    unit_price = product['base_price']
    gross_amount = unit_price * quantity
    discount_amount = gross_amount * discount
    net_amount = gross_amount - discount_amount

    # Sales stage and status
    stages = ['Lead', 'Qualified', 'Proposal',
              'Negotiation', 'Closed Won', 'Closed Lost']
    stage_weights = [0.05, 0.10, 0.10, 0.15, 0.50, 0.10]
    stage = np.random.choice(stages, p=stage_weights)

    # Select sales rep
    rep = sales_reps_df.sample(1).iloc[0]

    transaction = {
        'transaction_id': f"TXN{i+1:06d}",
        'transaction_date': transaction_date,
        'customer_id': customer['customer_id'],
        'product_id': product['product_id'],
        'rep_id': rep['rep_id'],
        'quantity': quantity,
        'unit_price': unit_price,
        'gross_amount': gross_amount,
        'discount_pct': discount,
        'discount_amount': discount_amount,
        'net_amount': net_amount,
        'cost': product['cost'] * quantity,
        'profit': net_amount - (product['cost'] * quantity),
        'stage': stage,
        'is_won': stage == 'Closed Won',
        'days_to_close': np.random.randint(7, 180) if stage in ['Closed Won', 'Closed Lost'] else None
    }
    transactions.append(transaction)

transactions_df = pd.DataFrame(transactions)
print(f"Generated {len(transactions_df)} transactions")

# Calculate some aggregate metrics
print("\n" + "="*60)
print("DATA GENERATION SUMMARY")
print("="*60)
print(f"Total Customers: {len(customers_df):,}")
print(f"Total Products: {len(products_df):,}")
print(f"Total Sales Reps: {len(sales_reps_df):,}")
print(f"Total Transactions: {len(transactions_df):,}")
print(f"\nDate Range: {START_DATE.date()} to {END_DATE.date()}")

# Calculate revenue metrics
total_revenue = transactions_df[transactions_df['is_won']]['net_amount'].sum()
total_profit = transactions_df[transactions_df['is_won']]['profit'].sum()

print(f"\nTotal Revenue (Closed Won): ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(
    f"Average Deal Size: ${transactions_df[transactions_df['is_won']]['net_amount'].mean():,.2f}")

print("\nSegment Distribution:")
print(customers_df['segment'].value_counts())

print("\nTop 5 Products by Revenue:")
product_revenue = transactions_df[transactions_df['is_won']].groupby(
    'product_id')['net_amount'].sum().sort_values(ascending=False).head()
for prod_id, revenue in product_revenue.items():
    prod_name = products_df[products_df['product_id']
                            == prod_id]['product_name'].values[0]
    print(f"  {prod_name}: ${revenue:,.2f}")

# Save to CSV files
print("\n" + "="*60)
print("Saving data to CSV files...")
print("="*60)

customers_df.to_csv('data/raw/customers.csv', index=False)
print("✓ Saved: data/raw/customers.csv")

products_df.to_csv('data/raw/products.csv', index=False)
print("✓ Saved: data/raw/products.csv")

sales_reps_df.to_csv('data/raw/sales_reps.csv', index=False)
print("✓ Saved: data/raw/sales_reps.csv")

transactions_df.to_csv('data/raw/transactions.csv', index=False)
print("✓ Saved: data/raw/transactions.csv")

print("\n" + "="*60)
print("DATA GENERATION COMPLETE!")
print("="*60)
print("\nNext steps:")
print("1. Review the generated CSV files in data/raw/")
print("2. Run the analysis notebook to process the data")
print("3. Import processed data into Tableau")
print("\nAll data files are ready for analysis!")

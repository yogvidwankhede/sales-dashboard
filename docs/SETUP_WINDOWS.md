# Setup Instructions for Windows

## Step 1: Open Command Prompt
- Press `Windows Key + R`
- Type `cmd` and press Enter
- Navigate to Desktop: `cd Desktop\sales-dashboard`

## Step 2: Create Virtual Environment
```bash
python -m venv venv
```

## Step 3: Activate Virtual Environment
```bash
venv\Scripts\activate
```

## Step 4: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Step 5: Verify Installation
```bash
python -c "import pandas; import numpy; import sklearn; print('Success!')"
```

## Next Steps
Run: `python src/generate_sales_data.py`
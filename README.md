# Excel Merge Automation (Basic)

Simple Python script to merge multiple Excel files into one output file.

## Features
- Merge multiple `.xlsx` files
- Timestamped output (no overwrite)
- Logging for audit & troubleshooting
- Simple & lightweight

## Use Case
- Daily / weekly Excel reporting
- Manual Excel merge replacement
- Small business data processing

## How to Run
```bash
pip install -r requirements.txt
python merge_excel.py
```

## How to install
- Command
```bash
pip install pyinstaller
pyinstaller --onefile merge_excel.py
```
- Make sure have folder before the apps used contains: data, output and logs
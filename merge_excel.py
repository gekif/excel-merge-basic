import pandas as pd
from pathlib import Path
from datetime import datetime
import logging

# Setup logging
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def merge_excel():
    try:
        data_folder = Path("data")
        output_folder = Path("output")
        output_folder.mkdir(exist_ok=True)

        files = list(data_folder.glob("*.xlsx"))
        if not files:
            raise ValueError("No Excel files found in data folder")

        dfs = []
        for file in files:
            df = pd.read_excel(file)
            dfs.append(df)
            logging.info(f"Loaded file: {file.name}")

        merged = pd.concat(dfs, ignore_index=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_folder / f"merged_{timestamp}.xlsx"
        merged.to_excel(output_file, index=False)

        logging.info(f"Output created: {output_file.name}")
        print("✅ Merge success:", output_file.name)

    except Exception as e:
        logging.error(f"Error: {e}")
        print("❌ Error:", e)


if __name__ == "__main__":
    merge_excel()

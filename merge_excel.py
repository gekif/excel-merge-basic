import logging
from datetime import datetime
from pathlib import Path

import pandas as pd


# =========================
# CONSTANTS
# =========================
DATA_FOLDER = Path("data")
OUTPUT_FOLDER = Path("output")
LOG_FOLDER = Path("logs")
LOG_FILE = LOG_FOLDER / "app.log"
DATE_COLUMN_NAME = "tanggal"
DATE_FORMAT = "%d/%m/%Y"


# =========================
# LOGGING SETUP
# =========================
def setup_logging() -> None:
    """
    Configure application logging.
    """
    LOG_FOLDER.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


# =========================
# CORE FUNCTIONS
# =========================
def load_excel_files(folder: Path) -> list[pd.DataFrame]:
    """
    Load all Excel files from a folder into a list of DataFrames.
    """
    excel_files = list(folder.glob("*.xlsx"))

    if not excel_files:
        raise ValueError("No Excel files found in data folder")

    dataframes = []

    for excel_file in excel_files:
        df = pd.read_excel(excel_file)
        dataframes.append(df)
        logging.info("Loaded file: %s", excel_file.name)

    return dataframes


def format_date_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Format date column to dd/mm/yyyy if the column exists.
    """
    if DATE_COLUMN_NAME in df.columns:
        df[DATE_COLUMN_NAME] = (
            pd.to_datetime(df[DATE_COLUMN_NAME], errors="coerce")
            .dt.strftime(DATE_FORMAT)
        )

    return df


def save_merged_file(df: pd.DataFrame, output_folder: Path) -> Path:
    """
    Save merged DataFrame to Excel with timestamped filename.
    """
    output_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_folder / f"merged_{timestamp}.xlsx"

    df.to_excel(output_file, index=False)
    logging.info("Output created: %s", output_file.name)

    return output_file


# =========================
# MAIN ORCHESTRATOR
# =========================
def merge_excel() -> None:
    """
    Main function to merge Excel files.
    """
    try:
        dataframes = load_excel_files(DATA_FOLDER)
        merged_df = pd.concat(dataframes, ignore_index=True)

        merged_df = format_date_column(merged_df)
        output_file = save_merged_file(merged_df, OUTPUT_FOLDER)

        print("✅ Merge success:", output_file.name)

    except Exception as error:
        logging.error("Merge failed: %s", error)
        print("❌ Error:", error)


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    setup_logging()
    merge_excel()
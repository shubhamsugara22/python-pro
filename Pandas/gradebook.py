from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
DATA_FOLDER = HERE/"data"

roster = pd.read_csv(DATA_FOLDER/"roster.csv", converters={}, usecols=[], index_col=)

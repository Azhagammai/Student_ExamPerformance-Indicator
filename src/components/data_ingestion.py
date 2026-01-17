import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation

from src.components.model_trainer  import ModelTrainerConfig
from src.components.model_trainer  import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

        # 🔥 Project root directory
        self.project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../")
        )

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting Data Ingestion")

            raw_csv_path = os.path.join(
                self.project_root, "notebook", "data", "raw.csv"
            )

            logging.info(f"Reading data from: {raw_csv_path}")

            df = pd.read_csv(raw_csv_path)

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42
            )

            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data Ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr, test_arr, preprocessor_path = (
    data_transformation.initiate_data_transformation(train_data, test_data)
)
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
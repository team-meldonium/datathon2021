import pandas as pd
import os

from src.utils import get_data_folder_info
from src.create_df import (create_edu_df,
                           create_med_df,
                           create_sport_df)

ROOT_FOLDER = '../'
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_INFO = get_data_folder_info(DATA_FOLDER)

edu_df = create_edu_df(DATA_INFO)
med_df = create_med_df(DATA_INFO)
sport_df = create_sport_df(DATA_INFO)


res_df = pd.concat((edu_df, med_df, sport_df), ignore_index=True)
res_df.to_csv('dataset.csv', index=False)
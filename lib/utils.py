#  Created by btrif Trif on 06-06-2022 , 12:54 PM.

import pandas as pd
from datetime import datetime, timedelta

json_file = "../tools/Pandas test large data set/MOCK_DATA.json"

data = pd.read_json(json_file)
dob1 = data['date_of_birth'][4]


def get_age_from_birthday(dob : str) -> int :

    birth_date = datetime.strptime(dob, "%d/%m/%Y")
    print(f'birth_Date : {birth_date}')
    year, month, day = birth_date.year, birth_date.month, birth_date.day
    print(f'year : {year}, month : {month}, day: {day}')
    age = datetime.now().year - year
    print(f'Age = {age}')
    return age



get_age_from_birthday(dob1)

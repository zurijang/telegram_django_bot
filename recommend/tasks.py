import pandas as pd

def LoadData(state, province, type1):  # load_data
    data = pd.read_csv('recommend\combine_TMAP_ver_1.csv')
    data = data.drop('Unnamed: 0', axis=1)
    data['점수'] = (data['검색지랭킹(시군구내)'] * 1.55) + (data['검색지빈도'] * 0.025)
    result_data = data[(data['지역(시도)']==state) & (data['지역(시군구)']==province) & (data['검색지유형1']==type1)]
    return result_data.sort_values('점수', ascending=False)

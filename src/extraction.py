import numpy as np
import pandas as pd
import pyreadstat


def proses_xpt_ke_csv(tahun, xpt_path, output_csv):
  print(f'Sedang memproses data BRFSS {tahun} dari {xpt_path}...')

  df_raw, _ = pyreadstat.read_xport(xpt_path, encoding='latin1')
  df = pd.DataFrame()

  df['HighBP'] = df_raw['_RFHYPE6'].map({1: 0, 2: 1})
  col_chol = '_RFCHOL3' if '_RFCHOL3' in df_raw.columns else 'TOLDHI3'
  df['HighChol'] = df_raw[col_chol].map({1: 0, 2: 1})
  df['CholCheck'] = df_raw['_CHOLCH3'].apply(
      lambda x: 1 if x == 1 else (0 if x in [2, 3] else np.nan)
  )
  df['Smoker'] = df_raw['SMOKE100'].map({1: 1, 2: 0})
  df['Stroke'] = df_raw['CVDSTRK3'].map({1: 1, 2: 0})
  df['HeartDiseaseorAttack'] = df_raw['_MICHD'].map({1: 1, 2: 0})
  df['PhysActivity'] = df_raw['_TOTINDA'].map({1: 1, 2: 0})
  df['Fruits'] = df_raw['_FRTLT1A'].map({1: 1, 2: 0})
  df['Veggies'] = df_raw['_VEGLT1A'].map({1: 1, 2: 0})

  col_alc = '_RFDRHV8' if tahun == '2023' else '_RFDRHV9'
  df['HvyAlcoholConsump'] = df_raw[col_alc].map({1: 0, 2: 1})

  col_hlth = '_HLTHPL1' if tahun == '2023' else '_HLTHPL2'
  df['AnyHealthcare'] = df_raw[col_hlth].map({1: 1, 0: 2})

  df['NoDocbcCost'] = df_raw['MEDCOST1'].map({1: 1, 2: 0})
  df['DiffWalk'] = df_raw['DIFFWALK'].map({1: 1, 2: 0})

  col_sex = '_SEX' if '_SEX' in df_raw.columns else 'SEXVAR'
  df['Sex'] = df_raw[col_sex].map({1: 1, 2: 0})

  df['BMI'] = df_raw['_BMI5'] / 100.0
  df['MentHlth'] = (
      df_raw['MENTHLTH']
      .replace({88: 0})
      .apply(lambda x: x if 0 <= x <= 30 else np.nan)
  )
  df['PhysHlth'] = (
      df_raw['PHYSHLTH']
      .replace({88: 0})
      .apply(lambda x: x if 0 <= x <= 30 else np.nan)
  )
  df['GenHlth'] = df_raw['GENHLTH'].apply(lambda x: x if 1 <= x <= 5 else np.nan)
  df['Age'] = df_raw['_AGEG5YR'].apply(lambda x: x if 1 <= x <= 13 else np.nan)
  df['Education'] = df_raw['EDUCA'].apply(lambda x: x if 1 <= x <= 6 else np.nan)

  col_inc = '_INCOMG1' if '_INCOMG1' in df_raw.columns else 'INCOME3'
  df['Income'] = df_inc.apply(lambda x: x if 1 <= x <= 8 else np.nan) if 'col_inc' in locals() else df_raw[col_inc].apply(lambda x: x if 1 <= x <= 8 else np.nan)

  df['Diabetes_012'] = df_raw['DIABETE4'].map({1: 2, 4: 1, 2: 0, 3: 0})
  df = df.dropna(subset=['Diabetes_012'])
  df['Diabetes_012'] = df['Diabetes_012'].astype(int)

  df.to_csv(output_csv, index=False)
  print(
      f'-> Berhasil menyimpan file: {output_csv} (Total baris utuh:'
      f' {len(df):,})\n'
  )
  return df


if __name__ == '__main__':
  df_23 = proses_xpt_ke_csv(
      '2023', 'data/LLCP2023.XPT', 'BRFSS_CDC_Diabetes_2023.csv'
  )
  df_24 = proses_xpt_ke_csv(
      '2024', 'data/LLCP2024.XPT', 'BRFSS_CDC_Diabetes_2024.csv'
  )
  df_25 = proses_xpt_ke_csv(
      '2025', 'data/LLCP2025.XPT', 'BRFSS_CDC_Diabetes_2025.csv'
  )

  df_combined = pd.concat([df_23, df_24, df_25], ignore_index=True)
  df_combined.to_csv('BRFSS_CDC_Diabetes_2023_2024_2025.csv', index=False)
  print(
      'Berhasil membuat file gabungan: BRFSS_CDC_Diabetes_2023_2024_2025.csv'
      f' (Total baris gabungan: {len(df_combined):,})'

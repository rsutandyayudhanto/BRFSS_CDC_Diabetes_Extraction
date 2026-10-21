# BRFSS CDC Diabetes Data Extraction Pipeline

Repositori ini mendokumentasikan kode sumber, kamus data (*codebooks*), dan panduan penyiapan dataset *Behavioral Risk Factor Surveillance System* (BRFSS) CDC tahun **2023, 2024, dan 2025**.

Pipeline ini disusun untuk mendukung penelitian skripsi berjudul:
> *"Optimasi Integrasi XGBoost dan Bayesian Optimization untuk Peningkatan Akurasi Prediksi Diabetes"*

## 📂 Struktur Repositori
- `src/extraction.py`: Skrip otomatis untuk membaca file SAS Transport (`.XPT`), memetakan 22 variabel utama secara utuh, hingga menghasilkan file luaran CSV:
  - `BRFSS_CDC_Diabetes_2023.csv`
  - `BRFSS_CDC_Diabetes_2024.csv`
  - `BRFSS_CDC_Diabetes_2025.csv`
  - `BRFSS_CDC_Diabetes_2023_2024_2025.csv` (File gabungan multi-tahun)
- `codebooks/`: Berisi dokumentasi kamus data resmi berformat HTML (*Codebook Report*) untuk tahun 2023, 2024, dan 2025.
- `data/`: Berisi informasi dan data mentah `.XPT` CDC (karena keterbatasan ruang maka `.XPT` disimpan pada folder Google Drive).
- `requirements.txt`: Daftar pustaka Python yang dibutuhkan.
- `output/`: Berisi file luaran dataset `.CSV` (karena keterbatasan ruang maka file luaran `.CSV` disimpan pada folder Google Drive):
  - `BRFSS_CDC_Diabetes_2023.csv`
  - `BRFSS_CDC_Diabetes_2024.csv`
  - `BRFSS_CDC_Diabetes_2025.csv`
  - `BRFSS_CDC_Diabetes_2023_2024_2025.csv` (File gabungan multi-tahun)

## ⚙️ Cara Menjalankan Skrip
1. Unduh file `.XPT` mentah dari tautan folder Google Drive di folder `data/`.
2. Pasang dependensi pustaka:
   ```bash
   pip install -r requirements.txt

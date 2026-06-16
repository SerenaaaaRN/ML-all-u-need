# Prediksi Biaya Asuransi Medis

Dataset ini berisi data biaya asuransi medis individu di Amerika Serikat, mencakup faktor-faktor seperti usia, BMI, jumlah tanggungan, status merokok, dan wilayah tempat tinggal. Biaya asuransi kesehatan sangat bervariasi antar individu — ada yang hanya membayar beberapa ribu dolar, ada pula yang mencapai puluhan ribu. Bisakah kita memprediksi berapa biaya asuransi seseorang berdasarkan profil demografis dan kesehatannya?

## Data
- **Source:** Medical Cost Personal Dataset (Kaggle)
- **Jumlah baris:** 1.338
- **Jumlah kolom:** 7
- **Target:** `charges` (biaya asuransi medis dalam USD)

## EDA Insights
- Tidak ada missing values — data bersih dari sisi kelengkapan.
- Kolom charges memiliki 10,39% outlier dengan distribusi yang sangat right-skewed — sebagian besar biaya rendah, beberapa ekstrem tinggi.
- BMI memiliki 0,67% outlier — hanya 9 individu dengan BMI ekstrem.
- Dataset seimbang secara demografis antara pria dan wanita, dengan distribusi region yang cukup merata.
- Status merokok (smoker) muncul sebagai faktor dominan — perokok cenderung memiliki biaya jauh lebih tinggi.

## Hasil Model
| Model | R2_Score | RMSE | MAE |
|-------|----------|------|-----|
| GradientBoosting | 0.8928 | 4439.32 | 2640.92 |
| RandomForest | 0.8797 | 4701.39 | 2650.11 |
| LinearRegression | 0.8070 | 5954.75 | 4182.31 |
| ElasticNet | 0.3357 | 11048.84 | 7987.71 |
| SVR | -0.1324 | 14424.91 | 9266.95 |

**Winner:** GradientBoosting (R2=0,893, RMSE=4.439)

## Cara Jalanin
```bash
python "medical cost personal/src/main.py"
```

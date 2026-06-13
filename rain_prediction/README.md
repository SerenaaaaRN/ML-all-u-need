# Prediksi Hujan (Australia)

Dataset ini berisi data cuaca harian dari berbagai stasiun cuaca di Australia selama kurang lebih 10 tahun (2008–2017). Setiap baris mencatat kondisi cuaca seperti suhu, kelembapan, tekanan udara, arah angin, dan curah hujan. Pertanyaan utamanya sederhana: bisakah kita memprediksi apakah besok akan hujan hanya berdasarkan data cuaca hari ini? Ini relevan untuk pertanian, pariwisata, dan perencanaan aktivitas sehari-hari.

## Data
- **Source:** Weather Dataset (Kaggle — Australian Government Bureau of Meteorology)
- **Jumlah baris:** 145.460
- **Jumlah kolom:** 23
- **Target:** `RainTomorrow` (Yes / No)

## EDA Insights
- Dataset sangat besar (145 ribu baris) dengan 23 kolom — gabungan numerik, kategorikal, dan tanggal.
- Target sangat imbalance: 77,6% tidak hujan vs hanya 22,4% hujan besok. Model harus waspada dengan bias ke kelas mayoritas.
- Empat kolom memiliki missing value di atas 38%: Sunshine (48%), Evaporation (43%), Cloud3pm (41%), Cloud9am (38%) — akhirnya di-drop.
- Kolom Rainfall memiliki outlier hingga 18% — wajar karena curah hujan ekstrem jarang terjadi tapi mencolok.
- Ada 49 lokasi unik di seluruh Australia — perlu penanganan khusus karena kardinalitas tinggi (pake TargetEncoder).
- Kolom arah angin (WindGustDir, WindDir9am, WindDir3pm) adalah kategorikal sirkular yang setelah OneHotEncoder meledak jadi 48 kolom baru.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| RandomForest | 0.8506 | 0.8376 | 0.8757 |
| GradientBoosting | 0.8448 | 0.8319 | 0.8607 |
| LogisticRegression | 0.8392 | 0.8265 | 0.8538 |
| KNN | 0.8234 | 0.8094 | 0.7952 |
| DecisionTree | 0.7827 | 0.7840 | 0.6945 |
| NaiveBayes | 0.7072 | 0.7268 | 0.7536 |

**Winner:** RandomForest (Accuracy 85,1%, ROC-AUC 0,876)

## Cara Jalanin
```bash
python rain_prediction/src/main.py
```

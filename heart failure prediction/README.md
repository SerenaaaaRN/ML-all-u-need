# Prediksi Penyakit Jantung

Dataset ini berisi data pasien dengan berbagai indikator kesehatan seperti usia, jenis kelamin, tekanan darah, kadar kolesterol, dan hasil elektrokardiografi. Penyakit jantung adalah salah satu penyebab kematian tertinggi di dunia, dan deteksi dini bisa menyelamatkan nyawa. Bisakah kita memprediksi apakah seseorang memiliki penyakit jantung berdasarkan parameter medis yang umum diukur?

## Data
- **Source:** Heart Failure Prediction Dataset (Kaggle)
- **Jumlah baris:** 918
- **Jumlah kolom:** 12
- **Target:** `HeartDisease` (1: penyakit jantung, 0: tidak)

## EDA Insights
- Tidak ada missing values sama sekali — data siap olah tanpa perlu imputasi.
- Beberapa kolom memiliki outlier: FastingBS (23,31%), Cholesterol (19,93%), RestingBP (3,05%), Oldpeak (1,74%), dan MaxHR (0,22%).
- FastingBS dan Cholesterol punya outlier tinggi — wajar karena kadar gula darah dan kolesterol bisa sangat bervariasi secara medis.
- Target cukup balanced: 55,34% positif vs 44,66% negatif — rasio imbalance hanya 1,24x, jadi tidak perlu handling khusus.
- ChestPainType dan ST_Slope adalah fitur kategorikal yang perlu di-encode, sementara kolom numerik seperti Age, RestingBP, dan Cholesterol bisa langsung di-scale.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| GradientBoosting | 0.8750 | 0.8751 | 0.9268 |
| RandomForest | 0.8641 | 0.8642 | 0.9316 |
| SVM | 0.8533 | 0.8531 | 0.9442 |
| LogisticReg | 0.8478 | 0.8487 | 0.9240 |
| DecisionTree | 0.8478 | 0.8481 | 0.8455 |
| KNN | 0.8424 | 0.8425 | 0.9038 |

**Winner:** GradientBoosting (Accuracy 87,5%, ROC-AUC 0,927)

## Cara Jalanin
```bash
python "heart failure prediction/src/main.py"
```

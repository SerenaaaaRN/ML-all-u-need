# Prediksi Diabetes

Dataset ini berisi data medis pasien perempuan keturunan suku Pima dengan berbagai indikator kesehatan seperti kadar glukosa, tekanan darah, BMI, dan insulin. Diabetes adalah salah satu penyakit kronis yang paling umum di dunia, dan deteksi dini sangat penting untuk mencegah komplikasi serius. Dataset ini memungkinkan kita melihat pola dari hasil tes medis sederhana yang bisa membantu memprediksi apakah seseorang menderita diabetes atau tidak.

## Data
- **Source:** Pima Indians Diabetes Database (Kaggle / UCI)
- **Jumlah baris:** 768
- **Jumlah kolom:** 9
- **Target:** `Outcome` (1: diabetes, 0: tidak)

## EDA Insights
- Nilai 0 pada kolom Glucose, BloodPressure, SkinThickness, Insulin, dan BMI sebenarnya adalah missing value — bukan angka normal secara medis. Ini perlu diimputasi.
- Sebanyak 8 dari 9 kolom numerik memiliki outlier, terutama BloodPressure (5,86%) dan Insulin.
- Target cukup imbalance: 65% tidak diabetes vs 35% diabetes, tapi masih wajar untuk classification.
- Glucose memiliki korelasi paling kuat dengan Outcome — masuk akal karena gula darah adalah indikator utama diabetes.
- Insulin banyak bernilai 0 (kemungkinan besar tidak diukur), bukan berarti kadarnya benar-benar nol.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| NaiveBayes | 0.7662 | 0.7679 | 0.8253 |
| DecisionTree | 0.7468 | 0.7503 | 0.7424 |
| SVM | 0.7338 | 0.7293 | 0.8051 |
| RandomForest | 0.7338 | 0.7343 | 0.8198 |
| GradientBoosting | 0.7338 | 0.7369 | 0.7864 |
| KNN | 0.6948 | 0.6896 | 0.7641 |

**Winner:** NaiveBayes (Accuracy 76,6%, ROC-AUC 0,825)

## Cara Jalanin
```bash
python diabetes_prediction/src/main.py
```

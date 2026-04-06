# Prediksi Klik Iklan

Dataset ini berisi data pengguna media sosial dengan informasi demografis seperti usia, jenis kelamin, dan perkiraan gaji, serta label apakah mereka mengklik iklan atau tidak. Dalam dunia digital marketing, memahami siapa yang paling mungkin merespon iklan sangat penting untuk efisiensi biaya iklan dan penargetan audiens yang tepat. Dataset ini memungkinkan kita mengeksplorasi faktor-faktor yang memengaruhi keputusan seseorang untuk mengklik sebuah iklan.

## Data
- **Source:** Social Network Ads (Kaggle)
- **Jumlah baris:** 400
- **Jumlah kolom:** 5
- **Target:** `Purchased` (apakah pengguna mengklik iklan)

## EDA Insights
- Proporsi target cukup timpang: 64% tidak klik, 36% klik — artinya model harus pintar-pintar mendeteksi calon pengklik.
- Tidak ada missing values dan tidak ada outlier signifikan, jadi data ini relatif bersih.
- Jenis kelamin (Gender) perlu di-encode karena kategorikal, sementara Age dan EstimatedSalary langsung bisa di-scale.
- User ID tidak relevan sebagai fitur karena unik per baris — harus di-drop sebelum training.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| NaiveBayes | 0.9211 | 0.9222 | 0.9554 |
| SVM | 0.8816 | 0.8837 | 0.9576 |
| KNN | 0.8816 | 0.8837 | 0.9308 |
| RandomForest | 0.8684 | 0.8707 | 0.9304 |
| LogisticRegression | 0.8026 | 0.8033 | 0.9055 |
| DecisionTree | 0.7895 | 0.7926 | 0.8099 |

**Winner:** NaiveBayes (Accuracy 92,1%, ROC-AUC 0,955)

## Cara Jalanin
```bash
python advertisement_click_prediction/src/main.py
```

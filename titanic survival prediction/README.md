# Prediksi Survival Titanic

Dataset ini berisi data penumpang kapal Titanic yang tenggelam pada 15 April 1912, mencakup informasi seperti kelas tiket, jenis kelamin, usia, jumlah kerabat di kapal, dan tarif. Dari 2.224 penumpang dan awak kapal, hanya 706 yang selamat. Pertanyaannya,  faktor-faktor apa yang paling memengaruhi keselamatan seseorang saat tragedi? Apakah kelas tiket? Gender? Atau usia?

## Data
- **Source:** Titanic — Machine Learning from Disaster (Kaggle)
- **Jumlah baris:** 891
- **Jumlah kolom:** 12
- **Target:** `Survived` (0 / 1)

## EDA Insights
- Hanya 38,4% penumpang yang selamat — dataset cukup balance dibanding problem klasifikasi lain.
- Kolom Age memiliki 177 missing value (19,8%) — diimputasi menggunakan median berdasarkan Title dan Pclass.
- Kolom Cabin memiliki 687 missing value (77%) — terlalu banyak untuk diimputasi, akhirnya di-drop.
- Kolom Embarked hanya 2 missing value — diisi dengan modus (S).
- Penumpang kelas 1 (First Class) memiliki tingkat survival jauh lebih tinggi (63%) dibanding kelas 3 (24%).
- Perempuan memiliki tingkat survival ~74%, sementara pria hanya ~19% — "women and children first" benar-benar terjadi.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| RandomForest | 0.8492 | 0.8493 | 0.9100 |
| KNN | 0.8268 | 0.8266 | 0.8669 |
| LogisticReg | 0.8045 | 0.8038 | 0.8865 |
| DecisionTree | 0.8045 | 0.8050 | 0.8060 |
| NaiveBayes | 0.7877 | 0.7867 | 0.8282 |

**Winner:** RandomForest (Accuracy 84,9%, ROC-AUC 0,910)

## Cara Jalanin
```bash
python "titanic survival prediction/src/main.py"
```

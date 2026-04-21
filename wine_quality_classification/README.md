# Klasifikasi Kualitas Wine

Dataset ini berisi hasil analisis kimia dari berbagai sampel wine merah Portugis (Vinho Verde). Setiap sampel diukur 11 parameter kimia seperti kadar alkohol, keasaman, pH, dan kandungan sulfur — lalu diberi skor kualitas oleh panel ahli wine (skala 0–10). Pertanyaannya: bisakah kita memprediksi kualitas wine hanya dari komposisi kimianya? Ini menarik karena dalam industri anggur, penilaian kualitas biasanya subjektif dan mahal — pendekatan data-driven bisa jadi alternatif.

## Data
- **Source:** Wine Quality Dataset (UCI / Kaggle)
- **Jumlah baris:** 1.599
- **Jumlah kolom:** 12
- **Target:** `quality` (skor 0–10, Multiclass Classification)

## EDA Insights
- Sebelas fitur semuanya numerik — tidak ada kolom kategorikal sama sekali. Kimiawi wine murni angka.
- Target quality sangat tidak seimbang: skor 5 (42,6%) dan 6 (39,9%) mendominasi, sementara kualitas 3 dan 8 masing-masing hanya 0,6% dan 1,1% — ini masalah berat untuk multiclass classification.
- Tidak ada missing values sama sekali — data sangat bersih dari sisi kelengkapan.
- Residual sugar punya outlier terbanyak (9,7%) — wajar karena beberapa wine manis punya kadar gula jauh di atas rata-rata.
- Alkohol dan pH punya korelasi menarik dengan quality — wine berkualitas tinggi cenderung punya alkohol lebih tinggi dan pH sedikit lebih rendah.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| RandomForest | 0.6507 | 0.6287 | 0.8036 |
| SVM | 0.6471 | 0.6239 | 0.8459 |
| GradientBoosting | 0.6250 | 0.6189 | 0.7555 |
| LogisticRegression | 0.6066 | 0.5846 | 0.8327 |
| AdaBoost | 0.5699 | 0.5514 | 0.7852 |
| KNN | 0.5441 | 0.5265 | 0.6014 |
| DecisionTree | 0.5184 | 0.5189 | 0.5712 |

**Winner:** RandomForest (Accuracy 65,1%, F1-weighted 0,629)

## Cara Jalanin
```bash
python wine_quality_classification/src/main.py
```

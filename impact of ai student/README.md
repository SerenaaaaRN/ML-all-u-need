# Prediksi Risiko Burnout Akibat Penggunaan AI pada Mahasiswa

Dataset ini berisi data 50.000 mahasiswa yang mencatat kebiasaan penggunaan Generative AI (seperti ChatGPT, GitHub Copilot), metode belajar tradisional, dan kondisi psikologis selama satu semester. Setiap mahasiswa dikategorikan ke dalam tiga tingkat risiko burnout: Rendah, Sedang, atau Tinggi. Bisakah kita memprediksi risiko burnout seorang mahasiswa berdasarkan pola penggunaan AI-nya? Apakah mahasiswa yang terlalu bergantung pada AI lebih rentan burnout? Atau justru AI membantu mengurangi beban akademik?

## Data
- **Source:** AI Student Impact Dataset (Synthetic — Kaggle)
- **Jumlah baris:** 50.000
- **Jumlah kolom:** 16 (13 fitur setelah drop ID + 2 leakage)
- **Target:** `Burnout_Risk_Level` (Low / Medium / High) — multiclass

## EDA Insights
- Dataset sangat bersih — **tidak ada missing value** maupun duplikat.
- Target cukup seimbang: Medium 42,3%, Low 32,7%, High 25,0% — tidak perlu handling imbalance berat.
- Dua kolom **leakage** ditemukan dan di-drop: `Post_Semester_GPA` dan `Skill_Retention_Score` (keduanya adalah hasil *setelah* semester, tidak tersedia saat prediksi).
- `Weekly_GenAI_Hours` memiliki 5,17% outlier — mahasiswa yang menggunakan AI >25 jam/minggu termasuk kategori sangat intensif.
- Mayoritas mahasiswa menggunakan 2–3 tools AI berbeda (`Tool_Diversity`), dan hanya sebagian kecil yang berlangganan premium (`Paid_Subscription` ~26%).
- Institusi dengan kebijakan *Allowed_With_Citation* mendominasi, sementara *Strict_Ban* hanya minoritas — AI sudah mulai diterima di dunia akademik.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| HistGradientBoosting | 0.5301 | 0.5300 | 0.7094 |
| RandomForest | 0.5147 | 0.5150 | 0.6916 |
| LogisticReg | 0.5117 | 0.4969 | 0.7123 |
| NaiveBayes | 0.5099 | 0.5024 | 0.6936 |
| DecisionTree | 0.4309 | 0.4309 | 0.5695 |

**Winner:** HistGradientBoosting (Accuracy 53,0%, ROC-AUC 0,709)
— LogisticRegression unggul tipis di ROC-AUC (0,712) tapi kalah accuracy.

> **Catatan:** Accuracy seluruh model berkisar ~51–53%, hanya ~20% di atas random baseline (33%). Ini menunjukkan bahwa fitur yang tersedia (demografi, kebiasaan belajar, penggunaan AI) belum cukup untuk memprediksi burnout secara akurat. Faktor psikologis yang lebih dalam mungkin diperlukan.

## Cara Jalanin
```bash
python "impact of ai student/src/main.py"
```

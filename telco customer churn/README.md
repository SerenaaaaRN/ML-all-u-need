# Prediksi Churn Pelanggan Telco

Dataset ini berisi data pelanggan sebuah perusahaan telekomunikasi di Amerika, mencakup informasi demografis, layanan yang digunakan, durasi berlangganan, dan metode pembayaran. Churn (pelanggan berhenti berlangganan) adalah masalah besar di industri telekomunikasi — kehilangan pelanggan lama lebih mahal daripada mendapatkan pelanggan baru. Dengan dataset ini kita bisa menggali pola apa yang membuat pelanggan bertahan atau pergi.

## Data
- **Source:** Telco Customer Churn (Kaggle / IBM Samples)
- **Jumlah baris:** 7.043
- **Jumlah kolom:** 21
- **Target:** `Churn` (Yes / No)

## EDA Insights
- Churn rate sekitar 26,5% — artinya 1 dari 4 pelanggan berpotensi pergi. Cukup signifikan.
- Kolom TotalCharges terdeteksi sebagai object (string), bukan numerik — setelah diperiksa, ada beberapa nilai kosong yang bikin parsing error.
- Mayoritas kolom (16 dari 21) adalah kategorikal — mulai dari gender hingga metode pembayaran — perlu encoding besar-besaran.
- Pelanggan dengan kontrak bulanan (Month-to-month) jauh lebih sering churn dibanding yang kontrak tahunan — logis karena lebih mudah keluar.
- Tenure (lama berlangganan) sangat rendah pada pelanggan yang churn — artinya risiko churn paling tinggi di awal masa berlangganan.

## Hasil Model
| Model | Accuracy | F1_weighted | ROC_AUC |
|-------|----------|-------------|---------|
| LogisticReg | 0.7943 | 0.7897 | 0.8421 |
| RandomForest | 0.7879 | 0.7807 | 0.8243 |
| KNN | 0.7673 | 0.7615 | 0.7454 |
| DecisionTree | 0.7331 | 0.7372 | 0.6616 |
| NaiveBayes | 0.6541 | 0.6759 | 0.8180 |

**Winner:** LogisticReg (Accuracy 79,4%, ROC-AUC 0,842)

## Cara Jalanin
```bash
python "telco customer churn/src/main.py"
```

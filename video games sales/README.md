# Prediksi Penjualan Video Game

Dataset ini berisi data penjualan video game dari seluruh dunia, mencakup lebih dari 16 ribu game dengan informasi platform, genre, publisher, dan penjualan per region (NA, EU, JP, dan lainnya). Industri game adalah salah satu industri hiburan terbesar, dan memahami faktor apa yang membuat sebuah game laris bisa sangat berharga — apakah genre tertentu lebih laku? Apakah platform menentukan kesuksesan? Atau publisher besar selalu menang?

## Data
- **Source:** Video Game Sales (Kaggle)
- **Jumlah baris:** 16.598
- **Jumlah kolom:** 11
- **Target:** `Global_Sales` (penjualan global dalam jutaan USD)

## EDA Insights
- Tahun rilis (Year) dan Publisher memiliki missing value — 271 game tanpa tahun rilis, 58 game tanpa publisher.
- Penjualan sangat timpang: game teratas (Wii Sports) laku 82 juta, sementara ribuan game lain hanya laku ribuan — outlier sangat ekstrem di kolom sales.
- Genre Action adalah yang paling banyak diproduksi, tapi Genre Sports dan Platform malah punya penjualan rata-rata lebih tinggi.
- Wii adalah platform dengan game terlaris, disusul NES dan SNES — menunjukkan pengaruh basis pengguna terhadap penjualan.
- Penjualan NA (Amerika Utara) mendominasi total global — hampir setengah dari penjualan global berasal dari region ini.

## Hasil Model
| Model | R2_Score | RMSE | MAE |
|-------|----------|------|-----|
| GradientBoosting | 0.8495 | 0.8020 | 0.0366 |
| RandomForest | 0.7995 | 0.9256 | 0.0439 |
| LinearRegression | 0.6918 | 1.1478 | 0.2508 |
| ElasticNet | 0.6050 | 1.2994 | 0.2157 |
| SVR | 0.4251 | 1.5675 | 0.1097 |

**Winner:** GradientBoosting (R2=0,850, RMSE=0,802)

## Cara Jalanin
```bash
python "video games sales/src/main.py"
```

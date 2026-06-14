/**
 * Memformat nilai metrik menjadi string yang mudah dibaca oleh pengguna.
 * Secara khusus menangani 'Accuracy' dan 'R²' dengan mengubah desimal menjadi persentase.
 *
 * @param value - Nilai numerik mentah dari metrik.
 * @param metricName - Nama metrik (misalnya: 'Accuracy', 'R²', 'Loss').
 * @returns String yang telah diformat (contoh: "95%") atau nilai asli sebagai string.
 */
export function formatMetric(value: number, metricName: string): string {
  if (metricName === 'Accuracy' || metricName === 'R²') {
    return `${(value * 100).toFixed(0)}%`;
  }
  return value.toString();
}

/**
 * Mengekstrak dan mentransformasi fitur dari FormData berdasarkan skema yang diberikan.
 * Fungsi ini menangani konversi tipe data (string ke number), pemetaan opsi untuk dropdown,
 * serta logika khusus untuk field tertentu seperti 'gender' dan 'Location'.
 *
 * @param formData - Objek FormData yang berisi inputan dari pengguna.
 * @param schema - Array definisi field yang menjelaskan tipe data dan opsi yang tersedia.
 * @returns Sebuah objek record di mana kuncinya adalah nama field dan nilainya berupa number atau string.
 */
export function extractFeatures(
  formData: FormData,
  schema: any[]
): Record<string, number | string> {
  const features: Record<string, number | string> = {};
  for (const field of schema) {
    const val = formData.get(field.key);
    if (val === null) continue;

    if (field.type === 'number' || field.type === 'slider') {
      features[field.key] = Number(val);
      continue;
    }

    const options = field.options;
    let matchedOption: { label: string; value: string | number } | undefined;
    if (options) {
      const optionsMap = new Map<
        string,
        { label: string; value: string | number }
      >(options.map((o: any) => [o.value.toString(), o]));
      matchedOption = optionsMap.get(val.toString());
    }

    if (matchedOption && typeof matchedOption.value === 'number') {
      features[field.key] = Number(val);
    } else if (field.key === 'gender' || field.key === 'Location') {
      features[field.key] = String(val);
    } else {
      features[field.key] =
        !isNaN(Number(val)) && String(val).trim() !== ''
          ? Number(val)
          : String(val);
    }
  }
  return features;
}

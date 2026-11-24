# Mulai di sini — untuk orang awam

Tidak perlu belajar coding dulu. Kamu adalah pemilik produk; AI membantu mengurus detail teknis.

## Tiga langkah
1. Buat repo proyek dari template (atau salin ZIP ke repo baru jika tombol template belum aktif). Jangan gunakan repo master sebagai proyek. Hubungkan AI ke repo atau unggah snapshot dokumen.
2. Salin prompt di bawah. Ceritakan ide dengan bahasa biasa.
3. Jawab pertanyaan, lihat hasil, dan setujui setiap tahap. AI menyimpan dokumentasi jika memiliki akses; jika tidak, AI memberikan file/patch untuk disimpan manual.

## Prompt pertama
"Saya pemula dan ingin membuat website/aplikasi. Repository: [URL]. Baca AGENTS.md dan START_HERE.md. Gunakan Beginner Mode. Interview saya satu pertanyaan penting setiap kali, jelaskan istilah dengan sederhana, rekomendasikan pilihan beserta alasan dan biaya/risiko bila relevan. Isi dokumentasi untuk saya. Jangan coding sebelum gate disetujui. Verifikasi akses dan simpan hasil jika diizinkan."

## Yang perlu kamu putuskan
Tujuan produk, siapa pengguna, fitur penting, tampilan yang disukai, anggaran, serta persetujuan tahap. AI boleh merekomendasikan keputusan teknis tetapi tidak menganggap persetujuan otomatis.

## Perintah sehari-hari
- "Mulai project saya."
- "Lanjutkan pekerjaan berikutnya."
- "Tunjukkan hasil yang perlu saya review."
- "Saya ingin revisi bagian ini."
- "Siapkan handoff ke AI lain."
- "Apakah sudah aman untuk rilis?"

Perintah ini adalah prompt percakapan, bukan command otomatis. AI membaca status aktual dan meminta persetujuan jika perlu.

## Jika ingin pindah AI
Katakan "Siapkan handoff". Pastikan perubahan tersimpan, lalu kirim prompt resume dan URL/branch ke AI baru. Lihat [tutorial](guides/HANDOFF_GUIDE.md).

## Jika bingung
Minta AI menjelaskan satu keputusan dengan contoh, pilihan rekomendasi, biaya/risiko, dan akibat jika ditunda. Jangan kirim password, API key atau data pribadi nyata.

## v3
Tidak perlu menjalankan orchestrator. Gunakan percakapan seperti biasa. AI mengikuti quality/ANTI_AI_SLOP.md; minta audit kualitas sebelum menyetujui hasil. Mode otomatis lokal opsional untuk pengguna teknis.

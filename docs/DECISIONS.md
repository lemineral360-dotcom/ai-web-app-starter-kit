# Decision Log

Keputusan baru dicatat sebagai entri tambahan, bukan menghapus riwayat. Status approval untuk setiap **proyek turunan** dimulai PENDING.

## ADR-001 — Alur dan prinsip master template

- **Tanggal:** 20 November 2026
- **Status:** APPROVED — sebagai aturan master template
- **Keputusan:** Design-first; Planning Gate → Design System → Prototype → Design Gate → Architecture Gate → Development → Testing/Release.
- **Konteks:** Mendukung pengembangan banyak jenis website serta kelanjutan pekerjaan lintas ChatGPT, Claude, Gemini.
- **Aturan:** AI tidak menulis kode aplikasi sebelum Design Gate/Architecture Gate disetujui; perubahan lingkup, desain final, dan arsitektur menggunakan Change Request.
- **Desain:** Figma atau FigCraft fleksibel, satu versi desain final per proyek.
- **Teknologi:** Stack dipilih per proyek; tidak dipaksakan pada template.
- **Persetujuan:** Pemilik menerima dokumen fondasi master template untuk digunakan kembali.

## ADR-002 — Master Template v1.0: Ready to Use

- **Tanggal:** 20 November 2026
- **Status:** APPROVED — master template
- **Keputusan:** Tetapkan versi awal master template sebagai READY TO USE untuk membuat repository proyek baru.
- **Alasan:** Dokumen utama tersedia, repository berstatus GitHub Template, dan pemeriksaan dokumentasi telah berhasil.
- **Batasan:** Tidak berarti aplikasi sudah dibuat, di-deploy, atau gate proyek turunan sudah approved. CI masih terbatas pada pengecekan berkas dan JSON.

## Template keputusan baru
- ID:
- Tanggal:
- Topik:
- Status: PROPOSED / APPROVED / REJECTED / SUPERSEDED
- Konteks dan opsi:
- Keputusan dan alasan:
- Dampak:
- Persetujuan pemilik:
- Referensi:
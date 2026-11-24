# Tutorial engineering sampai production

1. Setelah Design Gate, AI mengusulkan stack sesuai kebutuhan, anggaran, hosting dan kemampuan maintenance. Isi arsitektur dan engineering yang relevan. Owner menyetujui Architecture Gate.
2. Pecah fitur menjadi task kecil dengan acceptance criteria. Implementasikan satu task, jalankan checks, catat hasil, review dan handoff.
3. QA memeriksa fungsi, visual parity, aksesibilitas, keamanan, performance dan recovery. Gunakan staging jika tersedia.
4. Review release checklist; owner menyetujui Release Gate dan tindakan production secara eksplisit. Deploy hanya jika tool/akses tersedia.
5. Verifikasi smoke test, monitoring dan rollback. Catat status aktual dan maintenance.

Prompt: "Lanjutkan engineering sesuai AGENTS.md, docs/ARCHITECTURE.md, design/DESIGN_HANDOFF.md dan engineering/README.md. Verifikasi gate, pilih task, implementasikan dan uji. Jelaskan hasil dengan bahasa sederhana. Jangan deploy tanpa izin."

Jika tool tidak tersedia, berikan instruksi atau patch dan tandai NOT RUN/BLOCKED. Tidak ada CI/CD universal karena stack belum dipilih.

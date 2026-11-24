# Parallel development (opsional)

Mulai hanya setelah gate yang relevan disetujui. Owner/orchestrator menentukan task ID, dependency, file scope, branch dan reviewer. Gunakan issue atau daftar task sebagai catatan kepemilikan terpusat; Markdown bukan mutex atomik.

1. Owner menetapkan task dan baseline SHA; catat di TASKS atau issue.
2. Setiap agen memakai branch/worktree terpisah, misalnya agent/T-001-ui.
3. Hindari perubahan file/schema/API bersama tanpa koordinasi. Jika overlap, serialkan pekerjaan.
4. Agen membuka PR berisi scope, tests, evidence, handoff per sesi.
5. Reviewer independen memeriksa acceptance criteria, security, design parity, regresi.
6. Owner menggabungkan PR berurutan sesuai dependency. Setelah merge, agen lain refresh baseline dan selesaikan konflik tanpa force push.
7. Integrator memperbarui TASKS/HANDOFF/DECISIONS di main. Jangan semua agen menulis tracker pusat secara bersamaan.

Task claim adalah koordinasi manusia, bukan jaminan lock. Jika claim ganda, hentikan pekerjaan yang bertabrakan. Jangan merge saat tes wajib gagal atau blocker belum diselesaikan.

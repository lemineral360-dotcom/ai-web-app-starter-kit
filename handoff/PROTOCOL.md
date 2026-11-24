# Protokol handoff v2

## Before
Verifikasi URL, branch, HEAD, status worktree, gate, role, task ID, acceptance criteria dan dependency. Jangan menghapus perubahan lokal milik orang lain. Jika akses terbatas, laporkan.

## During
Kerjakan scope yang disepakati; catat keputusan dan evidence. Jangan menebak approval, menjalankan deployment tanpa izin, atau commit secrets.

## After
Isi SESSION-TEMPLATE.md dalam catatan sesi (misalnya handoff/sessions/T-001-20261124.md). Sertakan baseline SHA dan commit pekerjaan bila sudah tersedia; tidak perlu mencatat SHA commit yang memuat catatan itu sendiri. Catat PR atau branch dan perubahan yang belum commit secara jelas. Perbarui tracker pusat melalui integrator bila parallel.

## Resume
Agen penerus memverifikasi branch/commit aktual, membaca handoff, memeriksa perubahan setelah baseline, dan menegaskan scope. Status tes: PASS/FAIL/NOT RUN/BLOCKED. Status gate: PENDING/APPROVED; hanya manusia berwenang menyetujui.

Tidak ada komunikasi otomatis antar platform. GitHub dan pengguna merupakan mekanisme transfer.

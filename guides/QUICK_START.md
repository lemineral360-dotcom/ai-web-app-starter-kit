# Mulai dalam 5 langkah

1. Di GitHub Settings > General, aktifkan Template repository bila belum aktif. Klik Use this template, buat repo proyek baru (private dianjurkan). Jangan mengerjakan produk di master kit.
2. Sambungkan repo ke AI pilihan, atau clone/download ZIP dan berikan file yang diperlukan. Pastikan AI punya akses; akses baca tidak berarti bisa push.
3. Salin prompt berikut ke AI pertama: "Baca AGENTS.md dan guides/QUICK_START.md pada [URL REPO]. Ini proyek baru. Mulai discovery, interview saya, isi intake dan PRD. Semua gate PENDING. Jangan coding."
4. Jawab pertanyaan AI dan setujui hasil setiap gate secara eksplisit. Gunakan docs/TASKS.md sebagai daftar pekerjaan.
5. Saat hendak berpindah AI, gunakan [tutorial handoff](HANDOFF_GUIDE.md). Tidak perlu menyalin seluruh chat.

## Jika memakai ChatGPT
Buat Project, salin templates/CHATGPT_PROJECT_INSTRUCTIONS.md ke Project Instructions; hubungkan GitHub jika tersedia atau unggah dokumen. Lihat [panduan lengkap](CHATGPT_PROJECT_SETUP.md).

## Jika hanya punya akses chat
Berikan AGENTS.md, PRD, TASKS, HANDOFF, DECISIONS serta file relevan, termasuk branch/commit. Minta AI menghasilkan patch atau dokumen utuh; simpan manual dan commit. Jangan menandai sudah push sebelum benar-benar tersimpan.

## Langkah berikutnya
Discovery → Planning Gate → UX/design → Design Gate → Architecture Gate → coding → QA → Release Gate. Semua approval milik manusia.

# Tutorial handoff antar AI

## Cara termudah: satu task, satu agen
Contoh: ChatGPT menyusun PRD; Claude menyusun desain; Gemini meninjau; Codex mengimplementasikan. Peran dapat ditukar. Tidak memerlukan API berbayar/orchestrator khusus, tetapi akses GitHub tiap alat berbeda.

### 1. Akhiri sesi agen lama
Kirim: "Selesaikan handoff sesuai handoff/PROTOCOL.md. Update TASKS, HANDOFF dan DECISIONS jika perlu; catat tes, blocker, branch, commit pekerjaan, dan satu next action. Commit jika punya izin, jika tidak berikan patch."
Periksa bahwa perubahan benar-benar tersimpan. Bila belum merge, berikan branch/PR kepada agen berikutnya, bukan hanya main.

### 2. Mulai sesi agen baru
Kirim: "Lanjutkan [URL REPO], branch [BRANCH], commit [SHA atau HEAD yang diverifikasi]. Baca AGENTS.md, handoff/CONTEXT.md dan docs/HANDOFF.md. Verifikasi gate, task dan hasil agen sebelumnya. Ringkas pemahaman dan lanjutkan task yang ditugaskan. Jangan mengulang pekerjaan atau melewati gate."
Jika AI hanya mampu membaca file upload, berikan snapshot terbaru dan patch yang belum merge; jangan pakai snapshot lama.

### 3. Verifikasi
Pastikan agen baru menyebut task, branch, baseline commit, status gate, blocker dan next action yang sesuai. Jika berbeda, hentikan perubahan dan sinkronkan dokumen.

## Pindah platform
| Platform | Cara mulai |
|---|---|
| ChatGPT | Project Instructions + GitHub connector jika ada; prompt resume |
| Claude chat | Berikan repo/file dan prompt resume; akses bergantung konektor |
| Claude Code | Buka clone repo; CLAUDE.md mengarahkan ke AGENTS.md |
| Gemini chat | Berikan file/repo dan prompt resume |
| Gemini CLI | Buka clone repo; GEMINI.md menunjuk aturan bersama |
| Codex | Pilih repo/worktree; baca AGENTS.md |
| Cursor | Buka repo; aturan .cursor/rules/project.mdc |
| GitHub Copilot | Buka repo; .github/copilot-instructions.md |
| AI lainnya | Salin AGENTS.md dan prompt resume |

## Jika beberapa agen bekerja bersamaan
Gunakan [parallel workflow](PARALLEL_WORKFLOW.md). Untuk pemula, tetap gunakan mode serial.

## Troubleshooting
- Akses gagal: minta pengguna menghubungkan akun/clone/unggah snapshot; jangan menebak isi.
- Branch berbeda: cocokkan PR dan commit; jangan reset paksa.
- Handoff lama: baca git log/diff dan TASKS; laporkan selisih.
- Gate belum disetujui: lakukan dokumentasi yang diizinkan, bukan coding.
- Agen tidak bisa commit: gunakan patch manual, pengguna memverifikasi.
- Konflik: hentikan merge, koordinasikan owner, jangan menimpa pekerjaan agen lain.

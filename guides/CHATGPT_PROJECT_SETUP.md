# Panduan ChatGPT Project — dari ide ke production

Panduan ini melengkapi, bukan mengganti, workflow persetujuan di [AGENTS.md](../AGENTS.md).

## 1. Gunakan master template
1. Buka repository ini di GitHub.
2. Pilih **Use this template → Create a new repository**.
3. Beri nama project, pilih private bila memuat strategi bisnis internal.
4. Baca `README.md`, `AGENTS.md`, dan `docs/WORKFLOW.md`.
5. Semua approval gate di project baru dimulai **PENDING**, meskipun master template READY TO USE.
6. Isi `templates/project-intake.md`, `docs/PRD.md` dan planning documents sebelum meminta implementasi.

## 2. Buat ChatGPT Project
1. Di ChatGPT, pilih **New project** dan beri nama sesuai produk.
2. Buka Project instructions, salin teks di [templates/CHATGPT_PROJECT_INSTRUCTIONS.md](../templates/CHATGPT_PROJECT_INSTRUCTIONS.md).
3. Tambahkan file Markdown inti ke Project sebagai context; prioritaskan `AGENTS.md`, `docs/CONSTITUTION.md`, `docs/PRD.md`, `docs/TASKS.md`, `docs/HANDOFF.md`, `design/DESIGN_SYSTEM.md` dan `design/DESIGN_APPROVAL.md`.
4. Jika GitHub connector dapat membaca repository, gunakan repository sebagai sumber aktual. **Perubahan percakapan/berkas yang diunggah tidak otomatis tersinkron ke GitHub.** Verifikasi commit/push setelah pengubahan.
5. Jangan unggah secrets, personal data, token API, atau .env.

## 3. Mulai discovery
Salin prompt [DISCOVERY_PROMPT.md](../templates/DISCOVERY_PROMPT.md) ke chat '00 — Product Discovery'. Lengkapi intake, PRD, fitur, role, dan kebutuhan non-fungsional. Bedakan keputusan dari asumsi. Minta owner menyetujui Planning Gate.

## 4. Bagi percakapan menurut pekerjaan
- 00 — Project Master / Decisions
- 01 — Discovery & PRD
- 02 — Features & Business Logic
- 03 — UX Flow & Sitemap
- 04 — Design System
- 05 — UI Screens & Prototype
- 06 — Architecture / Database / API
- 07 — Frontend
- 08 — Backend
- 09 — QA / Security
- 10 — Deployment / Maintenance

Setiap chat harus merujuk ke file otoritatif dan meninggalkan ringkasan keputusan di `docs/HANDOFF.md`; chat history bukan satu-satunya basis kebenaran.

## 5. Urutan gerbang kualitas
**Planning Gate → Design Gate → Architecture Gate → Development → Testing/Release Gate**.
- Planning: scope, user role, acceptance criteria, prioritas MVP.
- Design: token, komponen, layar, state, responsive, flow dan versi prototype yang disetujui.
- Architecture: stack, data model, API, security dan deployment.
- Testing/Release: fungsi, integrasi, accessibility, performance, security, rollback.

Owner memberikan persetujuan eksplisit; AI tidak boleh menandai dirinya sendiri APPROVED.

## 6. Update setelah tiap sesi
1. Tulis apa yang dikerjakan dan keputusan baru.
2. Catat status tugas di `docs/TASKS.md`, catatan lintas AI di `docs/HANDOFF.md`.
3. Catat keputusan di `docs/DECISIONS.md`, perubahan scope pada `docs/CHANGE_REQUEST.md`.
4. Catat ringkasan pekerjaan di [templates/PROGRESS.md](../templates/PROGRESS.md) dan [templates/CHANGELOG.md](../templates/CHANGELOG.md), jika diadopsi oleh project.
5. Buat PR untuk perubahan penting, review dan merge setelah disetujui.

## 7. Tool pilihan
ChatGPT Project = konteks dan keputusan; Figma/FigCraft = desain; GitHub = version control; Codex/IDE = implementasi; CI = otomatisasi tes. Framework, database, dan hosting **tidak diwajibkan** oleh template.

## 8. Checklist rilis
- [ ] Planning/Design/Architecture Gates disetujui dan tercatat
- [ ] Fitur prioritas punya acceptance criteria terverifikasi
- [ ] Mobile/tablet/desktop dan states diperiksa
- [ ] Authentication, authorization, validation dan data protection diperiksa
- [ ] Unit/integration/E2E sesuai risiko dijalankan
- [ ] Secret management, backup, monitoring, migration, rollback jelas
- [ ] Owner menyetujui release

> GitHub Actions pemeriksaan dokumentasi tidak sama dengan sertifikat kesiapan production.

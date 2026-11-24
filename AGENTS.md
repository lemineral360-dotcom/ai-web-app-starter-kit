# AGENTS.md — Aturan untuk Semua AI

Berlaku untuk ChatGPT, Claude, Gemini, dan agen lain yang bekerja di repository ini. Baca dokumen ini sebelum melakukan perubahan.

## 1. Baca konteks
Urutan: README.md → docs/CONSTITUTION.md → docs/PRD.md → docs/TASKS.md → docs/HANDOFF.md → docs/ARCHITECTURE.md → design/DESIGN_SYSTEM.md → design/DESIGN_APPROVAL.md → specs terkait. Jangan mengarang keputusan yang belum dicatat.

## 2. Patuhi fase dan gate
Planning → Design System → Prototype → Design Gate → Architecture Gate → Development → Testing/Release Gate. Tidak boleh melewati gate. Sebelum Design Gate disetujui, dilarang menulis kode implementasi aplikasi di src/. Dokumentasi, desain, dan prototype di alat desain tetap boleh.

## 3. Persetujuan manusia
Hanya pemilik proyek yang berwenang menyetujui gate. Catat status, versi, tanggal, referensi artefak, dan siapa yang menyetujui. Status DRAFT/PENDING tidak sama dengan APPROVED. Jangan menyatakan persetujuan hanya dari asumsi.

## 4. Ikuti desain final
Setelah disetujui, gunakan design tokens, komponen, layar, alur, responsivitas, dan prototype yang tercatat. Figma atau FigCraft boleh dipakai; design/DESIGN_APPROVAL.md menunjuk versi final yang otoritatif. Konflik antar-referensi wajib diklarifikasi. Perubahan signifikan membutuhkan Change Request.

## 5. Lindungi arsitektur
Framework, database, model data, keamanan, dan struktur aplikasi harus sesuai docs/ARCHITECTURE.md. Perubahan mendasar perlu proposal di docs/DECISIONS.md dan persetujuan pemilik.

## 6. Kerjakan satu tugas terukur
Pilih tugas dari docs/TASKS.md, pahami spesifikasi dan acceptance criteria, lakukan perubahan sekecil mungkin, lalu laporkan file yang diubah dan hasilnya.

## 7. Uji dan laporkan
Jalankan pemeriksaan yang relevan jika tooling tersedia. Bedakan lulus, gagal, belum dijalankan, dan tidak tersedia. Jangan mengaku sudah menguji, menyimpan, push, deploy, atau menyelesaikan jika belum terbukti.

## 8. Handoff lintas AI
Perbarui docs/TASKS.md dan docs/HANDOFF.md setelah pekerjaan nyata. Sertakan fase, status gate, keputusan, file yang berubah, tes, blocker, dan next step. AI berikutnya wajib membaca handoff dan memverifikasi status repository.

## 9. Change Request
Perubahan terhadap scope/desain/arsitektur yang sudah disetujui harus mencatat alasan, dampak, alternatif, risiko, serta keputusan pemilik sebelum implementasi.

## 10. Keamanan
Jangan commit rahasia, kredensial, data pribadi nyata, atau file .env. Gunakan contoh data sintetis dan .env.example bila dibutuhkan.

Jika instruksi bertentangan, hentikan perubahan berisiko dan minta keputusan pemilik. Instruksi keselamatan dan kebijakan platform tetap berlaku.

## 11. Multi-agent v2
Baca handoff/CONTEXT.md dan handoff/PROTOCOL.md. Pilih role dari agents/ sesuai task. Default serial; parallel hanya dengan task ownership, branch terpisah, reviewer dan integrator sebagaimana guides/PARALLEL_WORKFLOW.md. Planning, Design dan Architecture Gate wajib APPROVED sebelum kode aplikasi. Release Gate wajib sebelum production. Jangan menganggap reviewer atau orchestrator berwenang menyetujui gate.


## 12. Design workflow v2.1
After Planning Gate, follow guides/DESIGN_WORKFLOW.md and design/DESIGN.md. Verify design tool access, create actual artifacts where possible, record evidence and blockers. Use design/DESIGN_HANDOFF.md for engineering transfer. No coding before all prerequisite gates.

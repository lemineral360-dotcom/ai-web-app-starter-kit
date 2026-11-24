# Tutorial desain dari nol — v2.1
1. Setelah Planning Gate, pilih tool (Figma, FigCraft, Penpot atau lainnya). Verifikasi akses dokumen aktif dan kemampuan membuat komponen/prototype. Jangan membuat file baru jika owner meminta edit dokumen aktif.
2. Minta AI mengisi design/DESIGN.md, persona, sitemap dan flows. Review arah visual.
3. Buat foundations dan token layers; pilih komponen relevan dan buat reusable variants dengan dummy preview. Review design system.
4. Buat wireframe, lalu high-fidelity screens dengan states dan responsive layout. Catat link dan versi.
5. Hubungkan prototype, uji critical journeys dan aksesibilitas; catat hasil nyata dan keterbatasan.
6. Isi DESIGN_HANDOFF dan DESIGN_APPROVAL. Owner menyetujui versi spesifik; lanjut Architecture Gate sebelum coding.
## Prompt siap salin
"Bertindak sebagai UI/UX Designer dan Design System Architect. Baca AGENTS.md, PRD, TASKS, HANDOFF dan design/DESIGN.md. Ikuti guides/DESIGN_WORKFLOW.md. Verifikasi tool/skill yang tersedia (Frontend Design dan Impeccable opsional). Mulai tahap desain yang belum selesai; gunakan dokumen aktif jika diminta. Buat artefak aktual, bukan hanya daftar komponen; gunakan dummy content realistis. Laporkan link, versi, evidence, blocker dan minta review owner. Jangan coding sebelum gates."
## Jika tool tidak tersedia
Buat spesifikasi, wireframe tekstual atau storyboard; tandai artefak visual/interaktif BLOCKED. Minta akses atau pengguna membuat artefak manual. Jangan mengklaim sudah menyimpan atau menguji desain.
## Handoff ke developer
Gunakan design/DESIGN_HANDOFF.md dan handoff/PROTOCOL.md. Sertakan versi, token, komponen, screen IDs, states, assets, acceptance criteria dan gate evidence. Storybook dan Playwright opsional setelah gate coding.

# Documentation Playbook

## Sumber kebenaran dan mapping
Dokumen yang sudah ada pada starter kit **tetap otoritatif**; file baru di `templates/` adalah contoh untuk dipakai pada repository hasil template.

| Topic | Existing authoritative file | Optional new project file |
|---|---|---|
| Project overview | docs/PRD.md + project-intake | PROJECT.md |
| Requirements | docs/PRD.md | FEATURES.md |
| UX | design/user-flows.md, design/screens.md | UX-FLOW.md |
| Visual design | design/DESIGN_SYSTEM.md, design/tokens.json | DESIGN.md bila diperlukan |
| Architecture | docs/ARCHITECTURE.md | TECH-STACK.md, DATABASE.md, API.md |
| Governance | docs/CONSTITUTION.md, AGENTS.md | RULES.md bila diperlukan |
| Security | docs/ARCHITECTURE.md | SECURITY.md |
| QA | specs/acceptance-criteria.md | TESTING.md |
| Delivery | docs/TASKS.md, docs/HANDOFF.md | ROADMAP.md, PROGRESS.md, CHANGELOG.md |
| Inspiration | design/sources.md | REFERENCES.md |

Jangan membuat duplikat yang saling bertentangan: tentukan satu canonical file dan tautkan file tambahan kepadanya.

## Cara mengisi satu dokumen
1. Isi identitas, status (DRAFT/REVIEW/APPROVED), owner dan versi.
2. Nyatakan keputusan yang sudah confirmed, labeli open questions.
3. Berikan contoh konkret + tabel acceptance criteria bila relevan.
4. Tambahkan tautan dependency lintas-file agar traceable.
5. Review dengan pemilik, lalu catat keputusan di docs/DECISIONS.md.
6. Update tugas/handoff; commit perubahan lewat branch dan PR.

## Minimum viable documentation
Untuk ide baru, cukup intake + PRD + feature spec + UX flow + design approval + architecture + acceptance criteria + handoff. File lain ditambahkan saat kebutuhan nyata muncul.

## Contoh perubahan
Permintaan: 'Pelanggan dapat impor daftar tamu dari Excel.'
- PRD: tambah use case dan constraints.
- FEATURES/specs: format file, limits, role, errors, acceptance criteria.
- UX: upload → preview → validation → confirm → result.
- DATABASE/API: struktur dan batch import yang aman.
- TESTING: duplicate/invalid/malicious/large files.
- TASKS/HANDOFF: status, referensi, blocker dan hasil tes.

## Definition of Done dokumentasi
- Istilah konsisten dan tidak bertentangan.
- Traceable dari problem → feature → flow → architecture → tests.
- Tidak ada keputusan critical tanpa owner approval.
- Tidak ada secrets atau data pribadi nyata.
- Progress dan status tes benar-benar didukung bukti.

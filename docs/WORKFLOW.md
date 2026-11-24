# Workflow dan Gates

1. Planning Gate: PRD, pengguna, scope, prioritas, acceptance criteria disetujui.
2. Design System: tokens, komponen, aksesibilitas, responsivitas.
3. Prototype dan Design Gate: layar utama, states, prototype interaktif, responsif; pemilik menyetujui versi final di design/DESIGN_APPROVAL.md.
4. Architecture Gate: stack, database, API, keamanan, deployment dan keputusan disetujui.
5. Development: implementasi per feature spec setelah semua gate sebelumnya approved.
6. Release Gate: review fungsi, visual parity, testing, keamanan, dokumentasi, rollback dan persetujuan pemilik.

Semua gate default PENDING. Perubahan pasca-persetujuan melalui docs/CHANGE_REQUEST.md.

Design detail: UX architecture → direction → foundations → components → wireframes → high fidelity → interactive prototype → usability review → Design Gate → developer handoff. See guides/DESIGN_WORKFLOW.md. Iterate as needed; no app code until Architecture Gate.

Engineering detail: architecture approval → task implementation → review → QA/staging → owner release approval → authorized deployment → smoke test/monitoring → maintenance. See guides/ENGINEERING_WORKFLOW.md. Use Beginner Mode for plain-language progress.

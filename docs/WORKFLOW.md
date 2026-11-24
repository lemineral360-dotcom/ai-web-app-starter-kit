# Workflow dan Gates

1. Planning Gate: PRD, pengguna, scope, prioritas, acceptance criteria disetujui.
2. Design System: tokens, komponen, aksesibilitas, responsivitas.
3. Prototype dan Design Gate: layar utama, states, prototype interaktif, responsif; pemilik menyetujui versi final di design/DESIGN_APPROVAL.md.
4. Architecture Gate: stack, database, API, keamanan, deployment dan keputusan disetujui.
5. Development: implementasi per feature spec setelah semua gate sebelumnya approved.
6. Release Gate: review fungsi, visual parity, testing, keamanan, dokumentasi, rollback dan persetujuan pemilik.

Semua gate default PENDING. Perubahan pasca-persetujuan melalui docs/CHANGE_REQUEST.md.

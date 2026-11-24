# AI Web & App Starter Kit v2.0 — Multi-Agent Development Kit

Template documentation-first berbahasa Indonesia untuk web, SaaS, mobile app, dan internal tools. Framework agnostic; bukan aplikasi siap deploy atau orchestrator otomatis.

## Mulai di sini
- **[Quick Start: 5 langkah](guides/QUICK_START.md)** — untuk pengguna baru.
- **[Cara pindah AI / handoff](guides/HANDOFF_GUIDE.md)** — cukup dua prompt.
- [ChatGPT Project Setup](guides/CHATGPT_PROJECT_SETUP.md)
- [Project Instructions](templates/CHATGPT_PROJECT_INSTRUCTIONS.md)
- [Discovery Prompt](templates/DISCOVERY_PROMPT.md)
- [Prompt library](prompts/README.md)

## Workflow
Discovery → Planning Gate → Design → Design Gate → Architecture Gate → Development → QA → Release Gate.
Semua gate proyek baru PENDING dan disetujui manusia. Default satu AI per task; [parallel workflow](guides/PARALLEL_WORKFLOW.md) opsional.

## Referensi
- [AGENTS.md](AGENTS.md): aturan bersama
- [Agent roles](agents/README.md)
- [Handoff protocol](handoff/PROTOCOL.md)
- [Context index](handoff/CONTEXT.md)
- [Documentation playbook](guides/DOCUMENTATION_PLAYBOOK.md)
- [Indeks dokumen](guides/README.md)
- [Contoh project](examples/README.md)
- [Release checklist](docs/RELEASE_CHECKLIST.md)

## Batasan
Setiap platform perlu akses repo sendiri. File instruksi tidak otomatis menjalankan agen atau menyinkron chat. Jangan commit rahasia. Aktifkan Template repository di Settings bila belum aktif. Pengujian integrasi lintas runtime belum dilakukan.

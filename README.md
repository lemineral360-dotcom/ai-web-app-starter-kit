# AI Web & App Starter Kit v3.0 — Intelligent Multi-Agent Development System (initial)

Template documentation-first berbahasa Indonesia untuk web, SaaS, mobile app, dan internal tools. Framework agnostic; bukan aplikasi siap deploy atau orchestrator otomatis.

## Mulai di sini
- [Panduan v3](guides/V3_USAGE.md)
- [Anti AI Slop dan quality control](quality/README.md)
- [Optional local dispatcher](orchestrator/README.md)
- **[START HERE — untuk pemula](START_HERE.md)**
- [Beginner Mode](guides/BEGINNER_MODE.md)
- [Engineering sampai production](guides/ENGINEERING_WORKFLOW.md)
- [Troubleshooting](guides/TROUBLESHOOTING.md)
- **[Quick Start: 5 langkah](guides/QUICK_START.md)** — untuk pengguna baru.
- **[Cara pindah AI / handoff](guides/HANDOFF_GUIDE.md)** — cukup dua prompt.
- [ChatGPT Project Setup](guides/CHATGPT_PROJECT_SETUP.md)
- [Project Instructions](templates/CHATGPT_PROJECT_INSTRUCTIONS.md)
- [Discovery Prompt](templates/DISCOVERY_PROMPT.md)
- [Prompt library](prompts/README.md)

- [Tutorial Design System hingga Prototype](guides/DESIGN_WORKFLOW.md)

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

# Project Constitution v1.0

## Prinsip inti
1. **Design First:** coding aplikasi hanya setelah Design Gate disetujui secara eksplisit.
2. **Consistency:** implementasi mengikuti spesifikasi, design tokens, dan komponen yang disetujui.
3. **Security First:** least privilege, validasi input, pengelolaan rahasia yang aman, dan privasi sejak planning.
4. **Quality First:** setiap fitur memiliki acceptance criteria dan verifikasi yang dapat dilacak.
5. **AI Continuity:** keputusan, tugas, dan handoff terdokumentasi agar model AI lain bisa melanjutkan tanpa menebak.

## Tata kelola
- Pemilik proyek memutuskan persetujuan fase dan perubahan besar.
- Keputusan yang disetujui dicatat di docs/DECISIONS.md.
- Sumber desain final adalah versi yang disebut dalam design/DESIGN_APPROVAL.md; file token dan spesifikasi di GitHub mencerminkan versi tersebut.
- Jika dokumen berbeda, jangan diam-diam memilih: catat konflik dan ajukan klarifikasi.
- Constitution ini adalah prinsip lintas proyek; PRD, arsitektur, dan desain ditentukan ulang untuk setiap proyek hasil template.
- Template bukan bukti bahwa suatu proyek telah mendapat persetujuan. Semua gate dimulai PENDING.
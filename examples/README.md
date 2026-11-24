# Contoh fiktif: TaskDesk

Produk web untuk tim kecil mengelola tugas. Bukan keputusan untuk proyek baru.

- Problem: tugas tercecer di chat.
- Roles: admin tim dan anggota.
- MVP: login, daftar tugas, assignment, status.
- Non-goals: billing, integrasi eksternal.
- Metric: 90% tugas memiliki assignee dan status.
- Feature F-001: anggota membuat tugas dengan judul wajib.
- Flow: dashboard → tambah tugas → validasi → simpan → daftar.
- Acceptance: Given anggota terautentikasi, when judul valid disimpan, then tugas tampil dalam timnya; pengguna tim lain tidak dapat membaca tugas.
- Design: token dan komponen form ditentukan pada Design Gate.
- Architecture: stack belum dipilih; tenant isolation wajib diuji.
- Semua gate PENDING.

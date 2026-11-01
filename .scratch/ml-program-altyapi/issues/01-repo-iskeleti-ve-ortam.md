# 01: Repo iskeleti ve ortam

Spec: [../spec.md](../spec.md) (user stories 1–8, Modül 1)

**What to build:** Öğrenen ayrı bir `ml-program` git reposunu açtığında, tek `uv sync` ile JAX, PyTorch, NumPy ve pytest içeren CPU ortamını alır. İçerik klasörleri (banka, dersler, plan, odevler, sinavlar, videolar), `kayit/` ve `calisma/` ilk günden yerinde durur. Kökteki CLAUDE.md Hoca'nın kişiliğini, dil kurallarını (İngilizce soru ve terimler, Türkçe açıklama, LaTeX yok) ve dosya haritasını verir. Yerleşim [11 numaralı bilet](../../ml-mulakat-programi/issues/11-proje-repo-yapisi.md) kararına birebir uyar.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Planlama reposundan ayrı yeni bir git reposu var (`~/Claude/ml-program/`)
- [ ] `uv sync`, varsayılan CPU ortamını kurar; `uv run pytest` boş da olsa çalışır
- [ ] Opsiyonel `video` grubu sabitlenmiş Manim Community sürümünü, `gpu` grubu tek 3090 için CUDA JAX ve PyTorch'u kurar
- [ ] Boş iskelet klasörleri var: banka, dersler, plan, odevler, sinavlar, videolar, calisma, kayit
- [ ] Render çıktıları gitignore'da; Manim kaynakları ve seslendirme metni commit'lenebilir; Git LFS yok
- [ ] Kökteki CLAUDE.md kişiliği, dil kurallarını ve dosya haritasını (içerik / kayıt / çalışma alanı ayrımı dahil) içerir
- [ ] Uzak repo kurulmaz, push yapılmaz

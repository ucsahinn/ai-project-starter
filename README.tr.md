# Context Engineering Project Starter

<p align="center">
  <a href="README.de.md">🇩🇪</a> ·
  <a href="README.es.md">🇪🇸</a> ·
  <a href="README.md">🇬🇧</a> ·
  <a href="README.pt-BR.md">🇧🇷</a> ·
  <a href="README.tr.md">🇹🇷</a> ·
  <a href="README.fr.md">🇫🇷</a>
</p>

> Kod yazmaya baslamadan once AI-agent uyumlu proje context'i, baslangic dokumantasyonu, domain guardrail'leri ve agent instruction dosyalari ureten Codex skill paketi.

[![License: MIT](https://img.shields.io/badge/license-MIT-111827)](LICENSE)
[![Security Policy](https://img.shields.io/badge/security-policy-b91c1c)](SECURITY.md)
[![Docs](https://img.shields.io/badge/docs-ready-2563eb)](docs/USAGE.md)
[![Public Safe](https://img.shields.io/badge/public--safe-checklist-7c3aed)](docs/PUBLIC_REPO_CHECKLIST.md)

- **Durum:** ilk public-ready skill paketi
- **Lisans:** MIT
- **Proje tipi:** context engineering ve proje baslangic dokumantasyonu icin Markdown tabanli Codex skill paketi
- **Not:** Bagimsiz topluluk projesidir. OpenAI ile bagli, onayli veya sponsorlu degildir.

Bu skill, ham proje fikrini Codex/Cursor/Claude Code/Windsurf/Continue/Copilot/Aider gibi agent'larin anlayacagi eksiksiz proje context'ine donusturur. Amac, agent'in baglamsiz kod yazmaya baslamasini engellemek ve urun hedefi, teknik sinirlar, guvenlik, test, kalite ve mimari kararlarin bastan net olmasini saglamaktir.

## 🧭 Enterprise Degerlendirme Yolu

| Kanitlamak istedigin sey | Baslangic | Alacagin kanit |
| --- | --- | --- |
| Starter'in mevcut isi ezmeden ilerledigini | [Install guide](docs/INSTALL.md) ve [Usage guide](docs/USAGE.md) | Modlar, kopyalama yolu ve guvenli dosya uretme beklentileri. |
| Uretilen context'in guvenlik ve kalite kapilari oldugunu | [Security model](docs/SECURITY_MODEL.md) | Secret handling, onay sinirlari, test beklentileri ve public-safe kurallar. |
| Skill'in enterprise starter icin yeterli oldugunu | [Examples](docs/EXAMPLES.md) | SaaS, cybersecurity, API, web, mobile, desktop, data, internal-tool ve library/CLI desenleri. |
| Public reponun paylasima uygun oldugunu | [Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) | Commit, tag, release veya reuse oncesi sizinti onleme checklist'i. |

## ✅ Guven Sinyalleri

| Sinyal | Standart |
| --- | --- |
| Koddan once context | Skill, implementation baslamadan once urun, mimari, guvenlik, test, operasyon ve task context'i hazirlar. |
| Mod kapili cikti | `PROMPT_ONLY`, `DOCS_ONLY`, `PLAN_ONLY`, `CREATE_FILES`, `AUDIT_CONTEXT` ve `REPAIR_CONTEXT` akisi acik tutar. |
| Public-safe paket | Ornekler ve template'ler placeholder kullanir; credential, private prompt, musteri verisi ve local operator path tasimaz. |
| Agent uyumlulugu | Cikti Codex, Claude Code, Cursor, Continue, Copilot, Devin/Windsurf, Aider ve benzer araclara uyumludur. |

## 🎯 Neden Var?

AI coding agent'lar guclu ama context yoksa proje hizla dagilir. Belirsiz "bunu kodla" istekleri duplicate modul, zayif guvenlik, belirsiz mimari ve scope creep uretir.

Bu repo su ihtiyaclari paketler:

- proje brief'i ve PRD,
- teknik spec ve architecture docs,
- implementation plan ve task listesi,
- security, testing ve quality gates,
- SaaS, cybersecurity, AI product, API, web, mobile, desktop, data product, internal tool ve library/CLI domain pack'leri,
- `AGENTS.md`, `CLAUDE.md`, Cursor, Continue, Copilot, Devin/Windsurf, Aider ve Codex context dosyalari.

## ⚡ Hizli Basla

| Sunu istiyorum... | Kullan |
| --- | --- |
| Yeni AI-coded projeyi guvenli baslatmak | [Skill entrypoint](.agents/skills/context-engineering-project-starter/SKILL.md) |
| Modlari ve ornekleri gormek | [Usage guide](docs/USAGE.md) |
| Skill'i kurmak/kopyalamak | [Install guide](docs/INSTALL.md) |
| Skill yapisini incelemek | [Skill structure](docs/SKILL_STRUCTURE.md) |
| Public repo guvenligini kontrol etmek | [Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) |
| Guvenlik modelini okumak | [Security model](docs/SECURITY_MODEL.md) |

## 🧩 Ne Sunar?

| Yetenek | Deger |
| --- | --- |
| Proje context temeli | `README.md`, `PROJECT_BRIEF.md`, `PRODUCT_REQUIREMENTS.md`, `TECHNICAL_SPEC.md`, `ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, `TASKS.md` |
| Agent instruction dosyalari | `AGENTS.md`, `CLAUDE.md`, Cursor, Continue, Copilot, Devin/Windsurf, Aider ve Codex context dosyalari |
| Enterprise starter | security, testing, observability, deployment, operations, risk register, ADR |
| Domain pack'ler | SaaS, cybersecurity, AI product, API, web, mobile, desktop, data, internal tool, library/CLI |
| Vibe coding guardrail | anti-slop, non-goals, milestone control, duplicate engelleme, verification-before-done |
| Context audit/repair | zayif, eski, duplicate, celiskili veya eksik context dokumanlarini bulma ve duzeltme |
| Template materializer | `scripts/create_starter.py` ile guvenli starter doc seti olusturma |

## 🚀 Ornek Kullanim

```text
context-engineering-project-starter skillini CREATE_FILES + ENTERPRISE_STARTER modunda kullan.
Proje fikri: Tenant bazli takimlar, RBAC, audit log, AI destekli remediation planlama ve guvenli raporlama iceren SaaS siber guvenlik platformu.
```

Sadece vibe coding guardrail:

```text
VIBE_GUARDRAILS modunu kullan. Bu proje vibe coding sirasinda dagilmasin diye gerekli agent context ve quality gate dosyalarini hazirla.
```

## 🧰 Desteklenen Modlar

- `PROMPT_ONLY`
- `DOCS_ONLY`
- `PLAN_ONLY`
- `CREATE_FILES`
- `AUDIT_CONTEXT`
- `REPAIR_CONTEXT`
- `ENTERPRISE_STARTER`
- `VIBE_GUARDRAILS`
- `RESEARCH_BACKED`

## 🛡️ Public Guvenlik Kurallari

Bu repo sunlari icermemelidir:

- API key, token, credential, cookie, private key, certificate veya private URL,
- musteri verisi veya sirket ici bilgi,
- private system prompt,
- proprietary proje detayi,
- maskelenmemis log, screenshot, local path veya kisisel not.

Yayinlamadan once [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) kullanin.

## ⚖️ Lisans

MIT. Detaylar icin [LICENSE](LICENSE).

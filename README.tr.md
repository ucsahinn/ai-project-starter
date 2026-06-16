# AI Project Starter

<p align="center">
  <img src="assets/icon.svg" alt="AI Project Starter ikonu" width="120" />
  <br />
  <img src="assets/banner.svg" alt="Brief, PRD, mimari, ajan kuralları ve kalite kapılarını gösteren AI Project Starter banner görseli" width="100%" />
</p>

<p align="center">
  &#127760; <strong>Dok&#252;man dilleri:</strong>
  <a href="README.de.md"><img src="https://flagcdn.com/w20/de.png" alt="Deutsch" width="20"></a> |
  <a href="README.es.md"><img src="https://flagcdn.com/w20/es.png" alt="Espa&#241;ol" width="20"></a> |
  <a href="README.md"><img src="https://flagcdn.com/w20/gb.png" alt="English" width="20"></a> |
  <a href="README.pt-BR.md"><img src="https://flagcdn.com/w20/br.png" alt="Portugu&#234;s (Brasil)" width="20"></a> |
  <a href="README.tr.md"><img src="https://flagcdn.com/w20/tr.png" alt="T&#252;rk&#231;e" width="20"></a> |
  <a href="README.fr.md"><img src="https://flagcdn.com/w20/fr.png" alt="Fran&#231;ais" width="20"></a>
</p>

> Kod yazmaya başlamadan önce AI-agent uyumlu proje context'i, başlangıç dokümantasyonu, domain guardrail'leri ve agent instruction dosyaları üreten Codex skill paketi.

[![License: MIT](https://img.shields.io/badge/license-MIT-111827)](LICENSE)
[![Security Policy](https://img.shields.io/badge/security-policy-b91c1c)](SECURITY.md)
[![Docs](https://img.shields.io/badge/docs-ready-2563eb)](docs/USAGE.md)
[![Public Safe](https://img.shields.io/badge/public--safe-checklist-7c3aed)](docs/PUBLIC_REPO_CHECKLIST.md)

- **Durum:** ilk public-ready skill paketi
- **Lisans:** MIT
- **Proje tipi:** context engineering ve proje başlangıç dokümantasyonu için Markdown tabanlı Codex skill paketi
- **Not:** Bağımsız topluluk projesidir. OpenAI ile bağlı, onaylı veya sponsorlu değildir.

Bu skill, ham proje fikrini Codex, Cursor, Claude Code, Windsurf, Continue, Copilot, Aider ve benzeri agent'ların anlayacağı eksiksiz proje context'ine dönüştürür. Amaç, agent'ın bağlamsız kod yazmaya başlamasını engellemek ve ürün hedefi, teknik sınırlar, güvenlik, test, kalite ve mimari kararları baştan netleştirmektir.

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f9ed.svg" alt="" aria-hidden="true" width="20"> Enterprise Değerlendirme Yolu

| Kanıtlamak istediğin şey | Başlangıç | Alacağın kanıt |
| --- | --- | --- |
| Starter mevcut işi ezmeden ilerliyor mu? | [Install guide](docs/INSTALL.md) ve [Usage guide](docs/USAGE.md) | Modlar, kopyalama yolu ve güvenli dosya üretme beklentileri. |
| Üretilen context güvenlik ve kalite kapıları içeriyor mu? | [Security model](docs/SECURITY_MODEL.md) | Secret handling, onay sınırları, test beklentileri ve public-safe kurallar. |
| Skill enterprise starter için yeterli mi? | [Examples](docs/EXAMPLES.md) | SaaS, cybersecurity, API, web, mobile, desktop, data, internal-tool ve library/CLI desenleri. |
| Public repo paylaşmaya uygun mu? | [Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) | Commit, tag, release veya reuse öncesi sızıntı önleme checklist'i. |

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/2705.svg" alt="" aria-hidden="true" width="20"> Güven Sinyalleri

| Sinyal | Standart |
| --- | --- |
| Koddan önce context | Skill, implementation başlamadan önce ürün, mimari, güvenlik, test, operasyon ve task context'i hazırlar. |
| Mod kapılı çıktı | `PROMPT_ONLY`, `DOCS_ONLY`, `PLAN_ONLY`, `CREATE_FILES`, `AUDIT_CONTEXT` ve `REPAIR_CONTEXT` akışı açık tutar. |
| Public-safe paket | Örnekler ve template'ler placeholder kullanır; credential, private prompt, müşteri verisi ve local operator path taşımaz. |
| Agent uyumluluğu | Çıktı Codex, Claude Code, Cursor, Continue, Copilot, Devin/Windsurf, Aider ve benzer araçlara uyumludur. |
| Starter smoke testi | `npm run check`, repo yapısını ve starter materializer dry-run akışını birlikte doğrular. |

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f3af.svg" alt="" aria-hidden="true" width="20"> Neden Var?

AI coding agent'lar güçlüdür ama context yoksa proje hızla dağılır. Belirsiz "bunu kodla" istekleri duplicate modül, zayıf güvenlik, belirsiz mimari ve scope creep üretir.

Bu repo şu ihtiyaçları paketler:

- proje brief'i ve PRD,
- teknik spec ve architecture docs,
- implementation plan ve task listesi,
- security, testing ve quality gates,
- SaaS, cybersecurity, AI product, API, web, mobile, desktop, data product, internal tool ve library/CLI domain pack'leri,
- `AGENTS.md`, `CLAUDE.md`, Cursor, Continue, Copilot, Devin/Windsurf, Aider ve Codex context dosyaları.

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/26a1.svg" alt="" aria-hidden="true" width="20"> Hızlı Başla

| Şunu istiyorum... | Kullan |
| --- | --- |
| Yeni AI-coded projeyi güvenli başlatmak | [Skill entrypoint](.agents/skills/ai-project-starter/SKILL.md) |
| Modları ve örnekleri görmek | [Usage guide](docs/USAGE.md) |
| Skill'i kurmak/kopyalamak | [Install guide](docs/INSTALL.md) |
| Skill yapısını incelemek | [Skill structure](docs/SKILL_STRUCTURE.md) |
| Public repo güvenliğini kontrol etmek | [Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) |
| Güvenlik modelini okumak | [Security model](docs/SECURITY_MODEL.md) |

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f9e9.svg" alt="" aria-hidden="true" width="20"> Ne Sunar?

| Yetenek | Değer |
| --- | --- |
| Proje context temeli | `README.md`, `PROJECT_BRIEF.md`, `PRODUCT_REQUIREMENTS.md`, `TECHNICAL_SPEC.md`, `ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, `TASKS.md` |
| Agent instruction dosyaları | `AGENTS.md`, `CLAUDE.md`, Cursor, Continue, Copilot, Devin/Windsurf, Aider ve Codex context dosyaları |
| Enterprise starter | security, testing, observability, deployment, operations, risk register, ADR |
| Domain pack'ler | SaaS, cybersecurity, AI product, API, web, mobile, desktop, data, internal tool, library/CLI |
| Vibe coding guardrail | anti-slop, non-goals, milestone control, duplicate engelleme, verification-before-done |
| Context audit/repair | zayıf, eski, duplicate, çelişkili veya eksik context dokümanlarını bulma ve düzeltme |
| Template materializer | `scripts/create_starter.py` ile güvenli starter doc seti oluşturma |

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f680.svg" alt="" aria-hidden="true" width="20"> Örnek Kullanım

```text
ai-project-starter skillini CREATE_FILES + ENTERPRISE_STARTER modunda kullan.
Proje fikri: Tenant bazlı takımlar, RBAC, audit log, AI destekli remediation planlama ve güvenli raporlama içeren SaaS siber güvenlik platformu.
```

Sadece vibe coding guardrail:

```text
VIBE_GUARDRAILS modunu kullan. Bu proje vibe coding sırasında dağılmasın diye gerekli agent context ve quality gate dosyalarını hazırla.
```

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f9f0.svg" alt="" aria-hidden="true" width="20"> Desteklenen Modlar

- `PROMPT_ONLY`
- `DOCS_ONLY`
- `PLAN_ONLY`
- `CREATE_FILES`
- `AUDIT_CONTEXT`
- `REPAIR_CONTEXT`
- `ENTERPRISE_STARTER`
- `VIBE_GUARDRAILS`
- `RESEARCH_BACKED`

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f6e1.svg" alt="" aria-hidden="true" width="20"> Public Güvenlik Kuralları

Bu repo şunları içermemelidir:

- API key, token, credential, cookie, private key, certificate veya private URL,
- müşteri verisi veya şirket içi bilgi,
- private system prompt,
- proprietary proje detayı,
- maskelenmemiş log, screenshot, local path veya kişisel not.

Yayınlamadan önce [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) kullanın.

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/2705.svg" alt="" aria-hidden="true" width="20"> Doğrulama

```powershell
npm run check
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

`npm run check`, repo yapısını ve starter materializer dry-run smoke testini birlikte çalıştırır.

## <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/2696.svg" alt="" aria-hidden="true" width="20"> Lisans

MIT. Detaylar için [LICENSE](LICENSE).

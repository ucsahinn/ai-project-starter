#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const skillName = "ai-project-starter";
const skillRoot = `.agents/skills/${skillName}`;
const requiredFiles = [
  "README.md",
  "README.tr.md",
  "README.de.md",
  "README.es.md",
  "README.fr.md",
  "README.pt-BR.md",
  "assets/icon.svg",
  "assets/banner.svg",
  "assets/social-preview.svg",
  "AGENTS.md",
  "LICENSE",
  "SECURITY.md",
  "CONTRIBUTING.md",
  "CODE_OF_CONDUCT.md",
  "CHANGELOG.md",
  "RELEASE_NOTES.md",
  "package.json",
  "llms.txt",
  ".github/CODEOWNERS",
  ".github/workflows/validate.yml",
  `${skillRoot}/SKILL.md`,
  `${skillRoot}/agents/openai.yaml`,
  `${skillRoot}/scripts/create_starter.py`,
  "docs/INSTALL.md",
  "docs/USAGE.md",
  "docs/EXAMPLES.md",
  "docs/SKILL_STRUCTURE.md",
  "docs/PUBLIC_REPO_CHECKLIST.md",
  "docs/SECURITY_MODEL.md",
  "docs/SEO.md",
  "docs/GITHUB_SETTINGS.md"
];

const errors = [];
for (const file of requiredFiles) {
  if (!fs.existsSync(path.join(root, file))) errors.push(`Missing required file: ${file}`);
}

const skillPath = path.join(root, skillRoot, "SKILL.md");
if (fs.existsSync(skillPath)) {
  const text = fs.readFileSync(skillPath, "utf8");
  const frontmatter = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!frontmatter) {
    errors.push("SKILL.md missing YAML frontmatter.");
  } else {
    const keys = [...frontmatter[1].matchAll(/^([A-Za-z0-9_-]+):/gm)].map((match) => match[1]);
    for (const key of keys) {
      if (key !== "name" && key !== "description") errors.push(`SKILL.md frontmatter has unsupported key: ${key}`);
    }
    if (!frontmatter[1].includes(`name: ${skillName}`)) errors.push(`SKILL.md name must be ${skillName}.`);
    if (!/^description:\s*\S/m.test(frontmatter[1])) errors.push("SKILL.md missing description.");
  }
}

const openaiYaml = path.join(root, skillRoot, "agents", "openai.yaml");
if (fs.existsSync(openaiYaml)) {
  const text = fs.readFileSync(openaiYaml, "utf8");
  for (const needle of ["display_name:", "short_description:", "default_prompt:"]) {
    if (!text.includes(needle)) errors.push(`agents/openai.yaml missing ${needle}`);
  }
  if (!text.includes("$ai-project-starter")) errors.push("agents/openai.yaml default_prompt must mention $ai-project-starter.");
}

const oldPrimaryNames = [
  "Context Engineering Project Starter",
  "context-engineering-project-starter"
];
const allowedOldNameFiles = new Set([
  "CHANGELOG.md",
  "RELEASE_NOTES.md",
  "docs/GITHUB_SETTINGS.md",
  "docs/SEO.md",
  "llms.txt",
  "scripts/validate-ai-project-starter.mjs"
]);

for (const file of walk(root)) {
  const rel = slash(path.relative(root, file));
  if (!rel || rel.startsWith(".git/")) continue;
  if (/\.(zip|7z|tar|gz|msi|exe|dmg|log)$/i.test(rel)) errors.push(`Forbidden artifact present: ${rel}`);
  if (/\.(md|json|yaml|yml|mjs|py|toml|txt)$/i.test(rel)) {
    const text = fs.readFileSync(file, "utf8");
    if (/C:\\Users\\/i.test(text)) errors.push(`${rel} contains a local machine path.`);
    if (/\bFIXME\b|\[TO\s*DO:?|TO\s*DO:/i.test(text)) errors.push(`${rel} contains unfinished marker text.`);
    if (/sk-[A-Za-z0-9_-]{20,}/.test(text)) errors.push(`${rel} contains a secret-like token.`);
    if (!allowedOldNameFiles.has(rel)) {
      for (const oldName of oldPrimaryNames) {
        if (text.includes(oldName)) errors.push(`${rel} still uses old primary identity: ${oldName}`);
      }
    }
  }
}

if (errors.length) {
  console.error(errors.map((error) => `ERROR: ${error}`).join("\n"));
  process.exit(1);
}

console.log("OK: ai-project-starter repository");

function walk(dir) {
  const output = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === ".git" || entry.name === "node_modules") continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) output.push(...walk(full));
    else output.push(full);
  }
  return output;
}

function slash(value) {
  return value.replace(/\\/g, "/");
}

#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import path from "node:path";

const scriptPath = path.join(".agents", "skills", "ai-project-starter", "scripts", "create_starter.py");
const smokeArgs = [
  scriptPath,
  "--output-dir",
  ".tmp-ai-project-starter-smoke",
  "--project-name",
  "Acme Security SaaS",
  "--pack",
  "enterprise",
  "--pack",
  "saas",
  "--pack",
  "cybersecurity",
  "--dry-run"
];

const candidates =
  process.platform === "win32"
    ? [
        { command: "py", prefix: ["-3"] },
        { command: "python", prefix: [] },
        { command: "python3", prefix: [] }
      ]
    : [
        { command: "python3", prefix: [] },
        { command: "python", prefix: [] }
      ];

const failures = [];
for (const candidate of candidates) {
  const result = spawnSync(candidate.command, [...candidate.prefix, ...smokeArgs], {
    encoding: "utf8",
    windowsHide: true
  });

  if (result.error?.code === "ENOENT") {
    failures.push(`${candidate.command}: not found`);
    continue;
  }

  if (result.status === 0) {
    if (result.stdout) process.stdout.write(result.stdout);
    if (result.stderr) process.stderr.write(result.stderr);
    process.exit(0);
  }

  const detail = [result.stdout, result.stderr].filter(Boolean).join("\n").trim();
  failures.push(`${candidate.command}: exited ${result.status ?? "unknown"}${detail ? ` (${detail})` : ""}`);
}

console.error(`No Python runtime found for starter smoke test. Tried: ${failures.join(", ")}`);
process.exit(1);

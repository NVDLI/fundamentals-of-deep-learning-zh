// SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
// SPDX-License-Identifier: CC-BY-4.0 AND Apache-2.0

// Generate the single docs page the site renders from the repo's root README.md.
//
// The course site is one page: authors maintain only README.md. This script
// stamps it into docs/intro.md (slug "/") right before `docusaurus start` and
// `docusaurus build` (wired as prestart/prebuild in package.json). Only the
// generated docs/intro.md is gitignored; the docs/ folder itself stays open for
// any hand-authored pages a course wants to add.
//
// README.md is rendered as CommonMark (docusaurus.config.js sets
// markdown.format: 'detect' for .md), so raw `<...>` and `{...}` in the README
// do not break the MDX build.

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const readmePath = path.join(root, 'README.md');
const outDir = path.join(root, 'docs');
const outPath = path.join(outDir, 'intro.md');

const readme = fs.readFileSync(readmePath, 'utf8');
const lines = readme.split('\n');

// First H1 becomes the page title; drop it from the body so the title (which
// Docusaurus renders as the page heading) is not duplicated.
let title = 'Course';
const h1Index = lines.findIndex((l) => /^#\s+\S/.test(l));
if (h1Index !== -1) {
  title = lines[h1Index].replace(/^#\s+/, '').trim();
  lines.splice(h1Index, 1);
}

// The kaizen llms plugin requires a description. Use the first real prose line
// after the title — skip blanks, badge-only lines, and other markup.
const isBadgeOrMarkup = (l) =>
  l.trim() === '' ||
  /^\s*[![]/.test(l) || // image/badge or link-only line
  /^\s*[#>|`-]/.test(l) || // heading, quote, table, fence, list/hr
  /^\s*<\//.test(l);
const descLine = lines.find((l) => !isBadgeOrMarkup(l));
const description = (descLine || `The ${title} course.`)
  .replace(/\s+/g, ' ')
  .replace(/[*_`]/g, '')
  .trim()
  .slice(0, 200);

const yamlString = (s) => `"${s.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;

const frontmatter = [
  '---',
  'slug: /',
  'sidebar_position: 1',
  `title: ${yamlString(title)}`,
  `description: ${yamlString(description)}`,
  '---',
  '',
  '',
].join('\n');

fs.mkdirSync(outDir, {recursive: true});
fs.writeFileSync(outPath, frontmatter + lines.join('\n'));

console.log(`readme-to-docs: wrote ${path.relative(root, outPath)} (title: ${title})`);

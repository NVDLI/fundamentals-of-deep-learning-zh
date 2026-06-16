// SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
// SPDX-License-Identifier: CC-BY-4.0 AND Apache-2.0

// FDL course site — Docusaurus config.
// The only theme wiring is the single `presets` entry. Everything else is this
// course's own metadata. Authors edit this file + course.yaml + docs/*.md only.

const rawBase = (process.env.SITE_BASE_PATH || '').trim();
const baseUrl = rawBase ? `${rawBase.replace(/\/$/, '')}/` : '/';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'FDL Course',
  tagline: 'A hands-on, open-source deep learning course',
  // GitLab Pages assigns the real URL on first deploy; baseUrl is derived from
  // CI_PAGES_URL at build time via SITE_BASE_PATH.
  url: 'https://gitlab-master-pages.nvidia.com',
  baseUrl,

  favicon: 'img/favicon.svg',
  onBrokenLinks: 'warn',
  i18n: {defaultLocale: 'en', locales: ['en']},

  // The single page is generated from README.md (see scripts/readme-to-docs.js).
  // 'detect' renders .md as CommonMark, so raw `<...>`/`{...}` in the README
  // don't break the MDX build.
  markdown: {format: 'detect'},

  // This one line gives the shared Kaizen look + search + i18n + AI layer.
  presets: [
    [
      '@dli/docusaurus-theme-kaizen',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: false,
      },
    ],
  ],

  themeConfig: {
    colorMode: {defaultMode: 'dark', respectPrefersColorScheme: false},
    navbar: {
      title: 'FDL Course',
      items: [{to: '/', label: 'Course', position: 'left'}],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} NVIDIA.`,
    },
  },
};

module.exports = config;

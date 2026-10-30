# Fengmian

Fengmian is an open-source Codex skill and plugin for turning articles, videos, scripts, and briefs into clear creator covers and thumbnails.

It helps creators choose a clear promise, show relevant evidence, and coordinate the image, cover wording, and publishing title. It protects supplied identity and approved edits, treats claims and brand assets carefully, and adapts each requested aspect ratio.

This public repository contains no portrait, private conversation, real client project, API key, proprietary font, or third-party logo.

## Features

- Chinese and English creator-cover workflows
- 3:4, 4:3, and 16:9 composition guidance
- Person-present and no-person routes
- Official-logo and neutral semantic-icon handling
- Optional adventure or journey style
- Exact-text protection and thumbnail-scale validation
- Optional source-aware hypotheses and performance testing
- Dependency-free PNG dimension checker

## Install

Ask Codex to install the `fengmian` skill from this repository with `$skill-installer`, or copy `skills/fengmian` into a supported personal skills directory.

For local development, clone the repository and open it as a Codex plugin. The plugin manifest is at `.codex-plugin/plugin.json`.

After installation, invoke it explicitly:

```text
使用 $fengmian，根据这篇文章制作 4:3 封面，不使用人物。
```

Codex can also select it automatically when a request matches the skill description.

## Privacy model

Fengmian has no bundled identity. Supply a portrait only in the task where it is needed. Do not commit portraits, private screenshots, client materials, or licensed brand files to this repository.

If no portrait is supplied, the skill defaults to a no-person composition.

## Validate

Run the dependency-free repository tests:

```bash
python3 -m unittest discover -s tests -v
```

Validate a rendered PNG:

```bash
python3 skills/fengmian/scripts/check_png_dimensions.py \
  assets/fengmian/example-4x3-v01.png \
  --width 1448 \
  --height 1086
```

The official Skill Creator and Plugin Creator validators can also be used when available in the host Codex installation.

## Contributing

Keep the public skill generic and privacy-safe. New examples must use original or properly licensed assets, and every brand asset must include provenance. See `CONTRIBUTING.md` and `ASSET-LICENSES.md`.

## License

Licensed under the Apache License 2.0. See `LICENSE`.

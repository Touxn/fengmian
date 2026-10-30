---
name: fengmian
description: "Create or revise creator covers and thumbnails from an article, video, script, or brief. 制作创作者封面、缩略图及指定比例版本；普通文章排版不触发。"
---

# Fengmian

Make the content's value visible and give the intended viewer a credible reason to click. Preserve exact requested text, supplied identity, and accepted work. User instructions and confirmed choices take priority.

Choose one clear promise, useful visual evidence, readable hierarchy, and complementary image and text. Thumbnail patterns are hypotheses, not proof of higher clicks. The public skill contains no default portrait, project images, or private history.

## Load guidance when needed

- `references/cover-strategy.md` for new concepts, wording, or reference analysis.
- `references/creator-cover-grammar.md` for visual hierarchy and composition.
- `references/layout-spec.md` for formats and display-size checks.
- `references/person-integration.md` when a person is present.
- `references/icon-policy.md` when an official or semantic icon is needed.
- `references/revision-control.md` for local edits, face corrections, and additional ratios.
- `references/evidence-and-testing.md` for source quality or requested performance testing.
- `references/adventure-style.md` only when an adventure or journey concept is selected.

Reuse guidance already read. Do not restart concept discovery for a local edit.

## Resolve the task and choose the operation

From the conversation, determine the topic, audience, placement, available evidence, publishing title, exact on-cover text, output count and ratio, supplied assets, requested operation, and protected content. Ask only about a missing fact that materially affects the work. Preserve explicit no-person, no-text, and output-count instructions.

For a new unselected topic, present three meaningful content-specific concepts and recommend one. Explain the promise, main image, wording, and tradeoff. Wait for the user's selection before generating. Differences should concern the reason to click or visual relationship. An existing selection satisfies this gate; follow an explicit instruction to skip proposals.

For a local revision, edit the selected target and protect everything outside the requested scope. A title change does not authorize a face change. For a face correction, use the accepted scene and the supplied original portrait. For an additional ratio, adapt the approved concept without requesting a new selection. Cropping is permitted only when authorized and essential content survives. Separate candidates from accepted work.

When no ratio is specified, infer it from the named platform. If the placement does not settle it, make one 4:3 concept first; do not add outputs beyond the request. Explicit sizes and counts take priority.

## Build the visual promise

Inspect available finished outputs, screenshots, and meaningful comparisons before inventing a metaphor. Prefer a real result when it directly supports the promise. Distinguish actual output from illustration and do not infer time savings, price, or quality from appearance alone.

The first focal point may be a result, comparison, person, object, or short phrase. Use scale, grouping, contrast, and negative space to give supporting elements clear roles. Do not mandate title-first hierarchy, a fixed person position, or physical interaction.

Let the image show evidence, situation, contrast, or emotion. The cover phrase can frame the result or question, while the publishing title adds context. Evaluate them together. Preserve every character of approved wording. When wording is delegated, simplify redundancy without inventing claims.

A person may contribute recognition, trust, explanation, emotion, or action. No person is required. When a real person is requested, use the original portrait supplied for the task as the identity authority. This public skill has no bundled portrait; if none is supplied, default to a no-person composition unless the user explicitly requests otherwise. Protect face, glasses, age, and expression in revisions. For depicted physical contact, verify anatomy, support, and lighting.

Use supplied or verified official assets where needed and cite provenance. A semantic icon can explain an abstract concept but must not impersonate a brand. Do not require an icon for every subject. Adapt reference mechanisms into an original composition; public views do not establish a thumbnail's causal performance.

## Generate, inspect, and deliver

Use the supported image tool and its current instructions. Do not claim unsupported masks, deterministic edits, or pixel guarantees. Preserve accepted baselines, use candidate versions, and stop repeating a method that damages protected features.

1. Check the selected concept, exact text, output count, and dimensions already established; ask only about a material unresolved gap.
2. At full size inspect wording, evidence, logo fidelity, and identity when present. Check anatomy and contact where depicted. Verify actual PNG dimensions with `scripts/check_png_dimensions.py` when available.
3. For local edits compare protected regions with the accepted baseline at equal scale. Separate visual preservation, measured identical pixels, and user approval.
4. Review the cover with its publishing title at the intended display size. When unknown, use aspect-preserving previews 320 and 160 pixels wide as labeled heuristics, not measured recognition tests. Inspect face and logo fidelity separately at useful size.
5. Save versioned files under `assets/fengmian/` in the current workspace. Record the selected promise, relevant inputs and provenance, per-ratio state, protected regions, and checks performed. Do not publish, monitor, test, or create extra variants without the user's request.

Return clickable output paths, verified dimensions, relevant asset sources, and material limitations. Never infer approval or improved click-through rate from generation success or visual inspection.

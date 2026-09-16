---
name: fengmian
description: "Create creator covers and thumbnails from an article, video, script, or brief. 制作创作者封面、缩略图及指定比例版本；普通文章排版、海报或完整品牌设计不触发。"
---

# Fengmian

Turn source content into a clear creator cover. Make the topic, viewer benefit, and visual story understandable at thumbnail size while keeping claims and supplied identity accurate.

The user's instructions take precedence over this skill. Do not add a person, optimize publishing copy, use a brand mark, or create extra aspect ratios when the user has said otherwise.

## Load guidance only when needed

- Read `references/cover-strategy.md` when extracting the message, choosing a route, or proposing alternatives.
- Read `references/creator-cover-grammar.md` when composing a new visual concept or fixing weak hierarchy.
- Read `references/layout-spec.md` before producing or validating a requested ratio.
- Read `references/person-integration.md` only when a supplied portrait or requested person appears in the cover.
- Read `references/icon-policy.md` only when a named product, platform, organization, logo, or symbolic icon appears.
- Read `references/adventure-style.md` only when the user requests an adventure or journey style, or when that route clearly fits the content. It is never the default.

Reuse guidance already read during revisions. Do not reload unrelated references.

## Input and privacy contract

Use any available combination of source content, publishing title, target audience, proof, platform, ratio, supplied assets, and restrictions. Source content plus a working title is enough to begin when the missing details are low risk.

- Never assume access to earlier conversations, private files, portraits, logos, or approved covers. Inspect only assets actually available in the current task.
- This public skill contains no default identity. If no portrait is supplied, default to a no-person composition.
- Treat a supplied portrait as task-scoped identity input. Do not copy it into the skill or a public repository.
- Ask only when a missing fact would materially change identity, legal asset use, or the truth of a claim.

Supported default deliverables:

- 3:4 portrait: 1086 x 1448
- 4:3 landscape: 1448 x 1086
- 16:9 landscape: 1280 x 720

If no ratio is given, choose the format implied by the named platform. If the platform does not settle it, make one 4:3 concept first. Create multiple ratios only when requested, and compose each ratio independently rather than cropping.

## Workflow

1. Inspect the source, requested text, supplied portrait, screenshots, and permitted product assets.
2. Extract the topic anchor, intended viewer, concrete transformation, strongest proof, emotional tone, and one useful unanswered question.
3. Separate the publishing title from the cover phrase. Preserve the publishing title unless optimization was requested. Compress the cover phrase to one topic and one value signal.
4. Align four signals: headline, dominant prop, person action when present, and background world. Each should point to the same subject without repeating the same graphic.
5. Choose a scene from where the task happens, where its result is used, or the simplest physical metaphor that explains it. Keep the background supportive and quiet.
6. When alternatives are requested, propose the requested number, or three when unspecified. For each, state the cover phrase, click promise, visual metaphor, main object, person role if any, strongest proof, and claim or clutter risk.
7. Reject a route before generation when the topic is not recognizable at thumbnail size, the prop and action tell different stories, more than three primary focal groups remain, or the result resembles a product ad instead of a creator cover.
8. Resolve named entities through `references/icon-policy.md`. Prefer user-supplied or official assets, and label neutral generated symbols as semantic icons rather than official logos.
9. Sketch the thumbnail as two or three large silhouettes: headline, subject or person-prop cluster, and optional proof strip. Add detail only after this hierarchy works.
10. Generate or assemble the requested ratio. Protect exact text and official assets from model redraws; use deterministic typography or compositing when available.
11. Inspect full size and at about 10 percent size. Regenerate when the title loses priority, the prop becomes unclear, a gesture disappears, the face is inaccurate, or the background reads before the topic.
12. Verify pixel dimensions and report only files that actually exist and passed inspection.

## Copy and evidence rules

- Prefer a short topic phrase plus one value dimension. Keep exact product names, versions, code identifiers, and necessary English.
- Preserve user-approved wording. Do not silently rewrite a publishing title or exact on-canvas phrase.
- Use proof such as `实测`, a duration, a result, or a case only when the source or completed work supports it.
- Avoid unsupported superlatives, rankings, financial promises, guarantees, and claims that erase the creator's editorial role.
- Leave part of the answer for the article or video. Reveal the subject and value without giving away every method or conclusion.
- Do not add filler labels, invented metrics, fake interfaces, or decorative English.

## Visual rules

- Headline is the first focal point. The dominant object or person-object action is second.
- Use one broad scene or atmospheric field, not a wall of cards, devices, logos, and explanatory diagrams.
- Use one primary product or concept mark. Add a second only when the relationship between two entities is the story.
- Translate abstract capabilities into one understandable object or action: a manual, toolbox, bridge, shelf, cockpit, production line, comparison, or finished result.
- When a person is present, connect hand, gaze, body direction, lighting, and depth to the dominant object. Do not paste an unrelated portrait into a corner.
- Keep exact text, faces, hands, and official marks free of distortion.

## Validation and handoff

Save final assets in the current workspace under `assets/fengmian/` using versioned slugs:

- `<slug>-3x4-v01.png`
- `<slug>-4x3-v01.png`
- `<slug>-16x9-v01.png`
- `icons/<slug>-concept-icon-v01.png` for a generated semantic icon

Use `scripts/check_png_dimensions.py` to verify PNG dimensions when shell execution is available.

Report:

- clickable output paths and pixel dimensions
- selected cover phrase and visual metaphor
- any publishing-title change the user authorized
- source links for official logos or product imagery
- whether each key icon is user-supplied, official, or a generated semantic icon
- whether thumbnail hierarchy, exact text, identity when applicable, and requested-ratio checks passed

Do not call a concept, prompt, static check, or unverified file a delivered cover.

## Invocation examples

`使用 $fengmian。根据这篇文章先给我三组 4:3 封面命题，不使用人物。`

`Use $fengmian to create independent 3:4 and 16:9 covers from this video script. Use the portrait I supplied only for this task.`

# Official and semantic icon policy

Use this reference whenever the cover involves a brand, product, platform, organization, tool, file type, technical concept, or abstract capability.

## Icon classes

Classify every key icon before composition.

1. User-supplied asset
2. Verified official asset
3. Generated semantic icon, called `意象图标`

Do not mix these classes silently. Record provenance in the final handoff.

## User-supplied assets

- Inspect resolution, transparency, geometry, cropping, and visible text.
- Treat a clear user-supplied asset as authoritative for the request.
- Treat a supplied icon collection as a candidate set. Use every icon only when the user explicitly requires all of them.
- Preserve recognizable geometry and proportions.
- Ask only when the file is ambiguous, damaged, or conflicts with a verified current identity.
- Avoid tracing or stylistically mutating a supplied official logo.

## Official asset search

Search primary sources in this order:

1. Official product or organization website
2. Official press, media, or brand kit
3. Official documentation
4. Verified official GitHub organization or repository
5. Official app store listing when no higher-quality source exists

Avoid third-party logo aggregators, unofficial icon libraries, reposted image sites, and secondary articles.

Verify:

- Correct product and current version
- Official domain or verified organization
- Consistent geometry and colors across official pages
- Adequate resolution or vector availability
- Usage restrictions when a brand kit states them

Download the official asset when allowed and practical. Save it as a local reference for the current cover. Cite the official source in the final handoff.

## When no official icon exists

Create a brand-neutral semantic icon when:

- The concept has no official identity
- Official sources show no icon
- The available official asset is unusable or cannot be reliably verified
- The topic is a file, process, relationship, or abstract capability

Do not imitate a nearby brand or construct a trademark-like wordmark.

## Semantic icon brief

Generate the icon as a separate asset before generating the cover.

Define:

- Concept name
- Core function
- One physical metaphor
- One primary shape
- One supporting cue
- Palette derived from the cover or verified topic colors
- Flat, dimensional, or material style
- Transparent or simple solid background
- No text unless the text is an exact technical identifier required by the topic

Keep the icon understandable at 64 to 128 pixels. Use simple geometry, a strong silhouette, and no more than two semantic cues.

Examples:

| Concept | Semantic icon direction |
| --- | --- |
| Skill | Open manual with one tab and a small capability spark |
| SKILL.md | Document or binder with a workflow tab, without claiming official status |
| Progressive disclosure | Three stacked layers revealed from top to bottom |
| Agent | Compass or operator node guiding a path to a result |
| Reusable workflow | Circular path connecting a checklist and finished artifact |
| Verification | Checklist combined with a magnifier or seal |

Save generated icons under:

`assets/fengmian/icons/<slug>-concept-icon-v01.png`

Inspect the icon before cover generation. Regenerate it when the silhouette is unclear, the metaphor is misleading, text is malformed, or the result resembles an existing brand mark.

## Cover placement

- Use one dominant icon or product object by default.
- Add a second icon only when the relationship is the central message.
- Group supporting icons into one subordinate cluster.
- Keep icon cards free of repeated brand text when the headline already names the product.
- Preserve official clear space around verified logos.
- Avoid placing a logo on a conflicting color or inside a distorted 3D surface.
- Use a generated semantic icon as an explanatory object, never as an official badge.

## Handoff language

Report each key asset using one of these labels:

- `用户提供`
- `官方素材` with source link
- `生成的意象图标` with its concept description

If an official search finds no reliable asset, state that an意象图标 was used to avoid inventing an official identity.

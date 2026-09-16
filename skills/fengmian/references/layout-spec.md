# Fengmian layout specification

Read this reference before generating or validating a requested aspect ratio. The public skill intentionally bundles no personal or project-specific cover image; derive geometry from these relationships and from references supplied in the current task.

## Shared hierarchy

Preserve this reading order:

1. Cover phrase
2. Dominant object, visible result, or integrated person-object action
3. Optional proof strip

Use no more than three primary focal groups. Keep negative space around every character and, when present, the face and hands. Choose colors from the subject or campaign rather than defaulting every topic to the same blue technology scene.

Avoid interface grids, scattered document cards, repeated icons, network nodes, dashboard walls, and decorative light trails unless the subject genuinely requires them.

## Headline

- Use one or two lines when possible.
- Break at semantic boundaries and keep protected product names or versions together.
- Emphasize one value word with a topic or brand-supported accent color.
- Maintain strong light-dark separation and a clean outline when needed.
- Keep hair, hands, icons, glow, particles, and background texture out of the text zone.
- Use a proof strip only when it adds verified credibility, and keep it subordinate.
- Move detailed promises into the publishing title instead of building a long subtitle.

## 3:4 portrait, 1086 x 1448

- Place the headline within roughly the upper 27 to 34 percent.
- Use two lines by default; allow three only when exact text requires it.
- Put the dominant object in the lower-left, lower-center, or central field.
- If a person is present, place them in the lower-right or integrate them through the center when the action requires contact.
- Keep the person roughly within 28 to 38 percent of canvas width unless the visual metaphor needs a larger body action.
- Keep platform overlay and lower metadata areas clear.

## 4:3 landscape, 1448 x 1086

- Reserve approximately x=4% to x=66% and y=5% to y=45% for the headline.
- Place the dominant object across the lower-left or center-left field.
- If a person is present, place them within the rightmost 25 to 32 percent, extending the interacted object or arms into the center.
- Keep at least 40 pixels of clear space around text at the target size.
- Use one broad background plane to connect title, object, and person.

## 16:9 landscape, 1280 x 720

- Place the headline in the left 45 to 58 percent.
- Limit it to one or two lines and shorten the cover phrase when needed.
- Put the dominant object in the center or center-left.
- If a person is present, use the rightmost 23 to 30 percent and shift inward when interaction would otherwise disappear.
- Keep the lower-right clear for common duration overlays.
- Use fewer background details because the cover will appear smaller in feeds.

## Person-present variants

- Read `person-integration.md`.
- Keep the person smaller than the headline's overall visual mass.
- Treat the person and object as one action cluster with a readable touch point and weight cue.
- Preserve the supplied identity, natural expression, coherent lighting, and continuous color across face and neck.
- Keep one outfit across ratios in the same campaign.

When no portrait is supplied, omit the person and give the dominant object or result enough scale to become the second focal point.

## Object and background

- Use one dominant semantic object, finished result, or broad scene.
- Prefer a physical metaphor that makes an abstract function visible.
- Use verified official product imagery only when it is relevant and legally available.
- Use a neutral semantic icon when no reliable official asset exists.
- Keep objects large enough to recognize at thumbnail size.
- Let background establish place, atmosphere, depth, and contrast without explaining features.

## Text fitting and revisions

- Preserve every approved character, product name, version, and identifier.
- Reduce font size before breaking a protected phrase.
- Reject any composition where an object, outline, hand, hair, or effect touches the headline.
- Treat 3:4, 4:3, and 16:9 as independent artifacts.
- Leave approved ratios unchanged when feedback names only one format.
- For identity correction, return to the supplied original portrait rather than repeatedly editing an already altered face.

## Thumbnail validation

At about 10 percent size, confirm:

- topic is identifiable within one second
- cover phrase remains readable
- only one value promise is visible
- dominant object remains recognizable
- person, when present, supports the message without overtaking the title
- background reads as one scene
- text, face, and hands remain unobstructed
- requested ratios feel related without being cropped copies

Finally verify pixel dimensions with `../scripts/check_png_dimensions.py` or another deterministic image inspector.

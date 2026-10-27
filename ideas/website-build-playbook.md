# Website-build playbook

**Status: works.** Evidence: the VR Academy landing-page rebuild
(`website/v2/`), run start to finish with this method in one continuous
session — from "the current site is stale" to a signed-off page, a chosen
logo, and three comparison versions kept intact throughout.

This file is venture-agnostic on purpose. It describes *how* to build a
website with an AI pair, not what Unayurved's website should say. The next
time this is needed — an e-commerce store, a SaaS landing page, anything —
this is the starting instruction, and the phases below are the same
regardless of what's being sold.

If you only remember one thing from this file: **the planning phase is
the product.** The build itself is mostly mechanical once the plan is
right. Where this process went wrong at all, it was always because a
phase below got skipped or rushed, never because the code was hard to
write.

---

## The core insight

A website brief given in one sentence ("make it more modern") under-specifies
the problem so badly that any output is a guess. The fix isn't a longer
brief — it's a structured back-and-forth *before* any code exists, where
the constraints, the competition, and the one idea worth building around
all get established on the record. That back-and-forth is Plan Mode. It is
cheap to redo; a built page is not. Front-load the thinking there.

---

## The phases

### Phase 0 — Read before you design

Before any visual idea, read everything that already constrains the
answer: brand voice, positioning, budget, past decisions, what's legally or
factually claimable, who the buyer is, and what action the page needs to
drive (a purchase, a signup, a message). For VR Academy this meant reading
`brand/positioning.md`, `brand/voice.md`, `decisions/decision-log.md`,
`WIP.md`, and the live ad copy before drawing anything — which is why the
first build already respected the settled "five students" USP, the
approved hook, and the WhatsApp-only lead channel instead of re-litigating
them.

**Do:** treat every existing constraint doc as load-bearing until told
otherwise. **Don't:** propose a new brand voice, a new offer, or a new
conversion channel as a side effect of a "redesign" ask — that's a
different, bigger conversation, and folding it in silently is how a design
task turns into scope creep nobody agreed to.

### Phase 1 — Research wide, not just the category

Look at direct competitors *and* premium sites outside the category. The
category tells you the baseline; the outside sites tell you what "good"
looks like when a bigger budget or a longer design history built it. For
VR Academy this meant Cuemath and Mole Academy (direct competitors) next
to Brilliant, Stripe, and Linear (unrelated premium sites) — and naming a
few sites was not enough. Fetch them, look at the real page (structure,
motion, what the hero actually shows), and note technique, not just
vibe: "a stack of soft-tinted demo cards, each with one animated example"
is usable; "feels clean and modern" is not.

**Anti-pattern:** researching only inside the niche. Every direct
competitor is optimizing against the same constraints as the client, so
copying them caps the outcome at parity, not advantage.

### Phase 2 — Find the one idea, then make it visual

Every business has one claim that actually differentiates it from the
next option. Find that claim, and then find a way to *show* it rather
than state it. For VR Academy the claim was "five students, not forty" —
stated as text on every competitor's site. Turning it into an animated
40-tile-collapsing-to-5 visual, and later an interactive slider a parent
can drag, made it a lived experience of the number instead of a line item.
For an e-commerce store this might be a fit guarantee, a supply-chain
claim, or a satisfaction number — the method is the same: find the
sharpest true claim, then design one moment on the page that makes a
visitor feel it rather than read it.

If the true claim can't be shown, showing it is not worth forcing. A
weaker but honest visual beats a strained metaphor.

### Phase 3 — Build a style tile before the page

Before writing a single section of real copy, build a small, cheap,
disposable page that shows only: the color palette (as literal swatches,
with hex values visible), the type scale at every size it will actually be
used, the buttons, one full-bleed color band, and one or two of the
signature interactive moments from Phase 2 — working, not mocked. Nothing
else. No hero, no nav, no real page structure.

This is the single highest-leverage step in the whole process. It is the
moment to get wrong cheaply. The VR Academy style tile
(`website/v2/style-tile.html`) is the concrete template: it let the
palette and the display typeface (a serif vs. a geometric sans, toggled
live on the same page) get judged and picked *before* an 800-line page was
built around the wrong one. Get explicit sign-off on the palette and the
type here. Everything downstream inherits this decision, so revisiting it
later means rebuilding, not tweaking.

**Rule:** the style tile links to a separate `tokens.css` (or equivalent)
that the full page also links to. Never let the palette live twice in two
files by hand — that's exactly how a site drifts out of sync with its own
brand file over time.

### Phase 4 — Build with placeholder discipline

Build the full page once the style is signed off. Two hard rules carry
over from every domain, not just coaching:

- **Never state a claim that isn't confirmed.** If a deliverable, a price,
  a duration, or a credential isn't nailed down, either leave it out or
  build the section as a visibly tagged placeholder (a dashed border and a
  "replace before launch" label worked well) so it can't ship by accident
  and doesn't block seeing the layout.
- **One conversion action, repeated.** Decide the single thing the page
  wants a visitor to do (message on WhatsApp, add to cart, book a demo)
  and put that exact action at every natural exit point — after the hero,
  after the proof, after the objection-handling, in a sticky mobile bar.
  Competitor benchmarking the count of these (VR Academy's competitors
  averaged 4; the rebuild used 6-8) is a fast, concrete design metric.

### Phase 5 — Verify like a skeptic, not like a designer

Looking at a screenshot is not verification. Real verification, done in
this project and worth repeating exactly:

- Click every conversion button and confirm the destination and any
  pre-filled content are correct — not just that the button exists.
- Run every animation/interaction start to finish, including edge cases
  (what does the interactive demo look like at its extremes?).
- Force a narrow mobile width and check for horizontal overflow — most
  buyers on a phone.
- Force reduced-motion and confirm every animated element has a sane
  static fallback.
- If comparing multiple versions, **fingerprint the ones not being
  touched** (`md5` the file) before and after each change to prove nothing
  leaked across versions. This caught nothing going wrong in this project
  only because it was checked every time, not because it wasn't a risk.
- Read the rendered page's full text against the claims list from Phase 4
  and grep for banned words/symbols (this caught real bugs: a stuck
  animation, a mid-transition screenshot false alarm, a color
  inconsistency the client's own eye caught that a static review missed).
- **Measure speed, don't assume it.** Run Lighthouse (`npx lighthouse <url>`)
  with its default *mobile* profile — slow 4G and a slower phone CPU. That is
  the honest number; desktop flatters. On the VR Academy page it found what no
  visual check could: the page could not draw until Google's font server
  answered, costing 2 seconds on mobile. Hosting the two font files with the
  page took the mobile score from 88 to 99 and first paint from 3.1 s to 1.1 s.
  Test the candidate fix on a scratch copy first, so the real page only changes
  once the gain is proven. It also caught a `<meta charset>` pushed past the
  first 1,024 bytes by a long header comment — an encoding bug that only shows
  up on some hosts.
- **Test at real device widths.** `resize_window` did not change the viewport
  in the browser tool used here, so load the page inside same-origin iframes at
  each width (360, 375, 390, 412, 768, 1024, 1280, 1440, 1920) and measure
  overflow, header fit, tap-target sizes and any custom layout logic in each.
  Add a static check of CSS/JS features against the oldest phones you care
  about (`npx doiuse`, `npx es-check`). Say plainly what could not be tested —
  real iPhones and the Safari/Firefox engines need the page hosted or shared.

### Phase 6 — Iterate from specific feedback, additively

When feedback names a specific thing ("I don't like the logo", "this
section uses three colors, use one"), fix exactly that thing in exactly
the named place. Two habits kept this fast and safe:

- **Never edit a version under active comparison without being asked.**
  When multiple directions are being judged side by side, each one stays
  frozen until the client picks or asks for a change to a *named* one.
  Fingerprinting (Phase 5) is what makes this provable, not just promised.
- **When a creative concept doesn't render as intended, say so.** One
  logo concept in this project was designed as a "camera aperture with a
  small hole," but rendered as a five-point star because the hole was too
  small to read. The write-up was corrected to describe what it actually
  looked like, with the weakness stated plainly, rather than left
  describing the original intent. A design system a client can't trust to
  self-report its own flaws will get less honest feedback in return.

### Phase 7 — Log decisions as they're made

Every real decision (a palette choice, a rejected concept, a wording call,
a claim confirmed as deliverable) gets one line in an append-only decision
log, dated, with the reasoning — not just the plan file. The plan file
describes intent; the log is what actually happened and why, and it's what
lets a later session (or a later you) pick the thread back up without
re-litigating something already settled. `decisions/decision-log.md` in
this repo is the concrete example — read it top to bottom and the entire
arc of this rebuild, including the parts that got rejected, is legible.

---

## What changes per project, what doesn't

| | Stays the same | Changes per project |
|---|---|---|
| Phase 0 | Read constraints before designing | *Which* docs exist to read |
| Phase 1 | Research wide: category + outside | *Which* sites are relevant |
| Phase 2 | One claim, made visual | *What* the claim is |
| Phase 3 | Style tile before full build | The palette/type/motion chosen |
| Phase 4 | Placeholder discipline, one repeated action | *What* the action is (buy, book, message) |
| Phase 5 | Rigorous browser verification | The specific checks (a cart flow needs different tests than a chat CTA) |
| Phase 6 | Additive, named-scope iteration | — |
| Phase 7 | Decision log | — |

---

## To run this again

Use the `website-build-planner` skill (`.claude/skills/website-build-planner/`)
to start. It walks the phases above in order, beginning in Plan Mode.

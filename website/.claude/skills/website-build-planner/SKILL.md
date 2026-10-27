---
name: website-build-planner
description: Runs the plan-first methodology used to build the VR Academy landing page rebuild (website/v2/) — read every existing constraint before designing, research direct competitors AND unrelated premium sites for technique, find the one true differentiating claim and make it visual, build a cheap disposable style tile (palette, type, buttons, one working interactive demo) and get it signed off BEFORE writing the real page, then build with placeholder discipline and verify like a skeptic in a real browser. Venture-agnostic — works for an e-commerce store, a SaaS page, or anything else, not just VR Academy. Use when the user wants to build, redesign, or rebuild a website and wants this same rigorous process, when they say a current site is "stale" or "boring" and ask what to do about it, or when they explicitly name this skill or ask to "do it like we did for the VR Academy site."
---

# Website-build planner

Full methodology, worked example, and the "what changes per project vs.
what doesn't" table live in **`ideas/website-build-playbook.md`** — read
that file in full before starting. This skill is a router into it, not a
replacement for it: if the two ever disagree, the playbook is the source
of truth and this file should be updated to match, not the other way
round.

## When to use this

The user wants a website (new, or a rebuild of an existing one) and the
starting brief is short — "make it more modern," "our site is boring,"
"build a landing page for X." Short briefs under-specify the problem. This
skill's job is to not let that under-specification turn into a guess.

**Do not use this** for a small, scoped, already-specified change to an
existing page ("change this button's color," "fix this typo") — that's
just an edit, no planning phase needed.

## How to run it

Work through the seven phases in `ideas/website-build-playbook.md`, in
order, resisting the urge to skip to Phase 4 (the actual build):

1. **Read constraints first.** Before anything else, find and read every
   doc that already constrains the answer for this project — brand voice,
   positioning, budget, past decisions, what's legally/factually
   claimable, the target buyer, the one action the page must drive. If
   this is a fresh project with no existing docs, say so and ask the
   handful of questions needed to establish these before designing
   anything (don't invent a brand voice or an offer on the user's behalf).

2. **Research wide.** Direct competitors *and* premium sites outside the
   category. Fetch and actually look at real pages — structure, motion,
   what the hero shows — not just names recalled from memory. Use browser
   automation to view sites at real sizes if available; note technique,
   not adjectives.

3. **Find the one idea.** Identify the single sharpest true differentiating
   claim, and find a way to make a visitor *feel* it (an animation, an
   interactive element, a comparison) rather than just read it. If the
   claim can't honestly be shown, don't force a metaphor — say so and fall
   back to stating it plainly.

4. **Build the style tile.** A small, disposable, no-real-copy page: color
   palette as literal labeled swatches, the type scale at real sizes,
   buttons, one full-bleed color band, and the signature interactive
   moment from step 3 — working. Nothing else. Link a shared tokens file
   from both the style tile and the eventual real page — never let the
   palette exist twice by hand.

5. **Build with placeholder discipline.** Never state an unconfirmed
   claim (price, duration, credential, result) — leave it out or build it
   as a visibly tagged placeholder. Pick the one conversion action the
   page wants and repeat it at every natural exit point.

6. **Verify like a skeptic.** In a real browser: click every conversion
   action and confirm the actual destination/payload, run every animation
   including its edge cases, force a narrow mobile width and check for
   overflow, force reduced-motion and confirm static fallbacks, and if
   comparing multiple versions, fingerprint (`md5`) the ones not being
   touched before and after every change to prove nothing leaked across
   them. Re-read the rendered page's text against the claims list from
   step 5. Measure speed with Lighthouse's mobile profile (test any fix on a
   scratch copy first — hosting fonts locally beat Google Fonts by ~2 s on
   mobile), and test at real device widths using same-origin iframes.

7. **Log every real decision** (palette pick, rejected concept, wording
   call, confirmed deliverable) as one dated line with its reasoning, in
   this project's append-only decision log — not just in the plan file.

When iterating on feedback: fix exactly the named thing in exactly the
named place; never edit a version under active side-by-side comparison
unless it's the one named; and if a creative concept doesn't render the
way it was designed to, say so plainly rather than describe the intent
instead of the result.

## Output

By the end: a signed-off style tile, one or more full page builds (kept
side by side if multiple directions were explored), a decision log
entry per real choice made, and — if the user asks for it — a push to
version control following whatever branch/PR convention this project uses
(check `CLAUDE.md` / `HANDOFF.md` first; don't invent one).

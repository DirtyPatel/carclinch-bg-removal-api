# [MVP] Define image quality criteria for MVP acceptance #4


**User Story:**\
As the team,
We want clear quality criteria,
So that we can decide if the MVP output is acceptable.

**Task:**\
Review background-removed car images from PoC testing
and define what "good enough for MVP" means.

**Acceptance Criteria:**\
Review sample output images\
Define quality checks (edges, artifacts, consistency)\
Identify acceptable vs non-acceptable results

**Deliverable:**\
Short quality checklist + Go/No-Go opinion for MVP demo.

---

## Output Image example & setting

*Figure 1: 2019 Kia Sorento output image setting*\
![2019 Kia Sorento output image setting](/screenshots/2019-Kia-Sorento-output-image-setting.png)

```
<img fetchpriority="high" class="img-fluid w-100 h-100 car-details-main-img" src="https://imgs-cdn1-dmhch4b7bfgcbhgm.z03.azurefd.net/bf3dddd3-ff8b-4458-96bf-ea18a5b0c2b4/6b774366-78ff-4a1f-9d34-71b107ccbc40.webp" alt="Main image">
```

Rendered size: 573 x 430 px\
Rendered aspect ratio: 573:430\
Intrinsic size: 1024 x 768 px\
Intrinsic aspect ratio: 4:3\
File size: 410 kB\
Current source: https://imgs-cdn1-dmhch4b7bfgcbhgm.z03.azurefd.net/bf3dddd3-ff8b-4458-96bf-ea18a5b0c2b4/6b774366-78ff-4a1f-9d34-71b107ccbc40.webp

---

## Proposed MVP Image Quality Criteria (Checklist + Go/No-Go)

### Scope

Applies to:

- **Car cutout** (background removed)
- **Car composited** onto a **user-uploaded background**
- (Optional/Nice-to-have) **shadow** and/or **watermark**

### Definition of “Good Enough for MVP”

The output is acceptable if a viewer **can’t immediately spot obvious cutout mistakes** at normal viewing size (web listing) and the car looks naturally placed on the new background.

---

## Quality Checklist (Manual Review)

**1) Cutout completeness (car parts)**

**Pass if:**

- No major missing car areas (roof, mirrors, wheels, bumpers, grille)
- Fine details may be imperfect, but the car still reads clearly

**Fail if:**

- Missing mirror/wheel/roof chunk
- Holes inside the car body (transparent gaps)
- Car is partially erased due to background similarity

✅ **MVP threshold:** *No missing “large parts” visible at normal web size.*

**2) Edge quality (halo, jaggies, fringing)**

**Pass if:**

- Car edges look clean overall
- Minor jagged pixels are acceptable if they don’t stand out at normal web size

**Fail if:**

- Strong white/black “halo” around the car
- Heavy jagged edges on roofline/doors
- Background color bleed (green/blue fringing) clearly visible

✅ **MVP threshold:** *No obvious halo/fringe when viewing at ~600px width.*

**3) Artifact control (weird leftovers)**

**Pass if:**

- No obvious leftover background blobs
- No random transparent patches around the car

**Fail if:**

- Background objects remain (trees, signs, people, license plate stand, reflections that look like blobs)
- Blocky artifacts or mask edges are clearly visible

✅ **MVP threshold:** *No distracting artifacts that would confuse a customer.*

**4) Composition quality (car on new background)**

**Pass if:**

- Car is fully inside the frame
- Car position looks reasonable (not floating, not cropped awkwardly)
- Background is applied correctly with no stretching that looks broken

**Fail if:**

- Car is floating with no grounding
- Car scale looks wildly wrong relative to background
- Cropping cuts off wheels/bumper in a bad way

✅ **MVP threshold:** *Car looks “placed” on the background without obvious* mistakes.

**5) Output resolution & format**

**Pass if:**

- Output image is not blurry/pixelated compared to input
- Minimum size works for typical listing view

**Fail if:**

- Output is noticeably softer than input
- Output too small for web display

✅ **MVP threshold (suggested):**

- Minimum output size: 1024 x 768 (or longer side ≥ 1024px)
- Format: PNG (if transparency needed) or WEBP/JPG (if composited onto background)

---

## Nice-to-Have Criteria (Optional)

### Shadow (if implemented)

**Pass if:**

- Soft shadow under car helps it sit on the ground
- Shadow doesn’t look like a dark blob

**Fail if:**

- Shadow direction/size is clearly wrong
- Shadow is harsh or disconnected from wheels

✅ **MVP threshold:** *Simple soft ground shadow is acceptable; realism is not required.*

### Watermark (if implemented)

**Pass if:**

- Watermark is visible but not blocking the car
- Consistent placement (e.g., bottom-right)

**Fail if:**

- Covers important details (logo/grille/price sticker area)
- Too strong or distracting

✅ **MVP threshold:** *Readable and consistent placement; subtle transparency.*

---

## Go / No-Go Rubric for MVP Demo

**Go ✅ if:**

- At least **80% of test images** pass the checklist (1–5)
- No more than **1 “Fail” category** per image (minor flaws allowed)
- The failures are explainable (e.g., “hard cases” like white car + white wall)

**No-Go ❌ if:**

- More than **20%** of outputs have obvious halos, missing parts, or big artifacts
- The output regularly looks “fake” or broken at normal listing size

### Suggested Test Set (for consistency)

Use 10–15 images covering common “hard” cases:

- White car on light background
- Dark car on dark background
- Complex background (trees, fence)
- Reflections on windows
- Cars with thin parts (mirrors, antennas)

### How to Review (Quick Procedure)

For each image:

1. View at **~600px wide** (typical listing)
2. Zoom to **100%** for edge check
3. Mark each category as **Pass / Minor Issue / Fail**
4. Record 1–2 notes if Fail (example: “halo around roofline”)

### Example: The Kia Sorento Sample Section (Add This)

You can append something like:

- **Sample:** 2019 Kia Sorento output
- **Intrinsic size:** 1024×768, WEBP, 410KB
- **MVP Review Notes (to fill):**
    - Cutout completeness: Pass / Minor / Fail
    - Edge quality: Pass / Minor / Fail
    - Artifacts: Pass / Minor / Fail
    - Composition: Pass / Minor / Fail
    - Resolution: Pass / Minor / Fail
    - Overall: Go / No-Go

---

## Sample Evaluation: 2019 Kia Sorento Output Image

*Figure 2: 2019 Kia Sorento Output Image*
![](/screenshots/2019-Kia-Sorento-output-image.png)

**Source image:** Dealer-style promotional photo\
**Output size:** 1024 × 768 (WEBP)\
**Rendered size:** ~573 × 430\
**Background:** Solid white with dealership banner overlay

### Quality Review (Based on MVP Criteria)

**1) Cutout Completeness — Pass**

- All major car components are intact (roof, mirrors, wheels, grille, bumper).
- No visible missing sections or holes in the body.
- Fine details (mirrors, roof rails) are preserved.

**✅ Meets MVP expectations**

**2) Edge Quality (Halo / Fringing) — Pass (Minor Issues Acceptable)**

- Overall edges are clean and well-defined.
- Minor softness around thin areas (roof rails, window edges) visible only at close inspection.
- No strong white/black halo visible at normal listing size.\
⚠️ Minor edge smoothing is acceptable for MVP.

**✅ Pass for MVP**

**3) Artifacts & Mask Errors — Pass**

- No background remnants (trees, pavement, shadows from original scene).
- No random transparent patches or blocky segmentation artifacts.
- Reflections on windows look natural and not broken by the mask.

**✅ Pass for MVP**

**4) Composition & Placement — Pass**

- Car is well-centered and fully within frame.
- Perspective and scale feel correct for a listing image.
- Car does not appear cropped or floating.\
ℹ️ Grounding shadow is absent, but acceptable at MVP stage.

**✅ Pass for MVP**

**5) Resolution & Visual Sharpness — Pass**

- Output resolution is sufficient for typical dealership listing views.
- No noticeable blur compared to expected web-quality automotive images.
- Compression artifacts are minimal and non-distracting.

**✅ Pass for MVP**

### Optional / Nice-to-Have Observations

**Shadow**

- No shadow present beneath the vehicle.
- Car appears slightly “flat” against white background, but still acceptable.\
➡️ **Nice-to-have improvement**, not required for MVP acceptance.

**Watermark / Branding**

- Dealer banner and branding are clearly visible and do not interfere with the car.
- Watermark placement does not obscure key vehicle features.

**✅ Acceptable for MVP demo purposes.**

---

## Overall MVP Verdict

**Overall Result: ✅ GO for MVP Demo**

**Rationale:**

- Image meets all core MVP quality criteria.
- Minor imperfections are only noticeable under close inspection.
- Output quality is comparable to existing online dealership listings.
- Demonstrates that background removal and replacement are viable for CarClinch’s use case.

This output is **“good enough”** to validate the concept with stakeholders and proceed with further RnD.

---

### Shadow Clarification (Corrected for MVP)

**Note on shadows:**
The sample Kia Sorento image contains **studio lighting and contact shading** from the original photography. This is **not a generated shadow** produced by the background-removal pipeline.

For MVP evaluation, the presence of a generated ground shadow will be treated as a **nice-to-have enhancement**, not a core acceptance requirement.

---

## Sample Evaluation: <Vehicle / Image ID>

**Input image type:** (dealer photo / phone photo / outdoor / studio)  
**Output size & format:** (e.g., 1024×768 WEBP)  
**Background used:** (white / uploaded background)

---

### Core MVP Quality Review

| # | Category | Status (Pass / Minor / Fail) | Notes |
|---|---------|-----------------------------|-------|
| 1 | Cutout completeness (car parts) |  |  |
| 2 | Edge quality (halo / fringing) |  |  |
| 3 | Artifacts & mask errors |  |  |
| 4 | Composition & placement |  |  |
| 5 | Resolution & visual sharpness |  |  |

---

### Optional / Nice-to-Have Enhancements

| Feature | Status (Not Present / Acceptable / Needs Improvement) | Notes |
|--------|--------------------------------------------------------|-------|
| Generated ground shadow |  |  |
| Watermark / branding |  |  |

---

### Overall MVP Verdict

| Decision | Rationale |
|----------|-----------|
| ✅ Go / ❌ No-Go | 1–2 concise bullets explaining the decision |



---

## Executive Summary

The proof of concept confirms that reliable car segmentation and background replacement can be achieved with minimal artifacts at standard web resolutions. The current implementation meets the MVP acceptance criteria, with optional enhancements, such as generated shadows, identified for future iterations.
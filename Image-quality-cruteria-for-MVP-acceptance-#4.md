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

Rendered size: 573 x 430 px
Rendered aspect ratio: 573:430
Intrinsic size: 1024 x 768 px
Intrinsic aspect ratio: 4:3
File size: 410 kB
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
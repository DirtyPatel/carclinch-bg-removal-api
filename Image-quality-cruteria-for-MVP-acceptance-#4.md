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

### Image Metadata: 

| Field                | Value                                      |
| -------------------- | ------------------------------------------ |
| Source image         | Dealer-style promotional photo             |
| Output size & format | 1024 × 768 (WEBP)                          |
| Rendered size        | ~573 × 430                                 |
| Background           | Solid white with dealership banner overlay |

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

## Core MVP Quality Review

| # | Category                        | Result   | Notes                                                                                                                                                                          |
| - | ------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Cutout completeness (car parts) | **Pass** | All major components intact (roof, mirrors, wheels, grille, bumper). No visible missing sections or holes. Fine details such as mirrors and roof rails preserved.              |
| 2 | Edge quality (halo / fringing)  | **Pass** | Edges are clean and well-defined. Minor softness around thin areas (roof rails, window edges) visible only at close inspection. No strong halo visible at normal listing size. |
| 3 | Artifacts & mask errors         | **Pass** | No background remnants, transparent gaps, or blocky segmentation artifacts. Reflections on windows remain natural and intact.                                                  |
| 4 | Composition & placement         | **Pass** | Car is well-centered and fully within frame. Perspective and scale are appropriate for a listing image. No awkward cropping or floating appearance.                            |
| 5 | Resolution & visual sharpness   | **Pass** | Output resolution is sufficient for dealership listings. No noticeable blur or distracting compression artifacts.                                                              |

---

## Optional / Nice-to-Have Enhancements

| Feature                 | Status      | Notes                                                                                                                               |
| ----------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Generated ground shadow | Not present | Car appears slightly flat against white background. Acceptable for MVP; realism enhancement planned for later iteration.            |
| Watermark / branding    | Acceptable  | Dealer banner and branding are visible and do not interfere with key vehicle features. Placement is consistent and non-distracting. |

---

## Overall MVP Verdict

| Decision              | Rationale                                                                                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ **GO for MVP Demo** | Image meets all core MVP quality criteria. Minor imperfections are only noticeable under close inspection. Output quality is comparable to existing online dealership listings and sufficient to validate the CarClinch use case. |
| **No-Go** ❌ | More than **20%** of outputs have obvious halos, missing parts, or big artifacts. The output regularly looks “fake” or broken at normal listing size |

---

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

---

## Sample Evaluation: 2019 Kia Sorento Output Image

*Figure 2: 2019 Kia Sorento Output Image*
![](/screenshots/2019-Kia-Sorento-output-image.png)

### Image Metadata

| Field                | Value                                      |
| -------------------- | ------------------------------------------ |
| Source image         | Dealer-style promotional photo             |
| Output size & format | 1024 × 768 (WEBP)                          |
| Rendered size        | ~573 × 430                                 |
| Background           | Solid white with dealership banner overlay |


### Core MVP Quality Review

| # | Category                        | Result   | Notes                                                                                                                                                                          |
| - | ------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Cutout completeness (car parts) | **Pass** | All major components intact (roof, mirrors, wheels, grille, bumper). No visible missing sections or holes. Fine details such as mirrors and roof rails preserved.              |
| 2 | Edge quality (halo / fringing)  | **Pass** | Edges are clean and well-defined. Minor softness around thin areas (roof rails, window edges) visible only at close inspection. No strong halo visible at normal listing size. |
| 3 | Artifacts & mask errors         | **Pass** | No background remnants, transparent gaps, or blocky segmentation artifacts. Reflections on windows remain natural and intact.                                                  |
| 4 | Composition & placement         | **Pass** | Car is well-centered and fully within frame. Perspective and scale are appropriate for a listing image. No awkward cropping or floating appearance.                            |
| 5 | Resolution & visual sharpness   | **Pass** | Output resolution is sufficient for dealership listings. No noticeable blur or distracting compression artifacts.                                                              |

### Optional / Nice-to-Have Enhancements

| Feature                 | Status      | Notes                                                                                                                               |
| ----------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Generated ground shadow | Not present | Car appears slightly flat against white background. Acceptable for MVP; realism enhancement planned for later iteration.            |
| Watermark / branding    | Acceptable  | Dealer banner and branding are visible and do not interfere with key vehicle features. Placement is consistent and non-distracting. |

---

## Overall MVP Verdict

| Decision              | Rationale                                                                                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ **GO for MVP Demo** | Image meets all core MVP quality criteria. Minor imperfections are only noticeable under close inspection. Output quality is comparable to existing online dealership listings and sufficient to validate the CarClinch use case. |

---

### Shadow Clarification (MVP Scope)

| Item             | Description                                                                          |
| ---------------- | ------------------------------------------------------------------------------------ |
| Shadow source    | Studio lighting and contact shading from original photography                        |
| Generated shadow | **Not present**                                                                      |
| MVP requirement  | Generated ground shadow treated as **nice-to-have**, not a core acceptance criterion |


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
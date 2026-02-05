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
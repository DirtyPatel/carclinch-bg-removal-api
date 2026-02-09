### 1. Purpose of This Document

The purpose of this document is to look at different technical options for building a car image background removal and replacement MVP. The goal is to choose an option that makes sense for a student capstone project by balancing cost, difficulty, learning value, and how easy it is to demo.

### 2. Problem Statement

The project focuses on automating car image background removal and replacement for sales listings. Doing this manually or relying on free or limited third-party tools does not scale well and can become costly over time. Because of this, the team needs to choose a technical approach that can support a working MVP by the end of the academic term.

### 3. Context and Constraints

From the initial client discussions, it was made clear that the solution is expected to be a working MVP or prototype, not a full production-ready system. Cost was identified as an important concern, while performance only needs to be “reasonable” for demonstration purposes. Scalability and deeper system integrations were mentioned as future considerations and are not required for the MVP.

The client did not enforce a specific technology stack and instead asked the team to research possible approaches and recommend a solution based on feasibility and trade-offs.

### 4. Evaluation Criteria


* How complex the solution is to build

* Cost and infrastructure requirements

* Quality and accuracy of the output images

* How suitable the option is for an MVP and demo

* Flexibility for future improvements


### 5. Option 1 – Open-Source Machine Learning Model (U²-Net Style)


This option uses a pre-trained open-source background removal model, such as U²-Net. The model would be set up as a simple inference pipeline where a user uploads a car image and receives the same image with the background removed. This approach also allows future features like background replacement or watermarking.

#### Pros

* No licensing fees or per-request API costs

* Full control over how images are processed

* Easy to customize or extend later

* High learning value for the team

### Cons

* Requires machine learning setup and testing

* May require GPU resources, which can increase cost

* More complex to deploy compared to a managed API

* Accuracy may vary depending on image quality

Although this option is more technically challenging. It avoids long-term dependence on paid third-party services and provides strong learning value. Since this is an MVP, the risks related to setup and accuracy are acceptable as long as the core functionality works.

### 6. Option 2 – Third-Party Background Removal API


This option uses an external background removal API. Images are sent to the service, and the processed images are returned to the application.

### Pros

* Very quick to implement

* High and consistent image quality

* Minimal infrastructure setup

### Cons

* Ongoing usage and subscription costs

* Dependence on a third-party service

* Limited control over image processing

* Lower learning value for the team

Discussion

While this option is easier to implement and produces strong results, it goes against the project’s cost constraints and the client’s goal of reducing reliance on paid tools. It is more suitable for quick demos rather than a research-focused capstone project.



### 7. Comparison Summary

| Criteria        | Open-Source ML | Third-Party API |
|-----------------|---------------|-----------------|
| Complexity      | Medium–High   | Low             |
| Cost Control    | High          | Low–Medium      |
| Accuracy        | Medium–High   | High            |
| Demo Readiness  | Medium        | High            |
| Flexibility     | High          | Low             |


### 8. Recommendation

Based on the comparison, the team recommends Option 1: Open-Source Machine Learning (U²-Net Style) for the MVP. Even though it requires more setup and may involve GPU costs, this option offers better cost control, flexibility, and learning value.

Since the goal is to deliver a working MVP by the end of the term, using an open-source model allows the team to demonstrate core functionality while keeping full control over the solution. It also makes future improvements easier once feasibility has been proven.

9. Next Steps

-   Test open-source background removal models

-   Compare CPU and GPU inference options

-   Build a simple inference (using the model ) workflow for the MVP

-   Monitor performance and cost during testing



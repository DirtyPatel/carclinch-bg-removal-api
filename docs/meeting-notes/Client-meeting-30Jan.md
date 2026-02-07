
### 1. Project Direction & Scope

At the core, he wants to **automate car image background removal and replacement** so he’s not stuck relying on limited or paid third-party tools. Manual edits and free plans don’t scale well, especially for sales listings

Main use case to focus on first?
- Upload a car image
- Remove the background
- Replace it with a clean background

Nice to have: 
- Add a realistic Shadow and Watermark 


### 2. Infrastructure & Tech Preferences

**Preferred tech stack or cloud?**  
No strict preference. He’s open to **any language or stack**, as long as it works.  

Azure is a strong candidate, especially for:

- AI models
    
- Experimentation
    
- Cost tracking
    

**Any integrations needed right now?**  
Nope. This should be a **standalone application** for now. Integration can come later.

**Prototype vs production?**  
Definitely leaning toward a **functional prototype / MVP**, not a full production system.
    

### 3. API Design & Integration

**How would it fit into his workflow later?**  
Eventually, it could be called as an API from CarAxios or another system, but **not required right now**.

**Processing style?**  
On-demand processing makes the most sense:

- Upload image
    
- Get processed image back
    

Batch processing could be explored later if needed.

**Key concerns?**

- **Cost** (big one)
    
- Performance should be “reasonable,” not enterprise-level
    
- Scalability is a future concern, not day one
    

### 4. Security & Access

- **Expected security level?**  
	Basic but sensible:

- API keys or tokens are more than enough for now
    

- **Compliance or data constraints?**  
	Nothing specific mentioned. Images are car photos, so no sensitive personal data involved.
    

### 5. Deliverables & Expectations

**Most valuable deliverables?**

- R&D findings (model options, tools, feasibility)
    
- A working **background removal MVP**
    
- Clear **cost analysis**
    
- Simple documentation or demo 

### 6. Timeline & Communication

**Immediate next step**  
- **Option analysis + R&D**  

This includes:

- Exploring Azure AI or open-source models
    
- Testing what can be trained vs reused
    
- Comparing cost vs quality
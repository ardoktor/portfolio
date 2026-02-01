mulakat.pro is an AI-assisted interview preparation system
designed to identify skill gaps, structure learning paths,
and simulate real interview expectations.

The core problem it solves is not “mock interviews” —
it’s decision ambiguity:
candidates don’t know what to study, in what order,
or how close they are to being interview-ready.
I designed mulakat.pro as a backend-first system that analyzes
resumes and job requirements, extracts structured signals,
and maps them into actionable preparation steps.

The platform focuses on:
• gap detection between candidate profiles and job roles
• structured topic breakdowns instead of generic advice
• AI-assisted evaluation with explainable outputs
System Design & Architecture
The system is built around retrieval-augmented generation (RAG)
and structured reasoning pipelines.

Job descriptions, resumes, and domain knowledge are processed
as retrievable sources rather than raw prompts.
This allows the system to:
• ground responses in actual requirements
• reduce hallucinations
• generate traceable, section-aware feedback
Agent-like flows are used to separate concerns:
analysis, evaluation, feedback generation,
and preparation guidance are handled as distinct steps
instead of a single LLM call.
What I Built
• Resume and job-post parsing pipelines
• Skill and requirement extraction logic
• Gap analysis and readiness estimation
• Structured interview topic generation
• Backend APIs for evaluation and progress tracking
• Deployment and iteration based on real user feedback
Why This Project Matters
mulakat.pro reflects how I approach AI products in general:
not as chat interfaces, but as decision-support systems.

The goal is not to “sound smart”,
but to guide users through complex processes
with clarity, structure, and measurable progress.
This same architectural mindset appears across my other products:
domain-aware retrieval, workflow-driven AI,
and backend systems designed for real-world use.
Tech Focus (optional compact block)
Python, Django, FastAPI
LLM integrations (OpenAI APIs)
Retrieval-Augmented Generation (RAG)
Structured outputs & evaluation pipelines
PostgreSQL, vector search
Backend-first product architecture
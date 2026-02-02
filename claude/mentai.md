✅ Block 1 — Narrative Card

The Problem (Narrative)
Most learning tools treat users as stateless — forgetting context, goals, and progress over time. MentAI targets continuity: building a system that remembers where a learner is, what they struggle with, and what they need next — without turning everything into a chat history.

MentAI was my first end-to-end product where I combined backend engineering, AI-assisted reasoning, and product thinking into one system. More importantly, it introduced me to entrepreneurship and real-world product development through building as a team and engaging early startup communities.

✅ Block 2 — Technical Card

Continuity as a Systems Constraint (Technical Deep Dive)

Constraints I designed for

Stateful guidance (progress, goals, patterns) on top of stateless execution (serverless)

Unstructured user input → structured signals

Repeatable loop: input → analysis → guidance → action → feedback

System loop

input -> normalize -> extract signals -> update user_state
     -> generate guidance -> assign actions -> collect feedback

✅ Block 3 — Narrative Card

System Philosophy (Narrative)
MentAI is not a content platform. It is a guidance system. The product is built around persistence: user history, feedback, and actions are treated as structured, evolving state rather than disposable input. Each interaction feeds the next one. The goal is not one good answer — it’s sustained guidance over time.

✅ Block 4 — Technical Card

State Model (minimal but real) (Technical Deep Dive)

Core entities

user_profile (stable)

goals (explicit targets)

daily_inputs (mood/energy/notes)

actions_tasks (assigned + completed)

progress_signals (habit streaks, friction points)

weekly_summary (compressed memory)

Why structured state beats raw chat

Queryable (progress tracking)

Explainable (why this suggestion?)

Safer outputs (less randomness)

✅ Block 5 — Narrative Card

Core Capabilities (Narrative)

Long-Term User Modeling: Reflections and feedback are stored as structured data to enable progress tracking and adaptive guidance.

Structured Guidance & Workflows: Daily prompts, reflection questions, task suggestions, and periodic evaluations — designed to be actionable, not motivational filler.

AI-Assisted Reasoning: LLMs are used as reasoning components to summarize input, extract signals, and shape future guidance through controlled pipelines.

Backend & Cloud Architecture: Event-driven logic powers asynchronous processing, scheduled nudges, and background evaluations.

✅ Block 6 — Technical Card (your “response.json” vibe)

Example API Response (MentAI Guidance Output) (Technical Deep Dive)

{
  "success": true,
  "data": {
    "markdown": "## Today’s Focus\n- 1 task...\n\n## Why this matters\n...",
    "html": "<h2>Today’s Focus</h2><ul>...</ul>",
    "metadata": {
      "title": "MentAI — Daily Guidance",
      "description": "Personalized daily guidance generated from structured user state",
      "confidence": 0.82,
      "sources": ["user_state", "weekly_summary", "goal_model_v1"]
    },
    "actions": [
      {
        "id": "task_7f2a",
        "label": "10-minute deep work block",
        "type": "timebox",
        "difficulty": "easy",
        "why": "low energy day + high avoidance pattern"
      }
    ],
    "links": {
      "internal": ["/progress", "/weekly-review", "/settings"],
      "external": []
    },
    "stats": {
      "fetchTimeMs": 241,
      "analysisTimeMs": 138,
      "llmTimeMs": 912,
      "totalTimeMs": 1291
    }
  }
}


Design note: this format is deliberate — the UI can render markdown/html, while product logic relies on actions + metadata.

✅ Block 7 — Narrative Card

Architecture (Narrative)
MentAI was built backend-first to validate the system logic before UI expansion. The product relies on structured user state + event-driven processing so the platform can maintain continuity while scaling and iterating fast.

✅ Block 8 — Technical Card

Google Cloud Functions — Event Driven Layer (Technical Deep Dive)

Why Cloud Functions

Async processing (don’t block UX)

Scheduled jobs (daily nudges / weekly review)

Stateless compute + stateful DB = scalable pattern

Function examples

on_daily_input_submitted(user_id)

normalize text → extract signals → update state → generate guidance

nightly_scheduler()

check inactive users → send “gentle nudge”

weekly_review_generator()

compress the week → write weekly_summary (memory)

✅ Block 9 — Narrative Card

What Didn’t Work & What I Learned (Narrative)
Not everything worked. The hardest part wasn’t generating content — it was sustaining engagement, balancing structure with flexibility, and building a real feedback loop early. MentAI taught me that a well-designed system doesn’t automatically create product-market fit. Distribution, messaging, and iteration speed matter as much as architecture.

MentAI also introduced me to entrepreneurship: we built as a team, grew an Instagram presence, and participated in the Karşıyaka Girişimcilik Merkezi collective. Even though it didn’t proceed as a full startup, it shaped my product instincts and directly influenced how I later built mulakat.pro and ConsulDent.

✅ Block 10 — Technical Card

Iteration Notes & Trade-offs (Technical Deep Dive)

Over-structured early UX → users felt “boxed in”
✅ fix: allow “free input” + structured extraction later

Too much generation → inconsistent tone and verbosity
✅ fix: templates + structured outputs + validation

Hard to measure progress
✅ fix: define a few core signals (streak, friction, task completion)
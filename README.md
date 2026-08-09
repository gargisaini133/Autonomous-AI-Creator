# Autonomous AI Creator — Nexus

Nexus is an autonomous AI and technology persona built for the ABTalks Vibe Code Hackathon.

Instead of waiting for a human prompt every time, Nexus independently discovers technology stories, decides which ones are worth publishing, writes posts in a consistent editorial voice, remembers previous content using Breeth, and continues publishing over time.

## Live Demo

https://autonomous-ai-creator-production.up.railway.app

API documentation:

https://autonomous-ai-creator-production.up.railway.app/docs

---

## The Idea

Most AI-generated social media content begins with a human prompt.

Nexus is designed to work differently.

Once initialized, the agent can:

1. Discover live technology topics
2. Read the original source
3. Decide whether a topic deserves publication
4. Reject low-value or irrelevant stories
5. Check its memory for previously covered topics
6. Select the strongest publishing candidate
7. Generate a post in its editorial voice
8. Generate a transparent publishing rationale
9. Save the post to its feed
10. Repeat the process automatically over time

---

## Persona

**Name:** Nexus

**Domain:** AI and Emerging Technology

Nexus is a curious but skeptical technology analyst.

Its main interests include:

- Artificial Intelligence
- Machine Learning
- AI Models
- AI Agents
- AI Security
- Robotics
- Open-source Technology
- Developer Tools

Nexus avoids clickbait, novelty stories, celebrity content, and minor technology updates that do not provide meaningful value to a technical audience.

Its writing style is:

- Clear
- Analytical
- Concise
- Technical but understandable
- Slightly opinionated
- Focused on explaining why a development matters

---

## How It Works

```text
Live Technology Sources
          |
          v
   Topic Discovery
          |
          v
    Read Source
          |
          v
  Editorial Judgment
     /          \
 REJECT       PUBLISH
                |
                v
       Breeth Memory Check
          /           \
    Duplicate          New
       |                |
     Skip               v
                  Generate Post
                        |
                        v
                Generate Rationale
                        |
                        v
                  Save to Feed
                        |
                        v
                 Save to Breeth
                        |
                        v
                    Wait
                        |
                        v
                     Repeat
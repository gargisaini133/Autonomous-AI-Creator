# AI Usage Log

## August 8, 2026

### Project Planning
Used ChatGPT to understand the Autonomous AI Creator problem statement and design the initial system architecture.

### Backend Setup
Used ChatGPT to:
- Set up a FastAPI project
- Create `POST /api/agent/init`
- Create `GET /api/agent/feed`
- Generate unique agent IDs
- Test API endpoints using FastAPI Swagger docs

### Database
Used ChatGPT to:
- Set up SQLite
- Create an `agents` table
- Create a `posts` table
- Create a `candidates` table
- Store initialized agents
- Store feed posts
- Store accepted and rejected topic candidates

### Topic Discovery
Used ChatGPT to:
- Connect the project to the Hacker News API
- Fetch live technology stories
- Debug HTTP requests
- Test live topic discovery

### Editorial Judgment
Used ChatGPT to:
- Build an initial keyword-based topic scoring system
- Implement `PUBLISH` and `REJECT` decisions
- Fix a keyword-matching bug where the word "faith" incorrectly matched "AI"
- Store editorial decisions for future evaluation

### Development Style
The project was built incrementally with small changes and testing after each feature.
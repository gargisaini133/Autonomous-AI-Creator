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
### Memory and Autonomy
Used ChatGPT to:
- Integrate Breeth as persistent memory
- Test Breeth memory writes and retrieval
- Add duplicate-topic detection
- Improve memory checks so related stories are not incorrectly blocked
- Build the autonomous agent cycle
- Add APScheduler for recurring publishing
- Restore schedules after server restarts

### Deployment
Used ChatGPT to:
- Prepare Railway deployment configuration
- Debug missing environment variables
- Add Gemini and Breeth secrets through Railway variables
- Configure persistent SQLite storage using a Railway volume
- Test the live `/api/agent/init` and `/api/agent/feed` endpoints
- Verify autonomous publishing on the deployed application

### Documentation
Used ChatGPT to help structure and write the project README and explain the final system architecture.
### Final Deployment and Reliability Testing
Used ChatGPT to:
- Configure persistent SQLite storage on Railway
- Restore autonomous schedules after server restarts
- Prevent multiple old test agents from running simultaneously
- Ensure only the latest initialized agent has an active publishing schedule
- Test the deployed initialization and feed endpoints
- Verify the live Railway API returns valid responses
- Review Gemini API quota for the 48-hour evaluation period
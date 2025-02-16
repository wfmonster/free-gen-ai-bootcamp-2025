
### WEEK 1 TODOS

Week 1 Challenge
- [x] Level 0: Create the Backend Technical Specification
- [x] Level 0: Create the Frontend Technical Specification
- [x] Level 1: Implement the missing API endpoints
    - [x] GET /groups/:id/words/raw
    - [x] POST /study_sessions/:id/review
    - [x] POST /study_sessions
- [ ] - test endpoints with curl.
- [ ] - test endpoints with frontend.


Testing endpoints with curl: 


### groups.py Routes
```bash
# GET /groups
curl -X GET "http://127.0.0.1:5000/groups?page=1&sort_by=name&order=asc"

# GET /groups/:id
curl -X GET "http://127.0.0.1:5000/groups/1"

# GET /groups/:id/words
curl -X GET "http://127.0.0.1:5000/groups/1/words?page=1&sort_by=kanji&order=asc"

# GET /groups/:id/words/raw
curl -X GET "http://127.0.0.1:5000/api/groups/1/words/raw"

# GET /groups/:id/study_sessions
curl -X GET "http://127.0.0.1:5000/groups/1/study_sessions?page=1&sort_by=startTime&order=desc"
```


### dashboard.py Routes
```bash
# GET /dashboard/recent-session
curl -X GET "http://127.0.0.1:5000/dashboard/recent-session"

# GET /dashboard/stats
curl -X GET "http://127.0.0.1:5000/dashboard/stats"
``` 


### study_activities.py Routes
```bash
# GET /api/study-activities
curl -X GET "http://127.0.0.1:5000/api/study-activities"

# GET /api/study-activities/:id
curl -X GET "http://127.0.0.1:5000/api/study-activities/1"

# GET /api/study-activities/:id/sessions
curl -X GET "http://127.0.0.1:5000/api/study-activities/1/sessions?page=1&per_page=10"

# GET /api/study-activities/:id/launch
curl -X GET "http://127.0.0.1:5000/api/study-activities/1/launch"
```


### study_sessions.py Routes
```bash
# POST /study-sessions
curl -X POST "http://127.0.0.1:5000/study-sessions" \
  -H "Content-Type: application/json" \
  -d '{"group_id": 1, "study_activity_id": 1}'

# GET /api/study-sessions
curl -X GET "http://127.0.0.1:5000/api/study-sessions?page=1&per_page=10"

# GET /api/study-sessions/:id
curl -X GET "http://127.0.0.1:5000/api/study-sessions/1"

# POST /study-sessions/:id/review
curl -X POST "http://127.0.0.1:5000/study-sessions/1/review" \
  -H "Content-Type: application/json" \
  -d '{"word_id": 1, "correct": true, "reviews": [{"word_id": 1, "correct": true}]}'

# POST /api/study-sessions/reset
curl -X POST "http://127.0.0.1:5000/api/study-sessions/reset"
```


### words.py Routes
```bash
# GET /words
curl -X GET "http://127.0.0.1:5000/words?page=1&sort_by=kanji&order=asc"

# GET /words/:id
curl -X GET "http://127.0.0.1:5000/words/1"
```

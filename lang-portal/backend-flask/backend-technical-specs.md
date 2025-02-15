# Technical Specs


## Business Goal: 

A language learning school wants to build a prototype of learning portal which will act as three things
- Inventory of possible vocabulary that can be learned
- Act as a  Learning record store (LRS), providing correct and wrong score on practice vocabulary
- A unified launchpad to launch different learning apps


## Business Requirements

We are building a language portal that acts as a launch pad for study activities.
But also lets us browse our vocabulary library.
- Have an inventory of words in the target language. 
- Have a group of words in thematic categories.(e.g. animals, foods, colors, places, etc.)
- We want to store study sessions(e.g. Words right and wrong. )
- The database will be built using Sqlite3.
- The API will be built using Flask.
- The API will always return JSON.
- There will be no authentication or authorization.
- Everything will be treated as a single user.

## API Endpoints

### Routes

#### GET /api/words (list of words)
    - return a list of words, paginated with 100 words at a time
    - review statistics 

    page: Page number (default: 1)
    sort_by: Sort field ('kanji', 'romaji', 'english', 'correct_count', 'wrong_count') (default: 'kanji')
    order: Sort order ('asc' or 'desc') (default: 'asc')


#### ExampleResponse Json
```json
{
  "current_page": 1,
  "total_pages": 3,
  "total_words": 124,
  "words": [
    {
      "correct_count": 0,
      "english": "to give",
      "id": 26,
      "kanji": "\u3042\u3052\u308b",
      "romaji": "ageru",
      "wrong_count": 0
    },
    {
      "correct_count": 0,
      "english": "good",
      "id": 61,
      "kanji": "\u3044\u3044",
      "romaji": "ii",
      "wrong_count": 0
    },
    ...
  ]
}
```


#### GET /api/groups (list of groups)
    - returns a paginated list of word groups with word counts. 
    
#### GET /api/groups/:id (individual group details)
    - Get words from a specific group (This is intended to be used by target apps)

    page: Page number (default: 1)
    sort_by: Sort field ('name', 'words_count') (default: 'name')
    order: Sort order ('asc' or 'desc') (default: 'asc')

#### POST /api/study-sessions (create study session)
    - create a new study session for a group

#### POST /api/study-sessions/:id/review (add words to study session)
    - add words to a study session
    - return the study session id

    group_id: ID of the group to study (required)
    study_activity_id: ID of the study activity (required)


# API Endpoints

## DASHBOARD 
--- 
#### GET /api/dashboard/recent-session

##### JSON Response
```json
{
  "id": 123,
  "group_id": 456,
  "created_at": "2025-02-08T17:20:23-05:00",
  "study_activity_id": 789,
  "group_id": 456,
  "group_name": "Basic Greetings"
}
```

#### GET /api/dashboard/study-progress
Returns study progress statistics. Please note that the frontend will determine progress bar basedon total words studied and total available words.

##### JSON Response
```json
{
  "total_words_studied": 3,
  "total_available_words": 124,
}
```

#### GET /api/dashboard/quick-stats
Returns quick overview statistics.
s
##### JSON Response
```json
{
  "success_rate": 80.0,
  "total_study_sessions": 4,
  "total_active_groups": 3,s
  "study_streak_days": 4
}
```

## WORDS 
--- 

#### GET /api/words 
  - pagination with 100 items per page
  - word parts are needed to use the typing tutor activity. 

##### JSON Response
```json
{
  "items": [
    {
      "japanese": "こんにちは",
      "romaji": "konnichiwa",
      "english": "hello",
      "correct_count": 5,
      "wrong_count": 2
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_items": 500,
    "items_per_page": 100
  }
}
```

####GET /api/words/:id 

##### JSON Response
```json
{
  "japanese": "こんにちは",
  "romaji": "konnichiwa",
  "english": "hello",
  "stats": {
    "correct_count": 5,
    "wrong_count": 2
  },
  "groups": [
    {
      "id": 1,
      "name": "Basic Greetings"
    }
  ]
}
```


## GROUPS 
--- 

- GET /api/groups
  - pagination with 100 items per page

##### JSON Response
```json
{
  "items": [
    {
      "id": 1,
      "name": "Basic Greetings",
      "word_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 10,
    "items_per_page": 100
  }
}
```

#### GET /api/groups/:id

##### JSON Response
```json
{
  "id": 1,
  "name": "Basic Greetings",
  "stats": {
    "total_word_count": 20
  }
}
```

#### GET /api/groups/:id/words

##### JSON Response
```json
{
  "items": [
    {
      "japanese": "こんにちは",
      "romaji": "konnichiwa",
      "english": "hello",
      "correct_count": 5,
      "wrong_count": 2
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 20,
    "items_per_page": 100
  }
}
```

#### GET /api/groups/:id/study-sessions

##### JSON Response
```json
{
  "items": [
    {
      "id": 123,
      "activity_name": "Vocabulary Quiz",
      "group_name": "Basic Greetings",
      "start_time": "2025-02-08T17:20:23-05:00",
      "end_time": "2025-02-08T17:30:23-05:00",
      "review_items_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 5,
    "items_per_page": 100
  }
}
```


## STUDY ACTIVITIES 
--- 

#### GET /api/study-activities/:id 

##### JSON Response
```json
{
  "id": 1,
  "name": "Vocabulary Quiz",
  "thumbnail_url": "https://example.com/thumbnail.jpg",
  "description": "Practice your vocabulary with flashcards"
}
```

#### GET /api/study-activities/:id/study-sessions
- pagination with 100 items per page

##### JSON Response
```json
{
  "items": [
    {
      "id": 123,
      "activity_name": "Vocabulary Quiz",
      "group_name": "Basic Greetings",
      "start_time": "2025-02-08T17:20:23-05:00",
      "end_time": "2025-02-08T17:30:23-05:00",
      "review_items_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_items": 100,
    "items_per_page": 20
  }
}
```

#### POST /api/study-activities/
  - required request params: 
    - group_id (int)
    - study_activity_id (int)

##### JSON Response
```json
{ 
  "id": 2, 
  "group_id": 1 
}
```


## STUDY SESSIONS 
--- 

#### GET /api/study-sessions
  - pagination with 100 items per page

##### JSON Response
```json
{
  "items": [
    {
      "id": 123,
      "activity_name": "Vocabulary Quiz",
      "group_name": "Basic Greetings",
      "start_time": "2025-02-08T17:20:23-05:00",
      "end_time": "2025-02-08T17:30:23-05:00",
      "review_items_count": 20
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_items": 100,
    "items_per_page": 100
  }
}

```

#### GET /api/study-sessions/:id

##### JSON Response
```json
{
  "id": 123,
  "activity_name": "Vocabulary Quiz",
  "group_name": "Basic Greetings",
  "start_time": "2025-02-08T17:20:23-05:00",
  "end_time": "2025-02-08T17:30:23-05:00",
  "review_items_count": 20
}
```

#### GET /api/study-sessions/:id/words

##### JSON Response
```json
{
  "items": [
    {
      "japanese": "こんにちは",
      "romaji": "konnichiwa",
      "english": "hello",
      "correct_count": 5,
      "wrong_count": 2
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 1,
    "total_items": 20,
    "items_per_page": 100
  }
}
```

#### POST /study-sessions/:id/review

Request Params
- id (study_session_id) integer
- word_id integer
- correct boolean

##### Request Payload
```json
{
  "correct": true
}
```

##### JSON Response
```json
{
  "success": true,
  "word_id": 1,
  "study_session_id": 123,
  "correct": true,
  "created_at": "2025-02-08T17:33:07-05:00"
}
```

#### GET /api/study-sessions/:id/words/:word_id/review 

##### Request Params
- id (study_session_id) integer
- word_id integer
- correct boolean

##### Request Payload
```json
{
  "correct": true
}
```

##### JSON Response
```json
{
  "success": true,
  "word_id": 1,
  "study_session_id": 123,
  "correct": true,
  "created_at": "2025-02-08T17:33:07-05:00"
}
```

## SETTINGS 
--- 

####POST /api/settings/reset-history

##### JSON Response
```json
{
  "success": true,
  "message": "Study history has been reset"
}
```

####POST /api/settings/full-reset

##### JSON Response
```json
{
  "success": true,
  "message": "System has been fully reset"
}
```



# Database Schema
---

We have the following tables:

| words |||Stores individual Japanese vocabulary words.|
|--------|------|-------|-------|
| id | int | Primary Key | Unique identifier for each word |
| kanji | string | Required |The word written in Japanese kanji |
| romaji | string | Required |The word written in Japanese romaji |
| english | string | Required |The word written in English |
| parts | json | Required | Word components stored in JSON format |


| groups |||Manages collections of words.|
|--------|------|-------|-------|
| id | int | Primary Key | Unique identifier for each group |
| name | string | Required | The name of the group |
| words_count | int | Default: 0 | Counter cache for the number of words in the group|      


| word_groups |||join-table enabling many-to-many relationship between words and groups.|
|--------|------|-------|-------|
| id | int | Primary Key | Unique identifier for each join |
| word_id | int | Foreign Key | References words.id |
| group_id | int | Foreign Key | References groups.id |


| study_activities |||Defines different types of study activities available|
|--------|------|-------|-------|
| id | int | Primary Key | Unique identifier for each activity |
| name | string | Required | Name of the activity (e.g., "Flashcards", "Quiz") |
| url | string | Required | The full URL of the study activity |


| study_sessions |||Records individual study sessions.|
|--------|------|-------|-------|
| id | int | Primary Key | Unique identifier for each session |
| group_id | int | Foreign Key | References groups.id |
| study_activity_id | int | Foreign Key | References study_activities.id |
| created_at | timestamp | Default: Current Time | When the session was created |


| word_review_items |||Tracks individual word reviews within study sessions.|
|--------|------|-------|-------|
| id | int | Primary Key | Unique identifier for each review |
| word_id | int | Foreign Key | References words.id|
| study_session_id | int | Foreign Key | References study_sessions.id |
| correct | boolean | Required | Whether the answer was correct |
| created_at | timestamp | Default: Current Time | When the review occurred |


### Relationships

- word belongs to groups through  word_groups
- group belongs to words through word_groups
- session belongs to a group
- session belongs to a study_activity
- session has many word_review_items
- word_review_item belongs to a study_session
- word_review_item belongs to a word

### Design Notes

- All tables use auto-incrementing primary keys
- Timestamps are automatically set on creation where applicable
- Foreign key constraints maintain referential integrity
- JSON storage for word parts allows flexible component storage
- Counter cache on groups.words_count optimizes word counting queries


### Background Tasks 
--- 
Listing out possible tasks we need for the lang portal.

#### Intialize the database
This task will initialize the sqlite database called `words.db

#### Migrate Database
This task will run a series of migrations sql files on the database

Migrations live in the `migrations` folder. The migration files will be run in order of their file name. The file names should looks like this:
```
0001_init.sql
0002_create_words_table.sql
```

#### Seed Data
This task will import json files and transform them into target data for our database.
All seed files live in the `/seed` folder.

In our task we should have DSL to specific each seed file and its expected group word name.

```json
[
  {
    "kanji": "払う",
    "romaji": "harau",
    "english": "to pay",
  },
  ...
]
```








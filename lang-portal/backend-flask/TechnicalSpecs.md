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
    - return a list of words, 100 words at a time
    - pagination 
    - review statistics 

    page: Page number (default: 1)
    sort_by: Sort field ('kanji', 'romaji', 'english', 'correct_count', 'wrong_count') (default: 'kanji')
    order: Sort order ('asc' or 'desc') (default: 'asc')


#### Response Json
```json
{
  "data": [
    {
      "id": 1,
      "kanji": "犬",
      "romaji": "inu",
      "english": "dog",
      "group_id": 1
    },
    {
      "id": 2,
      "kanji": "猫", 
      "romaji": "neko",
      "english": "cat",
      "group_id": 1
    },
    {
      "id": 3,
      "kanji": "鳥",
      "romaji": "tori", 
      "english": "bird",
      "group_id": 1
    }
  ],
  "pagination": {
    "total": 325,
    "per_page": 100,
    "current_page": 1,
    "total_pages": 4
  }
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



## Database Schema:

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
All tables use auto-incrementing primary keys
Timestamps are automatically set on creation where applicable
Foreign key constraints maintain referential integrity
JSON storage for word parts allows flexible component storage
Counter cache on groups.words_count optimizes word counting queries
















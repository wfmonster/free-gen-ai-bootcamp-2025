# Frontend Technical Specs

## Overview

The frontend is a React application that uses the Material-UI library for styling.

## Pages

### Dashboard `/dashboard`

#### Purpose
The dashboard page displays a summary of the user's study progress and act as a default landing page
when the user visits the web-app.

#### Components 
It contains the following sections:
- Last Study Session
    - shows last activity used. 
    - shows when the last activity was used.
    - summarizes wrong vs correct from last activity.
    - has a link to the group

- Study Progress 
    - total words studied e.g. 19/124
        - across all study sessions show the total words studied out of all possible words in our database. 
    - display a mastery progress e.g. 12% 

- Quick Stats
    - success rate e.g. 80%
    - total study sessions e.g. 12
    - total active groups e.g. 3
    - study streak  e.g. 4 days


- Start Studying Button
    - Goes to the study activities page. 

We will need the following API endpoints:
- GET /dashboard/last-study-session
- GET /dashboard/study-progress
- GET /dashboard/quick-stats

### Study Activities `/study-activities`

#### Purpose
The purpose of this page is to displays a collection of study activities
with a thumbnail and a name, to either launch or view the study activity.

#### Components
Study Activity Card
    - Shows a Thumbnail of the study activity
    - Name of the study activity
    - Launch Button to take us to the launch page
    - View Page to view more information about past study sessions for this study activity.

#### API Endpoints

GET /study-activities
    - pagination 


### Study Activities Show `/study-activities/:id`

#### Purpose
The purpose of this page is to display more information about a specific study activity
and its past study sessions.

#### Components
- Name of the study activity
- Thumbnail of the study activity
- Description of the study activity
- Launch Button 
- Paginated List of Past study sessions
    - id 
    - activity name 
    - group name 
    - start time
    - end time (inferred by the last word_review_item submitted.)
    - number of review items. 

#### API Endpoints

GET /api/study-activities/:id
GET /api/study-activities/:id/study-sessions


### Study Activities Launch `/study-activities/:id/launch`

#### Purpose
The purpose of this page is to launch a specific study activity.

#### Components
- Name of the study activity
- Launch Form 
    - select field for group
    - launch now button

## Behavior
After the form is submitted, a new tab opens with the study activity, based
on its URL provided in the database.

Also, after submitting the form, the page will redirect to the study session
show page.

#### API Endpoints

POST /api/study-activities/


### Words `/words`

#### Purpose
The purpose of this page is to display all the words in the database.

#### Components
- Paginated List of Words
Columns
    - Japanese
    - Romaji
    - English 
    - Correct Count 
    - Wrong Count
Pagination with 100 words per a page.
Clicking the japanese word will take us to the word show page.

#### API Endpoints

- GET /api/words


### Words Show `/words/:id`

#### Purpose
The purpose of this page is to display more information about a specific word.

#### Components
- Japanese
- Romaji 
- English
- Study Statistics
    - Correct Count
    - Wrong Count 
- Word Groups - shown as a series of pills (e.g. tags)
    - When group name is clicked, it will take us to the group show page.

#### API Endpoints
- GET /api/words/:id


### Word Groups `/groups`

#### Purpose
The purpose of this page is to show a list of all the word groups in the database.

#### Components
- Paginated Group List
    - Columns   
        - Group Name
        - Word Count
    Clicking the group name will take us to the group show page.
 
#### API Endpoints
- GET /api/groups


### Word Group Show `/groups/:id`

#### Purpose
The purpose of this page is to show a list of all the words in a specific word group.

#### Components
- Group Name
- Group Statistics 
    - Total Word Count 
- Words in Group (Paginated list of words)
    - Should use the same components as the words index page. 
- Study Sessions (Paginated list of study sessions)
    - Should use the same components as the study sessions index page.

#### API Endpoints
- GET /api/groups/:id
- GET /api/groups/:id/words
- GET /api/groups/:id/study-sessions


### Study Sessions `/study-sessions`

#### Purpose
The purpose of this page is to show a list of all the study sessions in the database.

#### Components
- Paginated List of Study Sessions
    - Columns
        - Id
        - Activity Name
        - Group Name
        - Start Time
        - End Time
        - Number of Review Items
    - Clicking the study session id will take us to the study session show page.

#### API Endpoints
- GET /api/study-sessions


### Study Session Show `/study-sessions/:id`

#### Purpose
The purpose of this page is to show more information about a specific study session.

#### Components
- Study Session Details
    - Activity Name 
    - Group Name
    - Start Time
    - End Time
    - Number of Review Items
- Words Review Items (Paginated list of wrods)
    - Should use the same components as the words index page.

#### API Endpoints
- GET /api/study-sessions/:id
- GET /api/study-sessions/:id/words


## Settings `/settings`

#### Purpose
The purpose of this page is to allow the user to configure the study portal.

#### Components
- Theme Selection eg. Light/Dark mode, System default 
- Language Selection eg. English, Japanese (potentially more target languages)
- Reset History Button 
    - This will delete all study sessions and word review items.
- Full Reset Button
    - this will drop all tables and recreate using original seed data.

#### API Endpoints
- POST /api/settings/reset-history
- POST /api/settings/full-reset


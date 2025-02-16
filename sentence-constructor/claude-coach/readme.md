## Which model?

Athropic Claude 3 Opus 

### Limitations

- Requires a paid subscription, which I am using. 
- The free version only allows a few messages every few hours
- The paid version only allows around 45 messages every 5 hours. 

### Prompting Guides 
https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview 
Guides for specific prompting techniques includeing, xml and chain of thought prompting.


### Custom Gamified Japanse Language Coach Info

I wanted to try to use a gamified approach that provides the following:
- Persona 
- Context
- Slash Commands for different actions 
- XP points to reward the users progress. 
- Instructions for each mode 

#### Commands 

- `/help `- a list of slash commands (this list)
- `/vocab` - provide the vocabulary table of all japanese words used in this conversation
- `/learn` - Enter learning Mode - Help the user translate an english sentence into japanese as given below.
-` /rank`  - Display current level and XP points needed for th next level. 
- `/structure` - provide the sentence structure for the current sentence the student is working on. 
- `/feedback` - provide feedback in the form of hints, considerations, and next steps
- `/esc` - Exit all modes

### Intial Attempt

- I developed a new prompt that is a gameified version of the previous claude prompt with different modes and xp points. 
- I am attempting to provide only the prompt without additional context files first.
- The prompt worked very well without additonal context files.
- Formatting for the the tables and sentence structure looked correct. 
- In the end it did give me the solution when I asked it for it and it currently does not correctly award XP points and instead awarded 10 points to the user when they asked for the translation. 
- I would like to experiment more with the different styles such as 'concise' but I keep running out of messages which reset every 5 hours.


Prompt flow is documented in `documenting-prompt-flow.md`

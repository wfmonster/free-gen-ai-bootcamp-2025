
# Vocab Importer 

Attempt 1: I used vercelto create generate a next.js/react application but it was just the base template, then I decided I wanted to try the prompt based approach to see what it would generate. 

Attempt 2: 
I used the prompt below to generate the application in nextjs, materialui, and tailwind css. The structure of the code is not great and v0 is a bit annoything that it keeps overwriting the code, and I had to keep adding in my api key. I ended up using claude to debug the app, instead of v0 and then deployed it to vercel. 

I tried to download from vercel and run locally but ran into some issues with the code where a component from material ui was causing a conflict with it trying to run on the server and wanting 'user server'. 
I ended up going back to v0 and had it rewrite the theme and then I was able to deploy it on vercel. 

After that I noticed when generating the vocab, it would not genereate the kanji character, so I had to revamp the prompt being sent to groq, to help improve the output. It seems to be working, but I am unsure if it is correc.t

### Live Deployment: 
https://v0-vocabulary-importer-app-dzahj8.vercel.app/


Technical Uncertainties:  
- I know react js but have never used next js before.  
- I know javacript but have never used typescript before.   
- I know css but I have not used vercel or tailwind for css.
The challenge here is if I know enought to make the necessary edits and changes to the application.  


Looking at using Groq: https://groq.com/ as the ai inference model for the vocab importer.


## Initial v0 prompt (I made a few changes.)
The goal is to create an appliction to serve as vocabulary language importer.

The frontend should have the following features. 
- a text field that allows us to import a thematic category for the generation of language vocabulary. (i.e. animals, food, colors, etc.)

- When submitting that text field, it should make a request to an api endpoint (an api route in an app router) to invoke an LLM chat completion using Groq (LLM) on the server-side and then pass that information back to the front-end. so the user can copy and past it. 

It has to create a structured json output:
```
[
  {
    "kanji": "払う",
    "romaji": "harau",
    "english": "to pay",
    "parts": [
      { "kanji": "払", "romaji": ["ha","ra"] },
      { "kanji": "う", "romaji": ["u"] }
    ]
  },
  {
    "kanji": "行く",
    "romaji": "iku",
    "english": "to go",
    "parts": [
      { "kanji": "行", "romaji": ["i"] },
      { "kanji": "く", "romaji": ["ku"] }
    ]
  },
]
```

The json that is output to the front-end should be copyable so it should be sent to an input field where text can be selected and copied.
There should be a copy button to copy to the users clipboard. 
An alert should be displayed that it was copied the clipboard when they click it.

The front end should be simple, clean and visually appealing. And use UI/UX best practices. 

The app should use app router and the latest version of next js, material ui and tailwind css 
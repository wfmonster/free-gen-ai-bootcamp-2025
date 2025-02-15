#Japanese Sentence Constructor

**Difficulty**: Level 100

### Business Goal: 
A chat agent that acts as a teaching assistant to guide students from translating a target English sentence into Japanese. 
The teaching assistant is not there to provide the direct answer, only guidance.

### Technical Uncertainty
1. How well can an AI-Powered Assistant perform a very broad task?
2. Would a very broad task be better performed by dividing it into subtasks with specialized agents?
3. Does using an AI-Powered Assistant make for a good place to rapidly prototype agents?
4. How could we take the agent we built in an AI-Powered Assistant and reimplement it into a stack that allows for direct integration into our platform?	
5. How much do we have to rework our prompt documents from one AI-Powered Assistant to another?
6. What prompting techniques can we naturally discover working in the confines of an AI-Powered Assistant?
7. Are there any interesting innovations unique to specific AI-Powered Assistants for our business goal?
8. What were we able to achieve based on our AI-Powered Assistant choice and our hardware, or budget limitations?

### Technical Restrictions
An AI-Powered Assistant of the developer’s choice must be used eg: 
- Meta AI https://www.meta.ai/
- ChatGPT https://openai.com/index/chatgpt/
- Anthropic Claude https://www.anthropic.com/claude
- Mistral AI https://mistral.ai/
- *Ollama + Open WebUI https://openwebui.com/
- *LibreChat https://www.librechat.ai/
-Leon https://github.com/leon-ai/leon


## Meta Powered AI-Assistant Guide

## Which Model 

Meta.ai is using Llama 3 - 70B

https://huggingface.co/meta-llama/Llama-3.1-70B 

Limitations
- This model currently seems to be unable to display Japanese Kanji in the browser.



## Prompting Guides

https://www.promptingguide.ai/techniques/meta-prompting 

It appears meta does not have any special requirements for creating prompts and understanding context.



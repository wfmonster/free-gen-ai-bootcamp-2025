
### Requirements 

**Functional Requirements**
- The application should support up to 300 students that may interact with the system locally and simultaneously.
- The application will served on a local machine that is only accessible on their local network.


**Constraints** (These are requirements imposed by external parties or factors)
- Hardware for the system should not exceed the budget of 10-15k
- The language model should be able to run on local hardware to ensure data privacy and to keep costs constrained. 

### Assumptions 

We are assuming that the open-source LLMs will be able to accomplish the task using an AI PC built within the budget.


### Data Strategy

There is a concern of copyrighted materials, so we must purchase and supply materials and store them for access in  our database.


### Considerations

we are considering using IBM Granite because it is a truly open-source model with training data that is traceable so we can avoid copyright infringement and understand what is going on with the model 

[IBM Granite](https://huggingface.co/ibm-granite)
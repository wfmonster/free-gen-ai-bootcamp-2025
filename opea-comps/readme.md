# Running OPEA on local machine - Mac OS M1 Pro

**Description:**
Running Ollama third-party service container locally with docker.


### Installation Requirements
- Docker
    - run `docker` to test that docker is installed. 
- Ollama
    Start ollama server on your machine after intalling it.
    Fetch the ollama model you want to use.
    - `ollama pull <model>`
    - `ollama pull llama3.2:1b`

You can get the model id string of the model you want to usefrom the ollama website:
https://ollama.com/library/llama3.2:1b

**Running Ollama:**
All of your local models are automatically served on localhost:11434. 
You run ollama run <name-of-model> to start interacting via the command line directly. To ensure everything is working:
`ollama run llama3.2:1b` 


### Project Setup
Create a `docker-compose.yaml` file and copy over the contents from the ollam documentation. We will not use a proxy. see: `docker-compose.yaml` for details.

Ollama-docker opea documentation (docker-compose.yaml file)
https://github.com/opea-project/GenAIComps/tree/main/comps/third_parties/ollama

- Installed the docker extension in cursor. 

You will need to get your IP address to use in the `docker-compose.yaml` file. This will vary depending on your operating system.

For macOS, use:
```bash
host_ip=$(ipconfig getifaddr en0)
```

For Linux systems, use: (this will throw an error on macos)
```bash
host_ip=$(hostname -I | awk '{print $1}') 
```

### Environment Setup and Running Docker Container

You have to make sure that you export the environment variables before running the docker compose up command. This will set your environment variables and then build the docker container.

This will take a bit of time the first time you run it. If you misconfigure the environment variables, you can stop the docker container and export them. then run docker compose up again.

```bash
# For macOS
export host_ip=$(ipconfig getifaddr en0)
export no_proxy=localhost,127.0.0.1
export LLM_ENDPOINT_PORT=9000 
export LLM_MODEL_ID="llama3.2:1b" 
docker compose up
```

This shows the successful build of the docker container and that the environment variables are set.

![Docker Compose Up Output](docker-compose-up-with-env.png)

You can use: `docker ps` to see what docker containers are running, in another terminal. 


### Ollama API 
- [Ollama API Docs](https://github.com/ollama/ollama/blob/main/docs/api.md)
- Once the Ollama server is running, we can make API calls to the Ollama API.
- Generate a completion with Ollama API: [Docs](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion)

## Making a request to the Ollama API: 

**Generate a completion.**
In a new terminal, run:
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "Why is the sky blue?"
}'
```

This shows the successful execution of the curl command.

![Curl Command Output](curl-generate-completion.png)

You do not need to pull a new model into the docker container. If you have ollama installed, models are automatically available at: `localhost:11434` when ollama is running on your machine.


### Technical Uncertainty. 

The documentation on the opea website for building the ollama docker container provided very little detail so it required some research to get the docker container running and working with ollama. 

I was unsure if I could interface directly with the ollama server from the docker container or if I needed to pull a model into the docker container.  Turns out that you do not need to pull the model into the docker container. You have to run the ollama server, then build the docker container. and can then make the curl request with the ollama api. 

Initially I was unsure if the curl command was really interacting with the docker container or if it was directly interacting with the ollama server. 

I know it is interfacing with the docker container because docker ps shows that the container is running on port 9000 and the curl command is using the localhost:9000/api/generate endpoint.

![Docker PS Output](docker-pos-output.png)


from comps import MicroService, ServiceOrchestrator, ServiceType
import requests
import os

class SimpleOllamaService:
    def __init__(self, port=8000):
        self.port = port
        self.service = ServiceOrchestrator()
        
    def construct_service(self):
        # Configure Ollama service connection
        ollama = MicroService(
            name="ollama",
            host="localhost",  # Assuming Ollama is running locally in Docker
            port=11434,  # Default Ollama port
            endpoint="/api/generate",
            use_remote_service=True,
            service_type=ServiceType.LLM
        )
        
        # Add service to orchestrator
        self.service.add(ollama)
        
    def query_ollama(self, prompt, model="llama3.2:1b"):
        """
        Send a query to Ollama and get response
        """
        url = f"http://localhost:11434/api/generate"
        data = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()['response']
        except Exception as e:
            return f"Error querying Ollama: {str(e)}"
    
    def start_service(self):
        self.construct_service()
        print(f"Service constructed and ready to accept queries")
        
        # Simple REPL for testing
        while True:
            prompt = input("\nEnter your prompt (or 'quit' to exit): ")
            if prompt.lower() == 'quit':
                break
            
            response = self.query_ollama(prompt)
            print(f"\nOllama Response:\n{response}")

if __name__ == "__main__":
    # First ensure Ollama is running in Docker:
    # docker run -d -p 11434:11434 ollama/ollama
    # docker exec -it <container_id> ollama run llama2
    
    service = SimpleOllamaService()
    service.start_service()
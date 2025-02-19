from comps import MicroService, ServiceOrchestrator, ServiceType
import requests
import os
import json

class SimpleOllamaService:
    def __init__(self, port=8000):
        self.port = port
        self.service = ServiceOrchestrator()
        
    def construct_service(self):
        # Configure guardrails service
        guardrails = MicroService(
            name="guardrails",
            host="localhost",
            port=3000,  # Typical port for guardrails service
            endpoint="/validate",
            use_remote_service=True,
            service_type=ServiceType.GUARDRAIL
        )
        
        # Configure Ollama service connection
        ollama = MicroService(
            name="ollama",
            host="localhost",
            port=11434,
            endpoint="/api/generate",
            use_remote_service=True,
            service_type=ServiceType.LLM
        )
        
        # Add services to orchestrator
        self.service.add(guardrails).add(ollama)
        
        # Create flow: guardrails -> llm
        self.service.flow_to(guardrails, ollama)
        
    def validate_content(self, content):
        """
        Validate content using guardrails service
        """
        url = "http://localhost:3000/validate"
        data = {
            "content": content,
            "settings": {
                "content_safety": True,
                "toxicity_threshold": 0.7,
                "profanity_check": True,
                "max_length": 1000
            }
        }
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"valid": False, "error": str(e)}
        
    def query_ollama(self, prompt, model="llama2"):
        """
        Send a query to Ollama with guardrails validation
        """
        # First validate the prompt
        validation_result = self.validate_content(prompt)
        if not validation_result.get("valid", False):
            return f"Content validation failed: {validation_result.get('error', 'Unknown error')}"
        
        # If validation passes, query Ollama
        url = f"http://localhost:11434/api/generate"
        data = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            llm_response = response.json()['response']
            
            # Validate the LLM response as well
            response_validation = self.validate_content(llm_response)
            if not response_validation.get("valid", False):
                return f"LLM response failed validation: {response_validation.get('error', 'Unknown error')}"
                
            return llm_response
        except Exception as e:
            return f"Error querying Ollama: {str(e)}"
    
    def start_service(self):
        self.construct_service()
        print("Service constructed with guardrails and ready to accept queries")
        print("Content will be validated for safety before processing")
        
        # Simple REPL for testing
        while True:
            prompt = input("\nEnter your prompt (or 'quit' to exit): ")
            if prompt.lower() == 'quit':
                break
            
            response = self.query_ollama(prompt)
            print(f"\nOllama Response:\n{response}")

if __name__ == "__main__":
    # Setup requirements:
    # 1. Ollama in Docker:
    #    docker run -d -p 11434:11434 ollama/ollama
    #    docker exec -it <container_id> ollama run llama2
    # 2. Guardrails service:
    #    Should be running on localhost:3000
    
    service = SimpleOllamaService()
    service.start_service()
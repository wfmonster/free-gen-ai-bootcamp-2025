# Import required components from the comps module
from comps import(
    MicroService, 
    ServiceOrchestrator, 
    ServiceType, 
    ServiceRoleType,
    MegaServiceEndpoint
)

from comps.cores.proto.api_protocol import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionResponseChoice,
    ChatMessage,
    UsageInfo,
)
import os

# Environment variables for service configuration
SERVICE_HOST_IP = os.getenv("SERVICE_HOST_IP", "0.0.0.0")

# Service 1: Embedding Service
EMBEDDING_SERVICE_HOST_IP = os.getenv("EMBEDDING_SERVICE_HOST_IP", "0.0.0.0")
EMBEDDING_SERVICE_PORT = os.getenv("EMBEDDING_SERVICE_PORT", 6000)

# retrieval 
RETRIEVER_SERVICE_HOST_IP = os.getenv("RETRIEVAL_SERVICE_HOST_IP", "0.0.0.0")
RETRIEVER_SERVICE_PORT = os.getenv("RETRIEVAL_SERVICE_PORT", 7000)

# reranking 
RERANKING_SERVICE_HOST_IP = os.getenv("RERANKING_SERVICE_HOST_IP", "0.0.0.0")
RERANKING_SERVICE_PORT = os.getenv("RERANKING_SERVICE_PORT", 8000)

# LLM Service
LLM_SERVICE_HOST_IP = os.getenv("LLM_SERVICE_HOST_IP", "0.0.0.0")
LLM_SERVICE_PORT = os.getenv("LLM_SERVICE_PORT", 9000)

os.environ["TELEMETRY_ENDPOINT"] = ""


# Goal is to create a RAG megaservice  
# The flow is: embedding >> retrieval >> reranking >> llm
# ChatQNA example: https://github.com/opea-project/GenAIExamples/tree/main/ChatQnA
# Docs: https://opea-project.github.io/latest/community/rfcs/24-05-17-OPEA-001-Deployment-Design.html
# https://github.com/opea-project/GenAIExamples/blob/main/ChatQnA/README.md
class ExampleRAGService:
    """
    A service orchestrator that manages connections between embedding and LLM services.
    Acts as a coordinator for a distributed system of AI services.
    """
    def __init__(self, host="0.0.0.0", port=8000):
      
        """
        Initialize the service with host and port configuration
        """
        self.port = port
        self.host = host
        self.endpoint = "/v1/example-rag-service"
        self.megaservice = ServiceOrchestrator()

    def construct_rag_service(self):
        """
        Configures and connects to remote embedding and LLM services.
        Creates a processing flow from embedding service to LLM service.
        """
        # Configure the embedding service connection
        embedding = MicroService(
            name="embedding",
            host=EMBEDDING_SERVICE_HOST_IP,
            port=EMBEDDING_SERVICE_PORT,
            endpoint="/v1/embeddings",
            use_remote_service=True,
            service_type=ServiceType.EMBEDDING,
        )

        # Configure the retrieval service connection
        retrieval = MicroService(
            name="retriever",
            host=RETRIEVER_SERVICE_HOST_IP,
            port=RETRIEVER_SERVICE_PORT,
            endpoint="/v1/retrieval",
            use_remote_service=True,
            service_type=ServiceType.RETRIEVER,
        )
        
        # Configure the reranking service connection
        rerank = MicroService(
            name="reranking",
            host=RERANKING_SERVICE_HOST_IP,
            port=RERANKING_SERVICE_PORT,
            endpoint="/v1/reranking",
            use_remote_service=True,
            service_type=ServiceType.RERANK,
        )

        # Configure the LLM service connection
        llm = MicroService(
            name="llm",
            host=LLM_SERVICE_HOST_IP,
            port=LLM_SERVICE_PORT,
            endpoint="/v1/chat/completions",
            use_remote_service=True,
            service_type=ServiceType.LLM,
        )
        
        # Add both services to the orchestrator
        self.megaservice.add(embedding).add(retrieval).add(rerank).add(llm)

        # Create a processing flow: embedding >> retrieval >> reranking >> llm
        self.megaservice.flow_to(embedding, retrieval)
        self.megaservice.flow_to(retrieval, rerank)
        self.megaservice.flow_to(rerank, llm)


    async def handle_request(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        try:
            # Format the request for Ollama
            ollama_request = {
                "model": request.model or "llama3.2:1b", 
                "messages": [
                    {
                        "role": "user",
                        "content": request.messages  # assuming messages is a string
                    }
                ],
                "stream": False  # disable streaming for now
            }
            
            # Schedule the request through the orchestrator
            result = await self.megaservice.schedule(ollama_request)
            
            # Extract the actual content from the response
            if isinstance(result, tuple) and len(result) > 0:
                llm_response = result[0].get('llm/MicroService')

                print(llm_response)

                if hasattr(llm_response, 'body'):
                    # Read and process the response
                    response_body = b""
                    async for chunk in llm_response.body_iterator:
                        response_body += chunk
                    content = response_body.decode('utf-8')
                else:
                    content = "No response content available"
            else:
                content = "Invalid response format"

            # Create the response
            response = ChatCompletionResponse(
                model=request.model or "example-model",
                choices=[
                    ChatCompletionResponseChoice(
                        index=0,
                        message=ChatMessage(
                            role="assistant",
                            content=content
                        ),
                        finish_reason="stop"
                    )
                ],
                usage=UsageInfo(
                    prompt_tokens=0,
                    completion_tokens=0,
                    total_tokens=0
                )
            )
            
            return response
            
        except Exception as e:
            # Handle any errors
            raise HTTPException(status_code=500, detail=str(e))
    
    
    def start(self):

        self.service = MicroService(
            self.__class__.__name__,
            service_role=ServiceRoleType.MEGASERVICE,
            host=self.host,
            port=self.port,
            endpoint=self.endpoint,
            input_datatype=ChatCompletionRequest,
            output_datatype=ChatCompletionResponse,
        )

        self.service.add_route(self.endpoint, self.handle_request, methods=["POST"])

        self.service.start()

# Create an instance of the service when run directly
if __name__ == "__main__":
    example_rag_service = ExampleRAGService() 
    example_rag_service.start()
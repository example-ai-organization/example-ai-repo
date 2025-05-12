from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

# load environment variables from .env file
# contains GOOGLE_API_KEY
load_dotenv()

def haiku_spitter(topic: str) -> str:
    # initialize model instance
    model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

    ai_response = model.invoke([SystemMessage("You will recieve a topic. Please respond with a haiku about that topic only. "), HumanMessage(topic)])

    # return string AI response
    return ai_response.content


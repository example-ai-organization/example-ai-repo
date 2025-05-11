from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

# load environment variables from .env file
# contains GOOGLE_API_KEY
load_dotenv()

# initialize model instance
model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

print("Give me a topic, and I shall give you a Haiku!")
topic = input()

ai_response = model.invoke([SystemMessage("You will recieve a topic. Please respond with a haiku about that topic only. "), HumanMessage(topic)])

# print ai response
print(ai_response.content)


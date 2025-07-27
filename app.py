from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

@app.get("/")
def read_root():
    return {"message": "Climate Chat API is running!"}

@app.post('/chat')
def handle_query(request: ChatRequest):
    try:
        if not OPENAI_API_KEY:
            return {"error": "OpenAI API key not configured"}
        
        openai.api_key = OPENAI_API_KEY
        
        print(f"Received query: {request.query}")  # 调试日志
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": request.query}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        answer = response.choices[0].message.content
        print(f"OpenAI response: {answer[:100]}...")  # 调试日志
        return {"response": answer}
    except Exception as e:
        print(f"Error: {str(e)}")  # 调试日志
        return {"error": str(e)}

# 添加一个简单的测试端点
@app.post('/test')
def test_endpoint(request: dict):
    print(f"Test endpoint received: {request}")
    return {"message": "Test successful", "received": request}

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host='0.0.0.0', port=port)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

@app.get("/")
def read_root():
    return {"message": "Climate Chat API is running!"}

@app.post('/chat')
def handle_query(request):
    try:
        if not OPENAI_API_KEY:
            return {"error": "OpenAI API key not configured"}
        
        openai.api_key = OPENAI_API_KEY
        
        query = request.get("query", "")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        answer = response.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host='0.0.0.0', port=port)

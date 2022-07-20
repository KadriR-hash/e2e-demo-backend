from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# end point used to write logs from the front  in a log file which is used as a plugin for  logstash
@app.post("/file/{message}")
async def root(message: str):
    # using Info as a default log type for testing purpose
    body = {
        "type": "Info",
        "message": message
    }
    # convert into JSON:
    json_content = json.dumps(body)
    print(json_content)
    with open('C:/Users/hp/OneDrive/Bureau/logs/logging.log', 'a+') as file:
        file.write(json_content+'\n')
    # file.close()

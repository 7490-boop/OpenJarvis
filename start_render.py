import os
os.environ["OPENJARVIS_HOME"] = "/tmp/openjarvis"

import uvicorn
from openjarvis.server.app import create_app

app = create_app(
    engine="litellm",
    model="gemini/gemini-2.5-flash",
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

from fastapi import FastAPI

app = FastAPI(title="SafeNestT Custom Platform", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "safenestt-custom-platform"}

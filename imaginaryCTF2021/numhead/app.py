import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="src.main:imaginary_app", host="0.0.0.0",
                port=8080, reload=False, debug=False)

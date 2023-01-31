from fastapi import FastAPI


app = FastAPI(debug=True)


@app.get('/')
def root():
    return {"message": "Melcow!"}


@app.get('/items/{item_id}')
def root(item_id):
    return {"item": f"Item no: {item_id}"}
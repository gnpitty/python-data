from prefect import flow, task

@task
def extract():
    return [1,2,3,6]

@task
def transform(data):
    print(data)
    return [i * 10 for i in data]

@flow
def pipeline():
    raw = extract()
    result = transform(raw)
    print(result)
## Ejecuta PipeLine
pipeline()
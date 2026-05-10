from app.graph import run_agent

while True:

    question = input("\nPregunta: ")

    if question.lower() == "salir":
        break

    run_agent(question)

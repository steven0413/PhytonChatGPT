import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key

    print("[bold green]Bienvenido a la demo de OpenAI Chat![/bold green]")

    table = Table("Comandos", "Descripción")
    table.add_row("exit", "Salir del programa")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del asistente
    context = [{"role": "system", "content": "Eres un asistente muy útil y servicial en OpenAI."}]
    messages = context.copy()

    while True:
        content = __prompt()

        if content == "new":
            print("[yellow]Creando una nueva conversación...[/yellow]")
            messages = context.copy()
            continue  

        messages.append({"role": "user", "content": content})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )

            response_content = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": response_content})

            print(f"[green]{response_content}[/green]")

        except Exception as e:
            print(f"[red]Error al comunicarse con OpenAI: {e}[/red]")

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar?")

    if prompt == "exit":
        exit_confirm = typer.confirm("¿Estás seguro de que quieres salir?")
        if exit_confirm:
            print("¡Hasta luego!")
            raise typer.Abort()
        return __prompt()  

    return prompt 

if __name__ == "__main__":
    typer.run(main)

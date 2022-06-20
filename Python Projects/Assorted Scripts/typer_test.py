# https://typer.tiangolo.com/
from typing import Optional

import typer

app = typer.Typer()


@app.command()
def hello(name: Optional[str] = None):
    if name:
        typer.echo(f"Hello {name}")
    else:
        typer.echo("Hello World!")


@app.command()
def bye(name: Optional[str] = None):
    if name:
        typer.echo(f"Bye {name}")
    else:
        typer.echo("Goodbye!")

@app.command()
def debug(name: Optional[str] = None):
    if name:
        typer.echo(f"This is a debug message,  {name}")
    else:
        typer.echo("Goodbye")

if __name__ == "__main__":
    app()
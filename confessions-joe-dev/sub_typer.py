import typer

app = typer.Typer()


@app.command()
def foo(y: float, x: int = 1 ):
    print(x * y)

@app.command()
def bar(z: str):
    print(f'(({z}))')


if __name__ == '__main__':
    app()
import typer

app = typer.Typer()

@app.command()
def main():
    print(f"Hello, Typer!")

if __name__ == "__main__":
    app()

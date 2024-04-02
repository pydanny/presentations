from pathlib import Path
from rich.console import Console

import typer

app = typer.Typer()
console = Console()
log = console.print


def bullets_to_slides(slide: str) -> str:
    new_slide = """

    """
    return slide.replace("- ", "")


@app.command()
def list2_slides(path: Path = typer.Argument(help="Path to the markdown file")):
    path = Path(path)
    content = path.read_text()
    top_slide = content.split("\n---\n")[0]
    slides = content.split("\n---\n")[1:]
    new_slides = []
    for i, slide in enumerate(slides):
        if '- ' in slide:        
            log(f"Slide {i + 1}:")
            log(slide)
            if typer.confirm("Do you want to convert this bullet list to slides?"):
                slide = slide.replace("- ", "1. ")
                log("Converted slide:")
                log(slide)
                break
            else:
                log("Slide not converted")
                new_slides.append(slide)
        else:
            new_slides.append(slide)


if __name__ == "__main__":
    app()
import pytube
from rich import print
from rich.progress import track
from rich.console import Console
from pytube.cli import on_progress

console = Console()

url = console.input("[bold green]URL video   [/]")
if url == 'ex':
    exit()
elif url == 'exit':
    exit()
else:
    pass
dire = console.input("[bold green]Enter the download directory   [/]")
if dire == 'ex':
    exit()
elif dire == 'exit':
    exit()
else:
    pass
console.print("[bold red]+++++++++++++++++++[/]")
print(dire)
console.print("[bold red]+++++++++++++++++++[/]")
yt = pytube.YouTube(url, on_progress_callback=on_progress)
ft = yt.title
console.print("[bold green]Please wait...[/]")
vid = yt.streams.get_highest_resolution()

va = yt.author
vd = yt.description
console.print("[bold blue](((((((((((((((AUTHOR)))))))))))))))[/]")
print(va)
console.print("[bold blue](((((((((((((((DESCRIPTION)))))))))))))))[/]")
print(vd)
console.print("[bold blue]###############################################################[/]")
for n in track(range(100), description="Download..."):
    downloads = vid.download(dire)
console.print("[bold green]##############################################################[/]")
console.print("[bold green]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!![/]")
console.print("[bold green]##############################################################[/]")
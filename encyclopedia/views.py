from django.shortcuts import render
from . import util

def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def show_entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Entrada não encontrada."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

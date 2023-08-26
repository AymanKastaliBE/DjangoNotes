from django.shortcuts import get_object_or_404, render, redirect
from .forms import NoteForm
from .models import Note


def index(request):
    notes = Note.objects.all().order_by( '-updated_at', '-created_at')
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)


def create_note(request):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note_form.save()
            return redirect('index')
    else:
        note_form = NoteForm()
        context = {
             'note_form': note_form,
        }
        return render(request, 'create_note.html', context)
    

def update_note(request, noteId):
    note = get_object_or_404(Note, id=noteId)
    if request.method == 'POST':
        note_form = NoteForm(request.POST, instance=note)
        if note_form.is_valid():
            note_form.save()
            return redirect('index')  # Redirect after successful edit
    else:
        note_form = NoteForm(instance=note)
    
    context = {
        'note': note,
        'note_form': note_form
        }
    return render(request, 'update_note.html', context)

def delete_note(request, noteId):
    note = get_object_or_404(Note, id=noteId)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    else:
        context = {
            'note': note,
        }
        return render(request, 'delete_note.html', context)
    
    
document.addEventListener('DOMContentLoaded', function() {
    fetchNotes();
    document.getElementById('add-note-form').addEventListener('submit', function(e) {
        e.preventDefault();
        addNote();
    });
});

function fetchNotes() {
    const url = 'http://127.0.0.1:8000/notes/';

    fetch(url)
    .then(response => response.json())
    .then(data => displayNotes(data.results))
    .catch(error => console.error('Erreur lors de la récupération des notes:', error));
}

function displayNotes(notes) {
    const notesList = document.getElementById('notes-list');
    notesList.innerHTML = '';

    notes.forEach(note => {
        const noteDiv = document.createElement('div');
        noteDiv.className = 'note-item';
        noteDiv.innerHTML = `
            <h3>${note.title}</h3>
            <p>${note.contents}</p>
            <button class="delete-btn" data-id="${note.id}">Supprimer</button>
        `;
        notesList.appendChild(noteDiv);
    });

    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function() {
            deleteNote(this.getAttribute('data-id'));
        });
    });
}

function addNote() {
    const title = document.getElementById('new-note-title').value;
    const content = document.getElementById('new-note-content').value;

    fetch('http://127.0.0.1:8000/notes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: title, contents: content })
    })
    .then(response => response.json())
    .then(data => fetchNotes())
    .catch(error => console.error("Erreur lors de l'ajout de la note:", error));
}

function deleteNote(noteId) {
    fetch(`http://127.0.0.1:8000/notes/${noteId}/`, {
        method: 'DELETE',
        headers: {
            
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erreur HTTP ! statut : ${response.status}`);
        }
        fetchNotes();
    })
    .catch(error => console.error("Erreur lors de la suppression de la note:", error));
}

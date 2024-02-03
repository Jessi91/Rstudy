// Récupérez l'élément du formulaire
const form = document.querySelector('form');

// Ajoutez un gestionnaire d'événements pour la soumission du formulaire
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Empêche la soumission par défaut du formulaire

    // Récupérez la catégorie sélectionnée
    const categorySelect = document.getElementById('categorySelect');
    const selectedCategory = categorySelect.value;

    // Redirigez l'utilisateur vers la page de quiz avec la catégorie sélectionnée
    window.location.href = `/quizApp/quiz/?category=${selectedCategory}`;
});

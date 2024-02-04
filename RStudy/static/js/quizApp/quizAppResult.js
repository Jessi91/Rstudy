document.addEventListener("DOMContentLoaded", function() {
    const app = Vue.createApp({
        delimiters: ['[[', ']]'],
        data() {
            return {
                selectedCategory: new URLSearchParams(window.location.search).get('category') || 'defaultCategory',
                questions: [],
                filteredQuestions: [], // Questions filtrées pour la catégorie sélectionnée
                showResults: false,
                score: 0,
                totalScore: 0,
                results: []
            };
        },
        methods: {
            getQuestions() {
                fetch(`http://127.0.0.1:8000/quizApp/api/get-quiz/?category=${encodeURIComponent(this.selectedCategory)}`)
                    .then(response => response.json())
                    .then(result => {
                        if (result.status) {
                            this.questions = result.data;
                            this.filterQuestions(); // Filtrez les questions après le chargement
                        } else {
                            console.error('Erreur dans les données reçues');
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            },
            filterQuestions() {
                this.filteredQuestions = this.questions.filter(q => q.category.toLowerCase() === this.selectedCategory.toLowerCase());
                // Réinitialisez 'showResults' pour ne pas afficher les anciens résultats lors du changement de catégorie
                this.showResults = false; 
            },
            
            submitQuiz() {
                this.score = 0;
                this.totalScore = 0;
                this.results = this.filteredQuestions.map(question => { // Utilisez 'filteredQuestions' au lieu de 'questions'
                    const userAnswers = question.answer.filter(a => a.selected).map(a => a.answer);
                    const correctAnswers = question.answer.filter(a => a.is_correct).map(a => a.answer);
                    const questionScore = userAnswers.every(answer => correctAnswers.includes(answer)) &&
                                          correctAnswers.every(answer => userAnswers.includes(answer)) ? question.marks : 0;
                    this.score += questionScore;
                    this.totalScore += question.marks;
                    
                    return {
                        question: question.question,
                        userAnswers,
                        correctAnswers,
                        questionScore
                    };
                });
                this.showResults = true;
            },
            
        },
        watch: {
            selectedCategory(newVal) {
                if (newVal) {
                    this.filterQuestions(); // Assurez-vous que cette méthode filtre les questions pour la nouvelle catégorie
                }
            }
        },
        
        mounted() {
            this.getQuestions();
        }
    });

    app.mount('#app');
});

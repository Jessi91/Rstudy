const resultsElement = document.getElementById('app');
// Mettez ce code dans quizAppAnswer.js

fetch(`/api/get-quiz/?category=${selectedCategory}`)
    .then(response => response.json())
    .then(data => {
        if (data.status === true && data.data.length > 0) {
            const quizData = data.data;

            quizData.forEach(questionData => {
                // Check if the question's category matches the selected category
                if (questionData.category === selectedCategory) {
                    // Create elements to display the question and answers
                    const questionElement = document.createElement('p');
                    questionElement.textContent = questionData.question;
                    resultsElement.appendChild(questionElement);

                    const answersList = document.createElement('ul');
                    questionData.answer.forEach(answer => {
                        const answerItem = document.createElement('li');
                        answerItem.textContent = answer.answer;
                        if (answer.is_correct) {
                            answerItem.classList.add('correct-answer');
                        }
                        answersList.appendChild(answerItem);
                    });
                    resultsElement.appendChild(answersList);
                }
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    }); 
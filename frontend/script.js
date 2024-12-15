async function fetchQuizzes() {
    const response = await fetch('http://127.0.0.1:5000/api/quizzes');
    const quizzes = await response.json();
    return quizzes;
  }
  
  let currentIndex = 0;
  
  async function loadQuiz() {
    const quizzes = await fetchQuizzes();
    const quiz = quizzes[currentIndex];
    const quizElement = document.getElementById("quiz");
    const resultElement = document.getElementById("result");
  
    resultElement.innerHTML = ""; // 前回の結果をリセット
    quizElement.querySelector(".question").textContent = quiz.question;
  
    const choicesElement = quizElement.querySelector(".choices");
    choicesElement.innerHTML = "";
  
    quiz.choices.forEach((choice, index) => {
      const button = document.createElement("button");
      button.textContent = choice;
      button.onclick = () => checkAnswer(quiz, index);
      choicesElement.appendChild(button);
    });
  }
  
  function checkAnswer(quiz, selectedIndex) {
    const resultElement = document.getElementById("result");
  
    if (selectedIndex === quiz.answer) {
      resultElement.innerHTML = `<p>正解！</p><p>${quiz.explanation}</p>`;
    } else {
      resultElement.innerHTML = `<p>不正解。正解は「${quiz.choices[quiz.answer]}」です。</p><p>${quiz.explanation}</p>`;
    }
  
    // 次の問題をロード
    currentIndex = (currentIndex + 1) % 2; // サンプルデータの数に合わせて変更
    setTimeout(loadQuiz, 3000);
  }
  
  // 初回ロード
  loadQuiz();
  
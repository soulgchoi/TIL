// 하나의 함수에 넣기
function init() {
    // Card 만들기
    const button = document.querySelector('#js-todo-button');
    const inputTag = document.querySelector('#js-todo-input');
    const reverseBtn = document.querySelector('#js-reverse-btn');
    const saveBtn = document.querySelector('#js-save-button');
    const loadBtn = document.querySelector('#js-load-button');

    saveBtn.addEventListener('click', () => {
        if (confirm('save?')) {
            const todoArea = document.querySelector('#js-todo-area');
            const content = todoArea.innerHTML;
            localStorage.setItem('content', content);
            alert('saved!');
        }
    })

    loadBtn.addEventListener('click', () => {
        if (confirm('load?')) {
            const todoArea = document.querySelector('#js-todo-area');
            const content = localStorage.getItem('content').split('\n');
            // const contents = localStorage.getItem('content').split('\n');
            // for (let i=0; i<contents.length; i++) {
                // createTodoCard(contests[i]);
            // }
            todoArea.innerHTML = content;
            alert('loaded!');
        }
    })


    reverseBtn.addEventListener('click', () => {
        const todoArea = document.querySelector('#js-todo-area');
        // const todos = document.querySelectorAll('.js-card'); // card 전부 todos 에 저장 > 복원 가능!
        // 위의 상태는 배열X, 배열로 바꿔야 함
        const todos = Array.from(document.querySelectorAll('.js-card'));
        while (todoArea.firstChild) {
            todoArea.removeChild(todoArea.firstChild);
        };
        // 역순으로 바꾸고, 하나씩 빼서 넣기
        todos.reverse().forEach((todo) => {
            todoArea.appendChild(todo);
        });
    })

    button.addEventListener('click', () => {
        const inputArea = document.querySelector('#js-todo-input');
        createTodoCard(inputArea.value);
        inputArea.value = null;
    });

    inputTag.addEventListener('keydown', (e) => {
        if (e.which === 13) {
            const inputArea = document.querySelector('#js-todo-input');
            createTodoCard(inputArea.value);
            inputArea.value = null;
        }
    });
}

const createTodoCard = (content, completed = false) => {
    const cardArea = document.querySelector('#js-todo-area');

    const todo = document.createElement('div');
    todo.className = 'ui segment js-card';
    const wrapper = document.createElement('div');
    wrapper.className = 'ui checkbox';
    const checkBox = document.createElement('input');
    checkBox.type = 'checkbox';
    checkBox.addEventListener('click', () => {
        if (checkBox.checked) {
            todo.classList.add('secondary');
            label.classList.add('done');
            // label 읽을 때 이미 label 등장한 시점
        } else {
            todo.classList.remove('secondary');
            label.classList.remove('done');
        };
    })

    const label = document.createElement('label');
    label.innerHTML = content;

    const deleteIcon = document.createElement('i');
    deleteIcon.className = 'icon close custom-icon';

    deleteIcon.addEventListener('click', () => {
        cardArea.removeChild(todo);
    })

    wrapper.appendChild(checkBox);
    wrapper.appendChild(label);
    todo.appendChild(wrapper);
    todo.appendChild(deleteIcon);
    cardArea.appendChild(todo);
};



init();
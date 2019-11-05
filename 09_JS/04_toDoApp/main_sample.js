function init() {
    const button = document.querySelector('#js-todo-button');
    const inputTag = document.querySelector('#js-todo-input');
    const reverseBtn = document.querySelector('#js-reverse-button');
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
            // const content = localStorage.getItem('content').split('\n');
            const contents = localStorage.getItem('content').split('\n');
            for (let i=0; i<contents.length; i++) {
                createTodoCard(contests[i]);
            }
            // todoArea.innerHTML = content;
            alert('loaded!');
        }
    })

    reverseBtn.addEventListener('click', () => {
        const todoArea = document.querySelector('#js-todo-area');
        const todos = Array.from(document.querySelectorAll('.js-card'));

        while (todoArea.firstChild) {
            todoArea.removeChild(todoArea.firstChild);
        }

        todos.reverse().forEach((todo) => {
            todoArea.appendChild(todo);
        });

    });

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

// Card 만들기
const createTodoCard = (content) => {
    if (content) {
        const cardArea = document.querySelector('#js-todo-area');

        const todo = document.createElement('div');
        todo.className = 'ui segment js-card';

        const wrapper = document.createElement('div');
        wrapper.className = 'ui checkbox';

        const checkBox = document.createElement('input');
        checkBox.type = 'checkbox';
        // 새로고침 이후에도 이벤트 리스너가 달리는지?
        checkBox.addEventListener('click', () => {
            if (checkBox.checked) {
                todo.classList.add('secondary');
                label.classList.add('done');
            } else {
                todo.classList.remove('secondary');
                label.classList.remove('done');
            }
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
    }
}

const saveToLocalStorage = () => {

}

init();
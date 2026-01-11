// script.js
// Todo application with persistence using localStorage

// ---------- Model ----------
class TodoItem {
    /**
     * @param {number|string} id - Unique identifier for the todo
     * @param {string} text - Description of the todo
     * @param {boolean} completed - Completion status
     */
    constructor(id, text, completed = false) {
        this.id = id;
        this.text = text;
        this.completed = completed;
    }

    /**
     * Convert the TodoItem to a plain object suitable for JSON.stringify
     * @returns {{id: (number|string), text: string, completed: boolean}}
     */
    toJSON() {
        return {
            id: this.id,
            text: this.text,
            completed: this.completed,
        };
    }
}

// ---------- State ----------
/** @type {TodoItem[]} */
let todos = [];

// ---------- Persistence ----------
function loadTodos() {
    const raw = localStorage.getItem('todos');
    if (!raw) {
        todos = [];
        return;
    }
    try {
        const parsed = JSON.parse(raw);
        // Ensure we get an array of plain objects
        if (Array.isArray(parsed)) {
            todos = parsed.map(obj => new TodoItem(obj.id, obj.text, obj.completed));
        } else {
            todos = [];
        }
    } catch (e) {
        console.error('Failed to parse todos from localStorage:', e);
        todos = [];
    }
}

function saveTodos() {
    const data = JSON.stringify(todos.map(t => t.toJSON()));
    localStorage.setItem('todos', data);
}

// ---------- UI Rendering ----------
function renderTodos() {
    const list = document.getElementById('todo-list');
    if (!list) return;
    // Clear existing items
    list.innerHTML = '';

    todos.forEach(todo => {
        const li = document.createElement('li');
        li.classList.add('todo-item');
        if (todo.completed) li.classList.add('completed');
        li.dataset.id = todo.id; // store id for potential debugging

        // Checkbox for completion toggle
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = todo.completed;
        checkbox.addEventListener('change', () => toggleCompletion(todo.id));

        // Text span
        const span = document.createElement('span');
        span.textContent = todo.text;
        span.classList.add('todo-text');

        // Delete button
        const delBtn = document.createElement('button');
        delBtn.textContent = 'Delete';
        delBtn.classList.add('delete-btn');
        delBtn.addEventListener('click', () => deleteTodo(todo.id));

        // Assemble
        li.appendChild(checkbox);
        li.appendChild(span);
        li.appendChild(delBtn);
        list.appendChild(li);
    });
}

// ---------- Business Logic ----------
function addTodo(text) {
    const id = Date.now(); // simple unique identifier based on timestamp
    const newTodo = new TodoItem(id, text, false);
    todos.push(newTodo);
    saveTodos();
    renderTodos();
}

function toggleCompletion(id) {
    const todo = todos.find(t => t.id === id);
    if (!todo) return;
    todo.completed = !todo.completed;
    saveTodos();
    renderTodos();
}

function deleteTodo(id) {
    todos = todos.filter(t => t.id !== id);
    saveTodos();
    renderTodos();
}

// ---------- Event Listeners ----------
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('todo-form');
    const input = document.getElementById('new-todo');

    // Load persisted todos and render them
    loadTodos();
    renderTodos();

    // Handle new todo submission
    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevent page reload
        const taskText = input.value.trim();
        if (taskText === '') return;
        addTodo(taskText);
        input.value = '';
        input.focus();
    });
});

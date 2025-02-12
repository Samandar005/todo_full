document.addEventListener('DOMContentLoaded', function() {
    const todos = document.querySelectorAll('li[data-id]');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    todos.forEach(todo => {
        const checkbox = todo.querySelector('.todo-checkbox');
        const title = todo.querySelector('.todo-title');

        checkbox.addEventListener('change', function() {
            const id = todo.dataset.id;

            const formData = new FormData();
            formData.append('completed', checkbox.checked);

            title.classList.toggle('line-through');

            fetch(`/todo/${id}/toggle/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            });
        });
    });
});

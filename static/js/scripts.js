document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll(".todo-checkbox");

    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", function () {
            const todoId = this.getAttribute("data-todo-id");
            const isChecked = this.checked;

            fetch(`/todo/update-status/${todoId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify({ completed: isChecked }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        const titleElement = this.nextElementSibling.querySelector(".todo-title");
                        if (isChecked) {
                            titleElement.classList.add("line-through");
                        } else {
                            titleElement.classList.remove("line-through");
                        }
                    }
                });
        });
    });

    function getCSRFToken() {
        return document.cookie
            .split("; ")
            .find((row) => row.startsWith("csrftoken="))
            .split("=")[1];
    }
});

function toggleStatus(todoId) {
    const checkbox = document.getElementById('todo-status');
    const statusLabel = document.getElementById('status-label');
    const url = `/todos/${todoId}/status/`;  // Adjust the URL according to your routing

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // Add CSRF token for security
        },
        body: JSON.stringify({ completed: checkbox.checked })
    })
    .then(response => {
        if (response.ok) {
            // Update the label based on the checkbox state
            if (checkbox.checked) {
                statusLabel.classList.remove('bg-red-200', 'text-red-700');
                statusLabel.classList.add('bg-green-200', 'text-green-700');
                statusLabel.textContent = 'Is Completed';
            } else {
                statusLabel.classList.remove('bg-green-200', 'text-green-700');
                statusLabel.classList.add('bg-red-200', 'text-red-700');
                statusLabel.textContent = 'Not Completed';
            }
            console.log('Status updated successfully.');
        } else {
            console.error('Error updating status.');
        }
    })
    .catch(error => console.error('Error:', error));
}
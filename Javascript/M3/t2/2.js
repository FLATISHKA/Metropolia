document.addEventListener('DOMContentLoaded', () => {
    const targetElement = document.getElementById('target');

    const items = ['First item', 'Second item', 'Third item'];
    items.forEach(itemText => {
        const li = document.createElement('li');
        li.textContent = itemText;
        targetElement.appendChild(li);
    });
});

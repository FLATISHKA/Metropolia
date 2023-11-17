document.addEventListener('DOMContentLoaded', () => {
    const triggerElement = document.getElementById('trigger');
    const targetImage = document.getElementById('target');

    triggerElement.addEventListener('mouseover', () => {
        targetImage.src = 'img/picB.jpg';
    });

    triggerElement.addEventListener('mouseout', () => {
        targetImage.src = 'img/picA.jpg';
    });
});

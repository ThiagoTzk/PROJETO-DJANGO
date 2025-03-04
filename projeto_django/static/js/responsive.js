document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.querySelector('.navbar');
    const cards = document.querySelectorAll('.card');

    function adjustLayout() {
        const screenWidth = window.innerWidth;

        if (screenWidth < 768) {
            navbar.style.backgroundColor = "#f8f9fa";
            cards.forEach(card => {
                card.style.marginBottom = "15px";
            });
        } else {
            navbar.style.backgroundColor = "";
            cards.forEach(card => {
                card.style.marginBottom = "";
            });
        }
    }

    adjustLayout();

    window.addEventListener('resize', adjustLayout);
});

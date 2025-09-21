document.querySelectorAll('.product-carousel').forEach((carousel, index) => {
    let currentIndex = 0;
    const slides = carousel.querySelector('.slides');
    const totalSlides = slides.children.length;

    function showNextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides;
        const offset = -currentIndex * 100;
        slides.style.transform = `translateX(${offset}%)`;
    }

    setInterval(showNextSlide, 3000); // Change image every 3 seconds
});

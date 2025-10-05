// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Form validation and enhancement
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('border-red-500');
            isValid = false;
        } else {
            input.classList.remove('border-red-500');
        }
    });
    
    return isValid;
}

// Add loading state to buttons
function addLoadingState(button) {
    const originalText = button.textContent;
    button.textContent = 'Loading...';
    button.disabled = true;
    
    return function() {
        button.textContent = originalText;
        button.disabled = false;
    };
}

// Enhanced image lazy loading with performance optimizations
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                
                // Create a new image to preload
                const newImg = new Image();
                newImg.onload = function() {
                    img.src = this.src;
                    img.classList.add('loaded');
                    img.classList.remove('lazy');
                };
                newImg.src = img.dataset.src;
                
                imageObserver.unobserve(img);
            }
        });
    }, {
        rootMargin: '50px 0px', // Start loading 50px before image enters viewport
        threshold: 0.1
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Performance monitoring for mobile devices
function checkPerformance() {
    if ('connection' in navigator) {
        const connection = navigator.connection;
        if (connection.effectiveType === 'slow-2g' || connection.effectiveType === '2g') {
            // Reduce animations and heavy effects for slow connections
            document.body.classList.add('reduce-motion');
        }
    }
}

// Throttle function for performance
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Enhanced scroll behavior for navigation
const handleScroll = throttle(function() {
    const scrolled = window.pageYOffset;
    const nav = document.querySelector('nav');
    
    if (nav && scrolled > 100) {
        nav.classList.add('shadow-lg');
    } else if (nav) {
        nav.classList.remove('shadow-lg');
    }
}, 16);

window.addEventListener('scroll', handleScroll);

// Touch gesture support for mobile
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', e => {
    touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', e => {
    touchEndX = e.changedTouches[0].screenX;
    
    // Close mobile menu on swipe left
    const mobileMenu = document.querySelector('.mobile-menu');
    if (mobileMenu && touchEndX < touchStartX - 50) {
        mobileMenu.classList.add('hidden');
    }
});

// Initialize performance optimizations
checkPerformance();
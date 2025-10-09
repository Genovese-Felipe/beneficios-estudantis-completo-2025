// BR Tech Pack - Interactive functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initNavigation();
    initThemeToggle();
    initTabs();
    initFilters();
    initMobileMenu();
    initAnimations();
});

// Navigation functionality
function initNavigation() {
    const navLinks = document.querySelectorAll('.nav__link');
    
    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Update active state
                updateActiveNavLink(this);
            }
        });
    });
    
    // Update active navigation on scroll
    window.addEventListener('scroll', throttle(updateNavOnScroll, 100));
}

// Update active navigation link
function updateActiveNavLink(activeLink) {
    document.querySelectorAll('.nav__link').forEach(link => {
        link.classList.remove('active');
    });
    activeLink.classList.add('active');
}

// Update navigation on scroll
function updateNavOnScroll() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPosition = window.scrollY + 150;
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');
        
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            const activeLink = document.querySelector(`a[href="#${sectionId}"]`);
            if (activeLink) {
                updateActiveNavLink(activeLink);
            }
        }
    });
}

// Theme toggle functionality
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Set initial theme
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeToggleIcon(currentTheme);
    
    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeToggleIcon(newTheme);
    });
}

function updateThemeToggleIcon(theme) {
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
}

// Tabs functionality for courses section
function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetTab = this.getAttribute('data-tab');
            
            // Update button states
            tabButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Update content visibility
            tabContents.forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(targetTab).classList.add('active');
        });
    });
}

// Filter functionality for tools section
function initFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const toolCards = document.querySelectorAll('.tool-card');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');
            
            // Update button states
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Filter cards
            toolCards.forEach(card => {
                const category = card.getAttribute('data-category');
                
                if (filterValue === 'all' || category === filterValue) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeInUp 0.6s ease forwards';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// Mobile menu functionality
function initMobileMenu() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('show');
        });
    }
    
    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav__link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('show');
        });
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
            navMenu.classList.remove('show');
        }
    });
}

// Animation on scroll
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.tool-card, .course-card, .benefit-category, .step');
    animateElements.forEach(element => {
        observer.observe(element);
    });
}

// FAQ functionality
document.addEventListener('click', function(e) {
    if (e.target.matches('.faq-question')) {
        const faqItem = e.target.closest('.faq-item');
        const isOpen = faqItem.hasAttribute('open');
        
        // Close all other FAQ items
        document.querySelectorAll('.faq-item[open]').forEach(item => {
            if (item !== faqItem) {
                item.removeAttribute('open');
            }
        });
    }
});

// Utility function for throttling
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

// Smooth reveal animation for cards
function revealCards() {
    const cards = document.querySelectorAll('.tool-card, .course-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

// Economy calculator (bonus feature)
function calculateEconomy() {
    const tools = [
        { name: 'GitHub Pro', value: 48 },
        { name: 'GitHub Copilot Pro', value: 240 },
        { name: 'JetBrains IDEs', value: 1200 },
        { name: 'DigitalOcean', value: 200 },
        { name: 'Microsoft Azure', value: 100 },
        { name: 'Canva Pro', value: 120 },
        { name: 'MongoDB Atlas', value: 50 },
        { name: 'Educative', value: 240 }
    ];
    
    const totalValue = tools.reduce((sum, tool) => sum + tool.value, 0);
    return {
        total: totalValue,
        monthly: Math.round(totalValue / 12),
        tools: tools
    };
}

// Initialize economy display
function displayEconomy() {
    const economy = calculateEconomy();
    const economyElements = document.querySelectorAll('.economy-value');
    
    economyElements.forEach(element => {
        element.textContent = `$${economy.total.toLocaleString()}`;
    });
}

// Call economy display when page loads
window.addEventListener('load', displayEconomy);

// Add loading state management
function showLoading(element) {
    element.classList.add('loading');
    element.innerHTML = '<div class="spinner"></div>';
}

function hideLoading(element, content) {
    element.classList.remove('loading');
    element.innerHTML = content;
}

// External link tracking (for analytics if needed)
function trackExternalLink(url, category) {
    // This would integrate with analytics service
    console.log(`External link clicked: ${url} (Category: ${category})`);
}

// Add click tracking to external links
document.addEventListener('click', function(e) {
    if (e.target.matches('a[target="_blank"]')) {
        const url = e.target.href;
        const category = e.target.closest('section')?.id || 'unknown';
        trackExternalLink(url, category);
    }
});

// Search functionality (if search input is added)
function initSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;
    
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const searchableElements = document.querySelectorAll('.tool-card, .course-card');
        
        searchableElements.forEach(element => {
            const text = element.textContent.toLowerCase();
            const isVisible = text.includes(searchTerm);
            element.style.display = isVisible ? 'block' : 'none';
        });
    });
}

// Keyboard navigation support
document.addEventListener('keydown', function(e) {
    // ESC key closes mobile menu
    if (e.key === 'Escape') {
        const navMenu = document.getElementById('nav-menu');
        navMenu.classList.remove('show');
    }
    
    // Enter key on buttons
    if (e.key === 'Enter' && e.target.matches('button')) {
        e.target.click();
    }
});

// Performance optimization: Lazy load images (if images are added)
function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Error handling for external API calls (if any)
function handleError(error, context) {
    console.error(`Error in ${context}:`, error);
    // Show user-friendly error message
    const errorMessage = document.createElement('div');
    errorMessage.className = 'error-message';
    errorMessage.textContent = 'Ocorreu um erro. Tente novamente mais tarde.';
    document.body.appendChild(errorMessage);
    
    setTimeout(() => {
        errorMessage.remove();
    }, 5000);
}

// Accessibility improvements
function improveAccessibility() {
    // Add focus indicators
    const focusableElements = document.querySelectorAll('button, a, input, select, textarea, [tabindex]');
    focusableElements.forEach(element => {
        element.addEventListener('focus', function() {
            this.classList.add('focused');
        });
        element.addEventListener('blur', function() {
            this.classList.remove('focused');
        });
    });
    
    // Add ARIA labels where needed
    const buttons = document.querySelectorAll('button:not([aria-label])');
    buttons.forEach(button => {
        if (!button.textContent.trim()) {
            button.setAttribute('aria-label', 'Botão');
        }
    });
}
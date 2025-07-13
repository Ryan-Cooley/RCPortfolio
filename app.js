(function () {
    // Navigation functionality
    [...document.querySelectorAll(".control")].forEach(button => {
        button.addEventListener("click", function() {
            const targetId = this.dataset.id;
            
            // Remove active class from current button
            const currentActiveBtn = document.querySelector(".active-btn");
            if (currentActiveBtn) {
                currentActiveBtn.classList.remove("active-btn");
            }
            
            // Add active class to clicked button
            this.classList.add("active-btn");
            
            // Remove active class from current section
            const currentActiveSection = document.querySelector(".active");
            if (currentActiveSection) {
                currentActiveSection.classList.remove("active");
            }
            
            // Add active class to target section
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.classList.add("active");
            }
        });
    });
    
    // Portfolio item click handlers - open modals
    [...document.querySelectorAll(".portfolio-item")].forEach(item => {
        item.addEventListener("click", function() {
            const projectType = this.dataset.project;
            const modal = document.getElementById(projectType + "-modal");
            if (modal) {
                modal.style.display = "block";
                document.body.style.overflow = "hidden"; // Prevent background scrolling
            }
        });
    });
    
    // Close modal handlers
    [...document.querySelectorAll(".close-modal")].forEach(closeBtn => {
        closeBtn.addEventListener("click", function() {
            const modal = this.closest(".project-modal");
            if (modal) {
                modal.style.display = "none";
                document.body.style.overflow = "auto"; // Restore scrolling
            }
        });
    });
    
    // Close modal when clicking outside
    [...document.querySelectorAll(".project-modal")].forEach(modal => {
        modal.addEventListener("click", function(e) {
            if (e.target === this) {
                this.style.display = "none";
                document.body.style.overflow = "auto";
            }
        });
    });
    
    // Handle hash navigation when landing on main page
    if (window.location.hash === '#portfolio') {
        const homeSection = document.querySelector("#home");
        const portfolioSection = document.querySelector("#portfolio");
        if (homeSection && portfolioSection) {
            homeSection.classList.remove("active");
            portfolioSection.classList.add("active");
            
            const homeBtn = document.querySelector('[data-id="home"]');
            const portfolioBtn = document.querySelector('[data-id="portfolio"]');
            if (homeBtn && portfolioBtn) {
                homeBtn.classList.remove("active-btn");
                portfolioBtn.classList.add("active-btn");
            }
        }
    }
})();

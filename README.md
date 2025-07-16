# Ryan Cooley's Personal Portfolio Website

This repository hosts the source code for Ryan Cooley's personal portfolio website, showcasing his work as a Computational Scientist and Systems Thinker. The website serves as a dynamic resume and project showcase, highlighting expertise in scientific computing, data automation, and software engineering.

## Features

*   **Interactive Project Showcase:** Detailed modals for each project, including descriptions, technical highlights, and visual assets.
*   **Responsive Design:** Optimized for various devices, from desktops to mobile phones.
*   **Skill Overview:** A dedicated section outlining key technical skills.
*   **Contact Information:** Easy access to professional contact details.

## Technologies Used

*   **HTML5:** For structuring the web content.
*   **CSS3 (SCSS):** For styling, with a focus on modern aesthetics and responsive layouts.
*   **JavaScript (Vanilla JS):** For interactive elements, navigation, and modal functionality.
*   **Font Awesome:** For icons.
*   **Google Fonts:** For custom typography.

## Project Structure

```
RCPortfolio/
├── .git/                   # Git version control
├── .gitignore              # Files and directories to ignore in Git
├── .gitmodules             # Git submodule configuration
├── app.js                  # Main JavaScript file for interactivity
├── index.html              # Main HTML file (website structure)
├── README.md               # Project README (this file)
├── Ryan_Cooley_Resume_2025.pdf  # Link to Ryan's resume
├── img/                    # Image assets for the website
├── Snake_Game/             # Submodule for the Python Snake Game
├── styles/                 # SCSS and compiled CSS files
├── TIP3P-Water-Sim/        # Submodule for the TIP3P Water Simulation project
└── VBA_Automation/         # Submodule for the VBA Automation project
```

## How to Run Locally

To view this website locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ryan-Cooley/RCPortfolio.git
    cd RCPortfolio
    ```
2.  **Initialize and update submodules:**
    This project uses Git submodules for some of the showcased projects.
    ```bash
    git submodule update --init --recursive
    ```
3.  **Open `index.html`:**
    Simply open the `index.html` file in your web browser. No local server is required for basic viewing.

## Contact

For inquiries, please refer to the contact information provided on the website.

---
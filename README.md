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
├── .DS_Store               # macOS system file
├── app.js                  # Main JavaScript file for interactivity
├── index.html              # Main HTML file (website structure)
├── README.md               # Project README (this file)
├── Ryan_Cooley_Resume_SWE.pdf  # Ryan's Software Engineering resume
├── img/                    # Image assets for the website
│   ├── MCplots/           # Monte Carlo simulation visualizations
│   │   ├── benchmark_results.png
│   │   ├── convergence_v2.png
│   │   ├── delta_surface.png
│   │   ├── enhanced_risk_analysis.png
│   │   ├── hedge_pnl.png
│   │   ├── iv_heatmap.png
│   │   ├── iv_surface.png
│   │   ├── MSFT_returns.png
│   │   └── vega_surface.png
│   ├── CallSign.png       # Ham Radio call sign
│   ├── HamRadioConfirmation.jpg  # Ham Radio license
│   ├── PCEP Certification.jpg     # Python certification
│   ├── ryan_pic.jpg       # Profile picture
│   ├── snake_image.png     # Snake game screenshot
│   ├── sma_dashboard_AAPL_20_50.png  # SMA backtester results
│   ├── sma_dashboard_QQQ_10_30.png   # SMA backtester results
│   ├── sma_dashboard_SPY_20_50.png   # SMA backtester results
│   ├── SMABacktetser.gif  # SMA backtester animation
│   ├── sushi_go.jpg       # Sushi Go game screenshot
│   ├── trajectory.gif      # TIP3P water simulation
│   ├── VBA_Master_Macro.png  # VBA automation screenshot
│   └── nearest_distances_histogram_waterbox.png  # Water simulation analysis
├── Snake_Game/             # Submodule for the Python Snake Game
├── styles/                 # SCSS and compiled CSS files
│   ├── _media.scss        # Media query styles
│   ├── styles.css         # Compiled CSS
│   ├── styles.css.map     # CSS source map
│   └── styles.scss        # Main SCSS file
├── TIP3P-Water-Sim/       # Submodule for the TIP3P Water Simulation project
├── VBA_Automation/         # Submodule for the VBA Automation project
└── openmm-vmd-membrane-transport-overview/  # Submodule for membrane transport simulation
```

## Submodules

This project uses Git submodules to include external repositories for specific projects:

*   **VBA_Automation:** Excel automation macros and documentation
*   **TIP3P-Water-Sim:** Molecular dynamics water simulation project
*   **openmm-vmd-membrane-transport-overview:** Membrane transport simulation prototype

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
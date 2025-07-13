# Ryan Cooley Portfolio Website

This is the source code for my personal portfolio website, featuring my projects in scientific programming, web development, and more. The site is built with HTML, CSS, and JavaScript, and is designed to showcase both my technical and scientific skills.

## Featured Project: TIP3P Water Box Simulation

This project demonstrates a molecular dynamics simulation of a TIP3P water box using OpenMM and AmberTools. The code and analysis scripts provided here allow you to reproduce the simulation, analyze the results, and visualize the distribution of nearest-neighbor distances between water molecules.

### Included Files
- `tip3p_molecular_dynamics_simulation.py` — Main simulation script (OpenMM)
- `tip3p_water_box_setup.leap` — Leap script for water box setup (AmberTools)
- `tip3p_distance_analysis.py` — Analyze nearest-neighbor distances
- `tip3p_periodic_boundary_analysis.py` — Analyze distances with periodic boundary conditions
- `tip3p_data_visualization.py` — Generate a professional histogram of the results
- `tip3p/nearest_distances_histogram_waterbox.png` — Example output graph
- `tip3p/trajectory.gif` — Animated visualization of the simulation

### How to Run the Simulation and Analysis
1. **Install dependencies:**
   ```bash
   pip install openmm parmed numpy matplotlib mdtraj
   ```
   AmberTools (for `tleap`) is also required for the setup step.

2. **Set up the water box:**
   ```bash
   tleap -f tip3p_water_box_setup.leap
   ```

3. **Run the molecular dynamics simulation:**
   ```bash
   python tip3p_molecular_dynamics_simulation.py
   ```

4. **Analyze the results:**
   ```bash
   python tip3p_distance_analysis.py
   python tip3p_periodic_boundary_analysis.py
   ```

5. **Visualize the data:**
   ```bash
   python tip3p_data_visualization.py
   ```
   The output histogram will be saved as `tip3p/nearest_distances_histogram_waterbox.png`.

6. **Visualize the trajectory:**
   Use VMD or similar software to view the generated trajectory files.

## Website Structure
- `index.html` — Main portfolio page with project modals
- `styles/` — CSS styles
- `app.js` — JavaScript for navigation and modals
- `img/` — Images for the site and projects
- `tip3p/` — Project images and analysis output

## Live Site
You can view the live portfolio at: [GitHub Pages URL]

---

If you have any questions or want to collaborate, feel free to reach out!


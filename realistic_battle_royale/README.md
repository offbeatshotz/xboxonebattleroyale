# Realistic Battle Royale (Python)

A high-performance, realistic battle royale game built with Python. Designed for PC and Xbox Series.

## Features
- **Ultra HD 4K HDR**: High-fidelity rendering with HDR support for modern displays.
- **Cross-Platform Play**: Full cross-play support for PC, Xbox One/Series, and PS5.
- **Unified Input**: Support for Keyboard/Mouse and Gamepads (Xbox/DualSense).
- **Realistic Graphics & Physics**: Powered by Ursina Engine (Panda3D) with 4K shadow maps.

## Cross-Platform Deployment
### PC (Windows/Linux)
Run directly via Python or package using `ursina build` or `PyInstaller`.

### Xbox One & Series X|S
1. **Developer Mode**: Enable Developer Mode on your Xbox.
2. **Panda3D UWP**: Use the [Panda3D UWP port](https://github.com/panda3d/panda3d) to package the Python scripts as a Universal Windows Platform (UWP) app.
3. **Deployment**: Sideload the `.appx` package to the console via the Xbox Device Portal.

### PlayStation 5 (PS5)
1. **SDK Access**: Requires Sony DevKit access.
2. **Interpreter Embedding**: Embed the Python interpreter within a C++ wrapper using the PS5 SDK.
3. **Networking**: Ensure the `socket` library is linked against PS5 networking modules.

## GitHub Hosting
This project uses the `docs/` directory for GitHub Pages hosting. 
To host your own download portal:
1. Push this repository to GitHub.
2. Go to **Settings** > **Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select the `main` branch and the `/docs` folder as the source.
5. Click **Save**.
6. Your hosted download page will be available at `https://<your-username>.github.io/<repo-name>/`.
- **250 Player Matches**: Custom networking architecture for high-capacity games.
- **Squad Play**: Support for up to 6 players per squad.
- **Massive Maps**: 10 maps of various sizes (Big & Medium).
- **Advanced Weapon System**: 4-5 attachment slots per weapon.
- **Diverse Vehicles**: Cars, motorcycles, bikes, gliders, and boats.
- **In-Game Store**: Easy-to-earn currency and crate system.

## Project Structure
- `client/`: Game client code (Ursina).
- `server/`: Dedicated server logic.
- `shared/`: Shared data models and constants.
- `assets/`: 3D models, textures, and realistic sounds.

## Requirements
- Python 3.10+
- Ursina Engine
- Panda3D
- Socket/Networking libraries

## Getting Started
(Detailed instructions coming soon)

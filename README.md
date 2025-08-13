# Bit - Interactive TRON Character

![Bit Character](https://img.shields.io/badge/TRON-Bit-00FFFF?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMjIgMTJMMTIgMjJMMiAxMkwxMiAyWiIgZmlsbD0iIzAwRkZGRiIvPgo8L3N2Zz4K)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://seheart.github.io/bit/)

An interactive recreation of **Bit**, the iconic geometric character from Disney's TRON (1982). Experience the binary companion with authentic movie sounds, geometric transformations, and classic Grid aesthetics.

## 🎮 Live Demo

**[▶️ Try Bit Interactive](bit-tron-character.html)**

*Open the HTML file in your browser to interact with Bit!*

## ✨ Features

### 🎯 Authentic TRON Experience
- **Geometric Transformations**: Faithful recreation of Bit's three states
  - **Neutral**: Blue/cyan compound polyhedron (dodecahedron + icosahedron)
  - **YES**: Yellow/orange octahedron with upward transformation
  - **NO**: Red stellated icosahedron with aggressive animation
- **Original Movie Sounds**: Crystal-clear audio extracted from TRON (1982)
- **TRON Aesthetics**: Grid background, neon glow effects, and authentic color palette

### 🎮 Interactive Controls
- **Click Bit**: Random Yes/No response
- **Keyboard Shortcuts**:
  - `Y` - YES response
  - `N` - NO response  
  - `Space` - Random response
  - `E` - Excite Bit (rapid responses like in the movie!)
- **Button Controls**: Ask questions and trigger responses

### 🎨 Visual Effects
- **Particle Systems**: Color-matched particles on each response
- **Smooth Animations**: CSS3 transforms with easing
- **Responsive Design**: Works on desktop and mobile
- **Floating Animation**: Continuous gentle movement
- **Grid Environment**: Classic TRON wireframe background

### 🔊 Audio System
- **High-Quality MP3**: Crystal clear movie audio
- **Fallback System**: Generated sounds if audio fails
- **Multiple Response Patterns**: Single responses and rapid sequences

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/seheart/bit.git
   cd bit
   ```

2. **Open in browser**:
   ```bash
   open bit-tron-character.html
   # or
   python -m http.server 8000  # for local server
   ```

3. **Interact with Bit**:
   - Click the character or use keyboard shortcuts
   - Watch the geometric transformations
   - Listen to authentic TRON sounds

## 📁 Project Structure

```
bit/
├── bit-tron-character.html    # Main interactive character
├── bit-yes.mp3               # YES sound (crystal clear)
├── bit-no.mp3                # NO sound (crisp quality)
├── bit-yes-original.mp3      # Original YES audio (backup)
├── bit-yes-crystal.mp3       # Processed YES audio (intermediate)
└── README.md                 # This file
```

## 🎵 Audio Processing

The audio files have been professionally processed for optimal quality:

- **Frequency Filtering**: High-pass (500Hz) and low-pass (4kHz) for clarity
- **Noise Reduction**: Removed background distortion and artifacts  
- **Loudness Normalization**: Balanced volume levels
- **Precision Timing**: Trimmed for perfect response timing
- **High Bitrate**: 320kbps MP3 for maximum quality

## 🎬 Character Behavior

Bit faithfully recreates the movie character's behavior:

### Responses
- **Binary Communication**: Only says "YES!" and "NO!"
- **Emotional Expression**: Conveys excitement through repetition
- **Geometric Language**: Shape changes communicate meaning

### States
- **Calm**: Gentle floating and rotation in neutral form
- **Excited**: Rapid transformations with "YES YES YES YES!"
- **Alarmed**: Sharp red spikes with "NO NO NO NO!"

## 🔧 Technical Implementation

### Frontend Technologies
- **HTML5**: Semantic structure and audio elements
- **CSS3**: Advanced animations, transforms, and visual effects
- **Vanilla JavaScript**: Interactive controls and audio management
- **Web Audio API**: Sound generation fallbacks

### Performance Features
- **Hardware Acceleration**: CSS3 transforms using GPU
- **Optimized Audio**: Preloaded with fallback systems
- **Responsive Design**: Scales across devices
- **Particle Optimization**: Efficient DOM manipulation

## 🎨 Visual Design

### Color Palette
- **Primary**: `#00FFFF` (Cyan Grid)
- **YES State**: `#FFFF00` (Yellow Energy)
- **NO State**: `#FF0000` (Red Alert)
- **Background**: Radial gradient from `#001133` to `#000011`

### Animations
- **Transform Timing**: `cubic-bezier(0.68, -0.55, 0.265, 1.55)` for bounce
- **Particle Physics**: Randomized trajectories with fade-out
- **Grid Pulse**: Breathing effect on background grid

## 📚 TRON Lore

Bit is a sentient program from the digital Grid, serving as a binary companion to other programs. Despite only being able to communicate "Yes" and "No," Bit displays remarkable emotional range and intelligence, becoming one of the most memorable characters in TRON through innovative computer graphics and expressive animation.

## 🛠️ Development

### Local Development
```bash
# Serve locally for testing
python -m http.server 8000
# or
npx serve .
```

### Audio Editing
The project includes processed audio files. To modify:
```bash
# Example processing with ffmpeg
ffmpeg -i input.mp3 -af "highpass=f=500,lowpass=f=4000,loudnorm" output.mp3
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is a fan recreation for educational and entertainment purposes. TRON and Bit are trademarks of The Walt Disney Company.

## 🙏 Acknowledgments

- **Disney/TRON**: Original character and design
- **Claude Code**: Interactive implementation and audio processing
- **TRON (1982)**: Source material and inspiration
- **Vector Graphics**: Mathematical precision in geometric design

## 🔗 Links

- **Live Demo**: [GitHub Pages](https://seheart.github.io/bit/)
- **Wiki**: [Project Wiki](https://github.com/seheart/bit/wiki)
- **Issues**: [Report Issues](https://github.com/seheart/bit/issues)
- **TRON on IMDb**: [TRON (1982)](https://www.imdb.com/title/tt0084827/)

---

**"YES!"** - *Bit, TRON (1982)*

*End of line.*
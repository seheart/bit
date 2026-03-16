# Bit — Interactive TRON Character

An interactive recreation of **Bit**, the geometric character from Disney's TRON (1982). Bit can only say "YES" or "NO", morphing between three polyhedral states with authentic movie sounds.

**[Live Demo](https://seheart.github.io/bit/)**

## Controls

| Input | Action |
|-------|--------|
| Click canvas | Random response |
| `Y` | YES |
| `N` | NO |
| `Space` | Random |
| `E` | Excite (rapid 5x) |

## Geometric States

- **Neutral** — Stellated icosahedron (cyan). 20-face icosahedron with triangular spike pyramids on each face, producing 60 visible faces.
- **YES** — Octahedron (yellow). 8-face regular octahedron.
- **NO** — Stellated dodecahedron (red). Pentagonal faces with long aggressive spikes.

See [MATHEMATICS.md](MATHEMATICS.md) for the full geometric and mathematical analysis.

## Project Structure

```
bit/
  index.html          # Single-page app (Three.js r128)
  bit-yes.mp3         # YES sound from TRON (1982)
  bit-no.mp3          # NO sound from TRON (1982)
  MATHEMATICS.md       # Geometric analysis
  *.webp              # Reference images
```

## Running Locally

```bash
python -m http.server 8000
# or
npx serve .
```

Open `http://localhost:8000` in your browser.

## License

Fan recreation for educational and entertainment purposes. TRON and Bit are trademarks of The Walt Disney Company.

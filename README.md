![illustration](_app/mtk.png)

# Media Tool Kit

A modular workspace for rapid media file manipulation using Python and industry-standard command-line tools.

## Purpose

This repository is designed for quick, LLM-assisted media processing. Drop in files, describe what you need, and get clean results organized in project folders.

## Tools Used

- **Video**: ffmpeg
- **Image**: ImageMagick  
- **Audio**: SoX (Sound eXchange)
- **Language**: Python 3.8+

## Installation

### macOS (Homebrew)
```bash
brew install ffmpeg imagemagick sox python3
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg imagemagick sox python3 python3-pip
```

### Verify Installation
```bash
ffmpeg -version
convert -version
sox --version
python3 --version
```

## Structure

```
media-tool-kit/
├── projects/       # Individual media processing projects
├── scripts/        # Reusable utility scripts
├── .cursor/rules/  # Cursor IDE rules and guidelines
└── README.md
```

## Workflow

1. Drop media files into the root or describe what you need
2. AI assistant creates organized project folder in `projects/`
3. Processing happens with clear logging
4. Results saved to project's `output/` directory
5. Commands logged for reproducibility

## Getting Started

Just describe what you want to do with your media files. Examples:

- "Compress this video to under 10MB"
- "Convert all these images to PNG"
- "Extract audio from this video and normalize it"
- "Trim this video from 1:30 to 2:45"

The workspace stays clean, originals stay safe, and everything is organized.

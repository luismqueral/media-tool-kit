![illustration](_app/mtk.png)

**Media Tool Kit** is [my personal framework](http://www.queral.studio) for media manipulation. It's designed for LLM's within generative coding environments to quickly, and consistently, images, sounds, and video.

The idea is to quickly make edits to media by just asking it.

"Compress this video to 10MB" or "Remove transparency". That kind of stuff.

## Tools Used
This is python-centric workspace. Scripts created in this workspace will leverage the following frameworks.
- **Video**: ffmpeg
- **Image**: ImageMagick  
- **Audio**: SoX (Sound eXchange)

I expect this list to grow over time, but for now this will do.

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

### Project Structure

Each new project should be listed in the `projects/` directory and carry a consistent structure:

```
projects/
└── [project-name]/
    ├── input/          # Source/original files
    ├── output/         # Processed results
    └── README.md       # What was done, commands used
```

This keeps work organized, originals safe, and makes it easy to reproduce or reference past work.

## Getting Started

Just describe what you want to do with your media files. Examples:

- "Convert all these images to PNG"
- "Extract audio from this video and normalize it"
- "Trim this video from 1:30 to 2:45"


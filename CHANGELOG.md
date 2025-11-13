# Changelog

All notable changes to the media-tool-kit project will be documented here.

## 2025-11-13

- improved README intro wording for better clarity ("make modifications to images, sounds, and video quickly and consistently")
- added link to queral.studio in README intro, changing "a personal framework" to "my personal framework" with link
- configured git to automatically switch between personal (luismqueral) and work (luis-nyt) identities based on directory location
- added comprehensive automated changelog maintenance guidelines to cursor rules with branch organization and category templates
- fixed git config email to use verified GitHub email (luismqueral@gmail.com) so commit avatar displays correctly
- updated README with project structure documentation showing input/output directory organization for consistent project layouts
- added "Rule of Three" philosophy to cursor rules - don't create reusable scripts until a pattern emerges after 2-3 uses, avoiding premature abstraction
- clarified when to create scripts in scripts/ directory vs keeping commands in project folders for one-off operations
- created initial project structure with cursor rules for LLM-assisted media processing workflow
- established modular organization pattern with projects/ and scripts/ directories to keep workspace clean
- added cursor rules in .cursor/rules/general-rules.mdc defining Python-first approach with ffmpeg, ImageMagick, and SoX as primary tools
- set up project guidelines emphasizing modularity, direct tool usage, and original file preservation
- created README.md with installation instructions and workflow overview
- added requirements.txt with minimal Python dependencies (prefer subprocess calls to heavy wrappers)
- configured .gitignore to exclude media files and build artifacts


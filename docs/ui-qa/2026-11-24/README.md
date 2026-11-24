# Readable Typography UI verification

24 November 2026. Tested with Obsidian 1.15.1 for Windows and a local vault containing synthetic notes, a Canvas board and a Base. The baseline was theme 3.6.1 at commit `f75a3b4`. The source under test after the fix was theme 3.6.2.

## Accent color fix

In 3.6.1, choosing `#c83838` in **Settings > Appearance > Accent color** saved the selection. Internal links and accent controls continued to use the theme's blue. The stylesheet now uses the selected color for links, controls, focus and selection. It adjusts the color's lightness for the active scheme and sets the contrasting foreground against accent fills.

The rerun applied red, bright yellow and deep blue through the native control in each scheme. In all six combinations, the accent against the note background and text against the accent button fill measured at least 5.45:1. **Restore default** brought back each scheme's original color.

## Desktop editor focus

In Source mode and Live Preview, the focus outline shared the left edge of the first glyph. The editor now has 8 px of inside padding on desktop. The Source mode rerun checked the measured text inset and saved and undid a keyboard edit.

## Checks

The 14 desktop UI checks and six stylesheet tests passed.

| Area | Verified in Obsidian |
| --- | --- |
| Appearance | Default and Readable Typography selection, dark and light schemes, system mode, three custom colors in each scheme and reset |
| Fonts | Interface, text and monospace pickers with local fonts, font size from 16 px to 22 px and back, quick font size adjustment toggle |
| Reading | Heading line-height, readable width of 65 ch and its toggle, paragraphs, nested and ordered lists, task edits, links, mixed scripts, table and callout |
| Editing | Source mode, Live Preview, selection, keyboard focus, and a saved edit followed by Undo |
| Navigation | File list, keyboard focus, internal link and Back, search matches and empty results, note menu and Escape |
| Workspace | Canvas cards and embedded notes, Bases table and property values |

## Screenshots

These WebP files capture the live Obsidian renderer using the synthetic vault. The main window captures are 1024 × 800 pixels and the Settings capture is 900 × 700 pixels.

| Capture | UI state |
| --- | --- |
| [01 Dark reading](01-dark-reading.webp) | Markdown reading view with properties, prose, links and nested bullets |
| [02 Light enlarged text](02-light-large-text.webp) | Reading view after setting the note font size to 22 px |
| [03 Light mixed scripts](03-light-mixed-scripts.webp) | Latin, Greek, Arabic, Japanese and Devanagari text with a table, callout and code |
| [04 Light source editor](04-light-source-editor.webp) | Raw Markdown and keyboard editing |
| [05 Light Live Preview](05-light-live-preview.webp) | Edited note in Live Preview with text selection |
| [06 Dark Appearance](06-dark-appearance-custom-accent.webp) | Active theme and a custom red accent |
| [07 Dark search](07-dark-search.webp) | Search panel with matching text in the active vault |
| [08 Dark note menu](08-dark-note-menu.webp) | Note actions menu and active reading pane |
| [09 Dark Canvas](09-dark-canvas.webp) | Board with embedded Markdown and connected cards |
| [10 Dark Bases](10-dark-bases.webp) | Native table for indexed notes and their properties |

The run covered Windows desktop. Mobile, macOS and Linux were outside this run. The theme was installed from the checkout in the local fixture.

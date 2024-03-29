### Setup

Execute `pip install -r requirements.txt` in this folder

### How to extract the canvas

1. Go to `view-source:https://adventofcode.com/{year you want}`, for example `view-source:https://adventofcode.com/2015`
2. Copy the whole thing (<kbd>Ctrl + A</kbd> then <kbd>Ctrl + C</kbd>)
3. Paste the content into `page.html` file
4. Run `canvas.py` and hope everything works
5. The canvas will be in the `canvas.svg` file (`canvas.html` is also created for debugging)


### Known issues

- The HTML debug-preview page does not properly set the `span` height for 2023, causing the lava falls and other effects to move down one `line_height`. However, the resulting SVG image does not have this problem.

- For 2020 if you want to have Storm, you'll need in add manually it to `page.html`, because it is calculated randomly in runtime using JavaScript (and my script does support that). Don't forget that there should not be a line break between the last `<a>` and the storm's `<div>`, otherwise there will be an empty line at the bottom.

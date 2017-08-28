# new-hampshire-wildlife-guide

This is a two part project that in the end assembles a wildlife guide for New Hampshire sourced from the data on http://amc-nh.org/resources/guides/.

## Output

Here's a screenshot of what the guide looks like.
![Screenshot of wildlife guide](./screenshot.png)

The final output is too big to host on GitHub (300+MB of wildlife photographs) but is hosted on my (Drive)[https://drive.google.com/open?id=0B43OdhDUo9n7anRmcnI0aWtEY00].

## To use

### Web scraper

The first part of generating the wildlife guide PDF involves scraping the site for all of its images and textual information on the wildlife. The script to do this is the `scraper.py` python file. This will save all the scraped data to the `data` folder.

* `python scraper.py`

### LaTeX guide builder

The second part is to assemble all the scraped data into a PDF wildlife guide using Lua and LaTeX (LuaTeX). The assembly script is located inside the `guide.tex` file. To run this file, you'll need to have LuaTeX installed.

* `lualatex guide.tex`
* `./cleanup.sh` (optional)



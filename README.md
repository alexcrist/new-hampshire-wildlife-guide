# new-hampshire-wildlife-guide

This is a two part project that in the end assembles a wildlife guide for New Hampshire sourced from the data on http://amc-nh.org/resources/guides/.

The first part involves scraping the site for all of its images and textual information on wildlife. The script to do this is the `scraper.py` python file. This will save all the scraped data to the `data` folder.

The second part is to assemble all the scraped data into a PDF wildlife guide using Lua and LaTeX (LuaTeX). The assembly script is located inside the `guide.tex` file. To run this file, you'll need to have LuaTeX installed which can be kind of a pain.

## To use

### Web scraper

* `python scraper.py`

### LaTeX guide builder

* `lualatex guide.tex`
* `./cleanup.sh`

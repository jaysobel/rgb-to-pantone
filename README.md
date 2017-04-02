# RGB to Pantone Mapping

This repository holds a pickled python dictionary of the 1,761 solid coated pantone colors and corresponding rgb values as {rgb : pantone} pairs. The dictionary was produced by scraping the hex background colors from the [rgb.to](http://rgb.to/pantone/coated/page/1) pantone website.

#Note
There is no direct rgb-to-pantone mapping. Photoshop is the most common way to search for individual suitable pantone colors. This repository is intended to help with larger batch mappings that do not require a high degree of precision.

The two python scripts are the scraper and a demo find_closest function which uses the pickled dictionary. The find_closest function takes r, g and b parameters and returns the string of the nearest pantone color using euclidean distance.

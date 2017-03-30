# RGB to Pantone Mapping

This repository holds a pickled python dictionary of the 1,761 solid coated pantone colors and corresponding rgb values as {rgb : pantone} pairs. The dictionary was produced by scraping the hex background colors from the [rgb.to](http://rgb.to/pantone/coated/page/1) pantone website.

Note that there is not precise rgb-pantone mapping, and that these correspondances are not official.

The python scripts are the scraper and a small demo of how the dictionary can be used to find the closest pantone color to a given r, g, b triplet using euclidean distance.

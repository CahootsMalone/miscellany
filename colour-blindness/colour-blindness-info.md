# Colour Blindness Notes

## General Information

* https://en.wikipedia.org/wiki/Color_blindness
  * Deuteranopia (red/green): 6% of males
  * Protanopia (red/green): 2% of males
  * Tritanopia (blue/yellow): <0.01% of people (equally prevalent in both males and females)

* [Worldwide prevalence of red-green color deficiency (Birch 2012)](https://pubmed.ncbi.nlm.nih.gov/22472762/)

* Resources from [DaltonLens](https://daltonlens.org/), a project by  Nicolas Burrus, who has protanopia:
  * [Online Color Blindness Simulators](https://daltonlens.org/colorblindness-simulator)
    * Online versions of notable colour blindness simulations. An excellent demonstration of the differences in the results of the various algorithms.
  * https://github.com/DaltonLens/DaltonLens-Python
    * Python implementation of various colur blindness simulation algorithms.
  * [Review of Open Source Color Blindness Simulations](https://daltonlens.org/opensource-cvd-simulation/)
    * By far the most thorough discussion of this subject I've been able to find.
    * [Let's collectively determine the best color blindness simulation method! (Reddit thread)](https://www.reddit.com/r/ColorBlind/comments/qzkl7h/lets_collectively_determine_the_best_color/)
    * [So which one should we use?](https://daltonlens.org/opensource-cvd-simulation/#So-which-one-should-we-use?) section

* [Computerized simulation of color appearance
for dichromats (Brettel et. al. 1997)](http://vision.psychol.cam.ac.uk/jdmollon/papers/Dichromatsimulation.pdf)

* https://www.reddit.com/r/ColorBlind/
  * Examples of graphics that aren't colour-blind-safe are shared here.

## Palettes

* [Coloring for Colorblindness (David Nichols)](https://davidmathlogic.com/colorblind)
    * This page contains live simulations of three forms of colour blindness, but no details are provided regarding the algorithms used. The code is minified and I didn't de-minify it to review it.
    * The default four-colour palette this page loads with performs well (i.e., the colours are distinguishable) in the different simulations:
      * #D81B60
      * #1E88E5
      * #FFC107
      * #004D40

* [Colorblind Safe Color Schemes (NCEAS Science Communication Resource Corner)](https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf)

* [colorBlindness Guide: Collection of safe colors (R library documentation)](https://cran.r-project.org/web/packages/colorBlindness/vignettes/colorBlindness.html#Collection_of_safe_colors)

* [Color Blindness (IBM Design Language)](https://www.ibm.com/design/language/color/#color-blindness)
  * Good simulated example
  * No evidence of the colour-blind-safe palette people refer to elsewhere
    * Appears on an older page that was taken down ([Internet Archive link](https://web.archive.org/web/20180503023309/https://www.ibm.com/design/language/resources/color-library)). The palette colours (and their IBM-assigned names) are:
      * Ultramarine 40: #648fff
      * Indigo 50: #785ef0
      * Magenta 50: #dc267f
      * Orange 40: #fe6100
      * Gold 20: #ffb000

* [Choosing color palettes (docs for Seaborn Python library for data visualization)](https://seaborn.pydata.org/tutorial/color_palettes.html)

## In-Browser Simulations

* [Firefox](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/simulation/index.html)
* [Chrome](https://developer.chrome.com/blog/new-in-devtools-83#vision-deficiencies)
  * `Ctrl/Cmd + Shift + I` to open the dev tools, `Ctrl/Cmd + Shift + P` to open the Command Menu, enter "rendering", [open the Rendering tab](https://developer.chrome.com/docs/devtools/rendering#open-rendering), and scroll down to "Emulate vision deficiencies".
  * [Implementation details](https://developer.chrome.com/docs/chromium/cvd)
      * > You might be wondering where the exact numbers in our example come from. What makes this color matrix a good approximation of deuteranopia? The answer is: science! The values are based on [a physiologically accurate color vision deficiency simulation model by Machado, Oliveira, and Fernandes](https://www.inf.ufrgs.br/%7Eoliveira/pubs_files/CVD_Simulation/CVD_Simulation.html).
* [Edge](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/accessibility/test-color-blindness)

## Simulations within Graphics Software

* GIMP
  * *View > Display Filters > Color Deficient Vision* ([docs](https://docs.gimp.org/2.10/en/gimp-display-filter-dialog.html))
  * [Source code](https://gitlab.gnome.org/GNOME/gimp/-/blob/master/modules/display-filter-color-blind.c)
    * Uses algorithm from Brettel 1997 paper.

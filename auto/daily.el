(TeX-add-style-hook
 "daily"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("ulem" "normalem") ("xcolor" "table") ("standalone" "subpreambles=true") ("hyperref" "linktocpage=true") ("babel" "portuguese" "english") ("inputenc" "latin1" "utf8")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "report"
    "rep10"
    "inputenc"
    "fontenc"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref"
    "paralist"
    "tcolorbox"
    "xcolor"
    "lipsum"
    "caption"
    "tabu"
    "standalone"
    "import"
    "setspace"
    "graphics"
    "tocloft"
    "minitoc"
    "babel"
    "subfig")
   (LaTeX-add-labels
    "sec:org5e5b2cb"
    "sec:org71c6115"
    "sec:orgc699158"
    "sec:org89b3a29"
    "sec:orgf3cc546"
    "sec:org7cac1ed"))
 :latex)


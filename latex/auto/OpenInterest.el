(TeX-add-style-hook
 "OpenInterest"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "article" "crop=false")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("xcolor" "table")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "fontenc"
    "inputenc"
    "lmodern"
    "textcomp"
    "lastpage"
    "xcolor"))
 :latex)


(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt" "a4paper" "toc=flat")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("flowfram" "pages=absolute") ("xcolor" "table") ("datetime2" "en-GB")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "geometry"
    "flowfram"
    "xcolor"
    "fancyhdr"
    "graphics"
    "hyperref"
    "minitoc"
    "datetime2"
    "setspace")
   (TeX-add-symbols
    '("member" 4)
    "headr"
    "footl")
   (LaTeX-add-xcolor-definecolors
    "slcolor"
    "color1"
    "color2"))
 :latex)


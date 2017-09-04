;;;Commentary;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Publishing definitions for project daily
;; data: 14/03/2017
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(setq org-publish-project-alist
      '(("html-daily"
         :base-directory "./"
         :base-extension "org"
         :exclude: "config/.\\| org/agenda.org\\| org/body.org"
         :include: "./org/highlights.org"
         :publishing-directory "./public_html/"
         :recursive t
         :with-tags nil
         :org-html-postanble nil
         :org-html-head-include-scripts nil
         :org-html-head-include-default-style nil
         :publishing-function org-html-publish-to-html
         :preparation-function project-prepare-html
         )
        ("static-daily"
         :base-directory "./static/"
         :base-extension "css\\|js\\|png\\|jpg\\|gif\\|pdf"
         :publishing-directory "./public_html/static/"
         :recursive t
         :publishing-function org-publish-attachment
         )
        ("tex-daily"
         :base-directory "./org/"
         :base-extension "org"
         :exclude "body.org\\|agenda.org"
         :publishing-directory "./latex/"
         :with-toc nil
         :publishing-function org-latex-publish-to-latex)
        ("pdf-daily"
         :base-directory "./"
         :base-extension "org"
         :publishing-directory "./public_pdf/"
         :with-tags nil
         :exclude-tags nil
         :publishing-function org-latex-publish-to-pdf
         )
        ("html" :components ("html-daily" "static-daily"))
        ("pdf" :components ("pdf-daily" "tex-daily"))
        )
      )


(defun project-prepare-html (options)
  (call-process-shell-command "pandoc" nil t nil "./org/highlights.org -f org -t html -o ./html/highlights.html")
  ;; (setq org-export-exclude-tags '("noexport"))
  )

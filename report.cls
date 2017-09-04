% Class information
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{report}[2017/01/05 Class for BGCs daiy]

% Loads
\LoadClass[11pt, a4paper, toc=flat]{article}
\RequirePackage{geometry}
\RequirePackage[pages=absolute]{flowfram}
\RequirePackage[table]{xcolor}
\RequirePackage{fancyhdr}
\RequirePackage{graphics}
\RequirePackage{hyperref}
\RequirePackage{minitoc}
\RequirePackage[en-GB]{datetime2}
\RequirePackage{setspace}


%% Options
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

%% Margins
\geometry{textwidth=18.5cm, left=1.5cm, top=1.5cm, textheight=25.0cm,
  headheight=1.0cm, marginparwidth=0.5cm, headsep=3.6cm,
  height=28cm, footskip=1.0cm}

% frames
\onecolumninarea[1]{0.72\textwidth}{\textheight}{0.28\textwidth}{0pt}
\newdynamicframe[1]{0.25\textwidth}{0.15\textheight}{1pt}{0.84\textheight}[leftUpper]
\newdynamicframe[1]{0.25\textwidth}{0.25\textheight}{0pt}{0.58\textheight}[midUpper]
\newdynamicframe[1]{0.28\textwidth}{0.25\textheight}{-3pt}{0.35\textheight}[midLower]
\newdynamicframe[1]{0.23\textwidth}{0.20\textheight}{0pt}{10pt}[leftLower]



% fonts and colors
\renewcommand{\familydefault}{\sfdefault} % defaul font
\definecolor{slcolor}{HTML}{000066}
\definecolor{color1}{RGB}{0,0,90} % Color of the article title and sections
\definecolor{color2}{RGB}{200,200,200} % Color of the boxes behind the
%\renewcommand{\familydefault}{\phv}

% members boxe
\newcommand*{\member}[4]{
  \begin{spacing}{1.2}
    \scriptsize\it\bf#1 \\
    \footnotesize\it#2 \\
    \scriptsize\it\href{mailto:#3}{#3} \\
    \scriptsize\it#4
  \end{spacing}
  \vspace{0.4cm}
}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% headers and footers
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\setlength\headheight{0.0cm}
\fancypagestyle{plain}
{
  \fancyhf{}
  \lhead{\includegraphics[width=3.2cm]{./images/Logo_Guide.png}}

  \chead {\huge \color{slcolor}\usefont{T1}{fvm}{sb}{n}
    Daily Fixed Income \\
  }
  \rhead{
    \footnotesize \color{slcolor} \usefont{T1}{fvm}{sb}{n}  \today\\
  }
  
  %\newcommand{\footl}{
%     cfoot{\coolor{slcolor}
%       \scriptsize
%       João Maurício Rosal, \it{PhD} \\
%       \scriptsize
%       \Letter\
%       \href{Mailt:jmrosal@guideinvestimentos.com}{jmrosal@guideinvestimentos.com}\\
%       \Telefon\ + 55 11 3576-6613}
% }}
}
  \renewcommand{\headrulewidth}{0.8pt}
  \renewcommand{\headrule}{\hbox to\headwidth{\color{slcolor}\leaders\hrule height \headrulewidth\hfill}}

  \renewcommand{\footrulewidth}{0.4pt}
  \renewcommand{\rule}{\hbox to\headwidth{\color{slcolor}\leaders\hrule height \headrulewidth\hfill}}

\pagestyle{fancy}

\lhead{\includegraphics[width=3.2cm]{./images/Logo_Guide.png}}

\newcommand{\headr}{
  \rhead{\footntesize \color{slcolor} \userfont{T1}{fvm}{sb}{n} Daily Fixed Income}
}

\newcommand{\footl}{
  \lhead{\footntesize \color{slcolor} \userfont{T1}{fvm}{sb}{n}
}}


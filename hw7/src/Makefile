HW = hw6
Q = questions/question_
QUESTIONS = 
UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
    PDFLATEX = pdflatex --shell-escape
    LATEX = latex --shell-escape
    BIBTEX = bibtex
endif
ifeq ($(UNAME), Darwin)
    PDFLATEX = /Library/TeX/texbin/pdflatex --shell-escape
    LATEX = /Library/TeX/texbin/latex --shell-escape
    BIBTEX = /Library/TeX/texbin/bibtex
endif

.PHONY: $(HW).pdf
$(HW).pdf: $(HW).dvi
	$(PDFLATEX) $(HW).tex && mv $(HW).pdf ../dist

$(HW).dvi: $(HW).tex $(QUESTIONS)
	$(LATEX) $(HW).tex

citations: $(HW).bbl

$(HW).bbl: $(HW).bib
	$(BIBTEX) $(HW) && $(LATEX) $(HW).tex && $(LATEX) $(HW).tex




clean:
	rm $(HW).pdf $(HW).dvi $(HW).aux $(HW).log $(HW).bbl $(HW).blg

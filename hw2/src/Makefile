HW = hw2
Q = questions/question_
QUESTIONS =  $(Q)1.tex $(Q)2.tex $(Q)3.tex $(Q)4.tex $(Q)5.tex $(Q)6.tex $(Q)7.tex
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

$(HW).pdf: $(HW).dvi
	$(PDFLATEX) $(HW).tex

$(HW).dvi: $(HW).tex $(QUESTIONS)
	$(LATEX) $(HW).tex

citations: $(HW).bbl

$(HW).bbl: $(HW).bib
	$(BIBTEX) $(HW) && $(LATEX) $(HW).tex && $(LATEX) $(HW).tex



$(Q)1.tex:


$(Q)2.tex:


$(Q)3.tex:


$(Q)4.tex:


$(Q)5.tex:


$(Q)6.tex:


$(Q)7.tex:



clean:
	rm $(HW).pdf $(HW).dvi $(HW).aux $(HW).log $(HW).bbl $(HW).blg

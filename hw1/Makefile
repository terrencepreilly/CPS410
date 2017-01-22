HW = hw1
Q = questions/question_
QUESTIONS =  $(Q)1.tex $(Q)2.tex $(Q)3.tex $(Q)4.tex $(Q)5.tex $(Q)6.tex
UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
    PDFLATEX = latex
    LATEX = latex
endif
ifeq ($(UNAME), Darwin)
    PDFLATEX = /Library/TeX/texbin/pdflatex
    LATEX = /Library/TeX/texbin/latex
endif

$(HW).pdf: $(HW).dvi
	$(PDFLATEX) $(HW).tex

$(HW).dvi: $(HW).tex $(QUESTIONS)
	$(LATEX) $(HW).tex


$(Q)1.tex:


$(Q)2.tex:


$(Q)3.tex:


$(Q)4.tex:


$(Q)5.tex:


$(Q)6.tex:



clean:
	rm $(HW).pdf $(HW).dvi $(HW).aux $(HW).log

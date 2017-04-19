# Each of the following uses different commands,
# etc. for compiling a dot file.
circles =
dot =
fdp =
neato =
patchwork =
twopi =

.PHONY: all
all: $(circles) $(dot) $(fdp) $(neato) $(patchwork) $(twopi)
	python convert.py # && rm -f $(dots)

$(circles): %.png: %.dot
	circo -Tpng %< -o $@

$(dot): %.png: %.dot
	dot -Tpng $< -o $@

$(fdp): %.png: %.dot
	fdp -Tpng $< -o $@

$(neato): %.png: %.dot
	neato -Tpng $< -o $@

$(patchwork): %.png: %.dot
	patchwork -Tpng $< -o $@

$(twopi): %.png: %.dot
	twopi -Tpng $< -o $@

.PHONY: clean
clean:
	rm -f $(dots) $(fdps) $(circles) *.eps

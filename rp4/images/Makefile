fdps =
dots = pylaga.png object_models.png
circles =

all: $(fdps) $(dots) $(circles)
	python convert.py # && rm -f $(dots)

$(fdps): %.png: %.dot
	fdp -Tpng $< -o $@

$(dots): %.png: %.dot
	dot -Tpng $< -o $@

$(circles): %.png: %.dot
	circo -Tpng $< -o $@

clean:
	rm -f $(dots) $(fdps) $(circles) *.eps
# process:
# 	fdp -Tpng process.dot -o process.png

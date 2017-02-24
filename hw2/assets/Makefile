fdps =
dots = object_models.png functional_models.png dynamic_models.png
circles =

all: $(fdps) $(dots) $(circles)
	python convert.py

$(fdps): %.png: %.dot
	fdp -Tpng $< -o $@

$(dots): %.png: %.dot
	dot -Tpng $< -o $@

$(circles): %.png: %.dot
	circo -Tpng $< -o $@

clean:
	rm -f *.png
# process:
# 	fdp -Tpng process.dot -o process.png

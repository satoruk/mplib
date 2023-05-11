.PHONY: run install deps
run:
	- mpremote run main.py
install: deps
	mpremote cp main.py :
deps:
	mpremote mip install github:satoruk/mplib/app/gram_scale
	mpremote mip install github:satoruk/mplib/lcd/hd44780/simple
	mpremote mip install github:satoruk/mplib/load_cell/hx711/simple
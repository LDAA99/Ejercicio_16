albumgraf: albumgraf.py
	python albumgraf.py

laminas.txt: album
	./album > laminas.txt

album: album.cpp
	c++ album.cpp -o album


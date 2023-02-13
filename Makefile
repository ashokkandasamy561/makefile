build:
	cd build
	./program.o
	python3 plot.py


program.o:
	mkdir -p build
	cd source
	g++ program.cpp -o program.o
	mv program.o build/
	cd ../
plot.o:
	python3 plot.py

clean:
	rm -rf *.o build

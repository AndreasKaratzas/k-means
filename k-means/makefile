CC = g++
CXXFLAGS = -Wall -funroll-loops -lrt -Ofast -fopt-info-vec-optimized -funsafe-math-optimizations -march=native

kmeans: kmeans.o Vec.o Class.o Center.o Distance.o Optimize.o Benchmark.o Interface.o Validation.o
	$(CC) $(CXXFLAGS) -o kmeans kmeans.o Vec.o Class.o Center.o Distance.o Optimize.o Benchmark.o Interface.o Validation.o

kmeans.o: kmeans.cpp kmeans.h Vec.h Class.h Center.h Distance.h Optimize.h Benchmark.h Interface.h Validation.h
	$(CC) $(CXXFLAGS) -c kmeans.cpp

Vec.o: Vec.h Common.h
Class.o: Class.h Common.h
Common.o: Common.h
Center.o: Center.h Common.h
Distance.o: Distance.h Common.h
Optimize.o: Optimize.h Common.h
Benchmark.o: Benchmark.h Common.h
Interface.o: Interface.h Common.h
Validation.o: Validation.h Common.h
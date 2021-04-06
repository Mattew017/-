#include <iostream>
#include <vector>
#include <fstream>
#include <ctime>
#include "Functions.h"
#include "BBO.h"
using namespace std;



int main()
{

	int search_params[] = { -100, 100, 30};
	std::ofstream file;
	unsigned int start_time, end_time;
	file.open("F1.txt");
	std::vector <int> coutOfIterations = { 100, 1000 };
	for (auto countOfIter: coutOfIterations)
	{
		for (size_t PopSize = 5; PopSize < 30; PopSize+=10)
		{
			for (double mp = 0.001; mp < 0.3; mp+= 0.001)
			{
				start_time = clock();
				Result answer = BBO(F1, countOfIter, PopSize, mp, search_params);
				end_time = clock() - start_time; //время выполнения
				std::vector <double> params = answer.params;
				double fit = answer.fitness;
				file << countOfIter << '\t' << PopSize << '\t' << mp << '\t' << fit << '\t';
				for (auto x : params)
					file << x << ';';
				file  << '\t';
				file << end_time << endl;
			}
		}
	}
	file.close();
	
	
}
#pragma once
struct Result
{
	double fitness;
	std::vector <double> params;
};
Result BBO(double (*function) (std::vector <double>), int CountOfIter, int PopSize, double mp, int SearchParams[3]);

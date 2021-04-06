#include <vector>
#include <algorithm>


struct Result
{
	double fitness;
	std::vector <double> params;
};

int randInt(int min, int max) {
	return min + rand() % (max - min + 1);
}

double randDouble(int min, int max) {
	if (max != min) 
		return randInt(++min, max) - rand() / (double)RAND_MAX;
	else
		return randInt(min, max); 
}

std::vector <double> randVector(int dim, int leftBound, int rightBound)
{
	std::vector <double> x; //1st generated population
	for (size_t i = 0; i < dim; ++i)
	{
		double RandNum = randDouble(leftBound, rightBound);
		x.push_back(RandNum);
	}
	return x;
}

double sum(std::vector <double> x)
{
	double result = 0;
	for (auto item : x)
		result += item;
	return result;
}

Result BBO(double (*function) (std::vector <double>), int CountOfIter, int PopSize, double mp, int SearchParams[3])
{
	int leftBound = SearchParams[0];
	int rightBound = SearchParams[1];
	int dimention = SearchParams[2];

	std::vector <double> mu, lamda;
	for (size_t i = 0; i < PopSize; ++i)
	{
		mu.push_back((PopSize + 1 - i) / (PopSize + 1));
		lamda.push_back(1 - mu[i]);
	}

	std::vector <std::vector <double>> Population; //1-ое сгенерированное поколение
	for (size_t i = 0; i < PopSize; ++i)
		Population.push_back(randVector(dimention, leftBound, rightBound));
	//Сортировка по возрастанию по значению функции в векторе
	sort(Population.begin(), Population.end(), [function](const std::vector <double>& first, const std::vector <double>& second)
		{
			return function(first) < function(second);
		});
	//Основная часть работы алгоритма
	for (size_t i = 0; i < CountOfIter; ++i)
	{
		//Миграция
		for (size_t i = 0; i < PopSize; ++i)
		{
			for (size_t j = 0; j < dimention; ++j)
			{
				if (randDouble(0, 1) < lamda[i])
				{
					double randomNumber = randDouble(0, 1) * sum(mu);
					double select = mu[0];
					int selectIndex = 0;
					while ((randomNumber > select) and (selectIndex < PopSize - 1))
					{
						selectIndex += 1;
						select += mu[selectIndex];
					}
					Population[i][j] = Population[selectIndex][j];
				}
				else
					Population[i][j] = Population[i][j];

			}
		}
		//Мутация
		for (size_t i = 0; i < PopSize; ++i)
		{
			for (size_t j = 0; j < dimention; ++j)
			{
				if (mp > randDouble(0, 1))
					Population[i][j] = randDouble(leftBound, rightBound);
			}
		}

		//Сортировка по возрастанию по значению функции в векторе
		sort(Population.begin(), Population.end(), [function](const std::vector <double>& first, const std::vector <double>& second)
			{
				return function(first) < function(second);
			});

	}

	//вектор значений fitness
	std::vector <double> fitness;
	for (auto x : Population)
		fitness.push_back(function(x));

	struct Result result;
	result.fitness = fitness[0];
	result.params = Population[0];
	return result;
}

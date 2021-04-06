#include <vector>
#include  <iostream>
#include <algorithm>

double PI = 3.14;

double F1(std::vector <double> x)
{
	double result = 0;
	for (auto i : x)
		result += i * i;
	return result;
}

double F2(std::vector <double> x)
{
	return *std::max_element(x.begin(), x.end());
}

double F3(std::vector <double> x)
{
	double summ = 0, multi = 1;
	for (auto i : x)
	{
		summ += abs(i);
		multi *= abs(i);
	}
	return summ + multi;
}

double F4(std::vector <double> x)
{
	double square_sum = 0;
	double cos_multi = 1;
	int index = 1;
	for (auto i : x)
	{
		square_sum += i * i;
		cos_multi *= cos(i / index);
		index++;
	}

	return 1 / 4000 * square_sum - cos_multi + 1;
}

double F5(std::vector <double> x)
{
	int dim = x.size(); // dimention of X
	double sum_square = 0;
	double sum_cos = 0;
	for (auto i : x)
	{
		sum_square += i * i;
		sum_cos += cos(2 * PI * i);
	}
	return  -20 * exp(-0.2 * sqrt(sum_square / dim)) - exp(sum_cos / dim) + 20 + exp(1);
}

#include "Center.h"

/**
 * Initializes `Center` variable.
 *
 * @param[in] Vec the dataset generated.
 * @param[in, out] old_Center the random centroids generated in the beginning of the K-means algorithm.
 *
 * @remark [<random> Engines and Distributions](https://docs.microsoft.com/en-us/cpp/standard-library/random?view=msvc-160#engdist)
 */
void init_centers(const std::vector<std::array<float, Nv>>& Vec, std::vector<std::array<float, Nv>>& old_Center)
{
	std::vector<int> Random(N);														///< Declares our random `Vec` generator vector
	std::iota(Random.begin(), Random.end(), 0);												///< Initializes vector with all possible indeces of `Vec`
	std::shuffle(Random.begin(), Random.end(), std::mt19937{ std::random_device{}() });							///< Shuffles `Random` vector
	for (int i = 0; i < Nc; i += 1)
	{
		std::array<float, Nv> Element;													///< Declares a vector `Elements` that temporarily holds the vector chosen from `Vec`					
		Element = Vec.at(Random.at(i));													///< Copies contents of the random `Vec` element
		old_Center.emplace_back(Element);												///< Moves `Element` variable to the `old_Center` variable
	}
}

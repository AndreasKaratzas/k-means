
#include "Optimize.h"

/**
 * Computes `Center` variable after `Classes` correction.
 *
 * @param[in] Vec the dataset.
 * @param[in] Classes the classes corresponding to the dataset.
 * @param[in, out] new_Center the new clusters of the K-means algorithm.
 */
void optimize_center(const std::vector<std::array<float, Nv>>& Vec, std::vector<std::array<float, Nv>>& new_Center, const std::array<std::vector<int>, Nc>& Classes)
{
	new_Center.clear();											///< Clears previously computed data
	for (int i = 0; i < Nc; i += 1)										///< Loops through all clusters
	{
		std::array<float, Nv> Element = { 0 };								///< Initializes `Element` array which holds a cluster vector
		for (int j = 0; j < Classes[i].size(); j += 1)							///< Loops through `Vec` vectors
		{
			for (int k = 0; k < Nv; k += 1)								///< Loops through vector elements
			{
				Element[k] += (float)(Vec.at(Classes[i].at(j))[k] / Classes[i].size());		///< Computes vector element
			}
		}
		new_Center.emplace_back(Element);								///< Updates `new_Center` variable
	}
}

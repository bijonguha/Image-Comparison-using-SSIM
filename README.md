# Image-Comparison-using-SSIM
Compairing two images using SSIM and MSE

## Algorithms
The Structural Similarity (SSIM) Index quality assessment index is based on the computation of three terms, namely the luminance term, the contrast term and the structural term. The overall index is a multiplicative combination of the three terms.

![Figure 1]
(https://ibb.co/chcSv5)

where

![Figure 2]
(https://ibb.co/bXNua5)

where μx, μy, σx,σy, and σxy are the local means, standard deviations, and cross-covariance for images x, y. If α = β = γ = 1 (the default for Exponents), and C3 = C2/2 (default selection of C3) the index simplifies to:

![Figure 3]
(https://ibb.co/fjVfF5)

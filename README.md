<h1> Image-Comparison-using-SSIM </h1>
Compairing two images using SSIM and MSE

<h2> Algorithms </h2>

<h3> SSIM </h3> 
The Structural Similarity (SSIM) Index quality assessment index is based on the computation of three terms, namely the luminance term, the contrast term and the structural term. The overall index is a multiplicative combination of the three terms.
<img src="https://image.ibb.co/kf198Q/1_1.jpg">
where
<img src="https://image.ibb.co/f1hua5/1_2.jpg">
where μx, μy, σx,σy, and σxy are the local means, standard deviations, and cross-covariance for images x, y. If α = β = γ = 1 (the default for Exponents), and C3 = C2/2 (default selection of C3) the index simplifies to:
<img src="https://image.ibb.co/dCu7v5/1_3.jpg">


<h3> MSE </h3>
<img src="http://www.pyimagesearch.com/wp-content/uploads/2014/06/compare_mse.png">

<h2> Pre-requisites </h2>
* python 2.7+
* cv2 (openCV)
* numpy
* skimage

<h2> Examples </h2>
python main.py <path to reference image> <path to query image>
'''
python main.py ../data/testimg.jpg ../data/testimg_alter.jpg
'''

<h3>Results</h3>
<img src="https://github.com/bijonguha/git-files/blob/master/comparison.png">
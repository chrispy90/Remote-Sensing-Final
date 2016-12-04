# Remote-Sensing-Final
This project will be comparing the how well machine learning classifiers compare to traditional supervised classifiers. This prject will be using Landsat 8 scenes. The 2011 National Land Cover Dataset will be used for both training and validation of the algorithms. ESRI's ArcGIS for Desktop 10.4 will be used for this analysis.

#Steps
>1.) Convert Landsat 8 images to polygons

>2.) Convert the polygons to centroids

>3.) Make two subsets of the centroids
>>a.) One for Training Sites
>>b.) One for Validation Sites

>4.) Run a traditional supervised classifier algorithm: Maximum Likelihood Classification

>5.) Run the Random Trees Classifier 

>6.) Run the Support Vector Machine Classifier

>7.) Compute accuracy for each classifier with a confusion matrix

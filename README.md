# Remote-Sensing-Final
This project will be comparing the how well machine learning classifiers compare to traditional supervised classifiers. This prject will be using Landsat 8 scenes. The 2011 National Land Cover Dataset will be used for both training and validation of the algorithms. ESRI's ArcGIS for Desktop 10.4 will be used for this analysis.


# Data Prep
Convert Landsat 8 images to polygons (Raster to polygon Tool)

Convert the polygons to centroids (Features to Points Tool -o as shapefile)

Make two subsets of the centroids (Subset Features Tool)

Ensure no points overlap within each subset or between the two (Select by Location Tool)

* Total Training sites: 1199

* Total Validation sites: 600

Clip out section of the NLCD raster that the Landsat image covers (CLip Tool)

Reclassify the clipped NLCD raster into 4 classes: 1) Water 2) Urban 3) Bare Soil 4) Vegetation (Reclassify Tool)

Add known land cover classification to points via the reclassifed NLCD raster (Extract Multi Values to Points Tool)

Remove extra fields in the training and validation points

Create a composite of the following Landsat bands: 1 through 7 (Image Analysis window -o Compsite.tif)

Create a shapefile to use to clip the Composite Landsat image so that the No data cells are removed (Image Analysis window: Clip button)


# Analysis

> Traditional supervised classifier algorithm: Maximum Likelihood Classification
* Generate a signature file to feed classifier (feed in training sites)
* Run Maximum Likliehood Classification Tool

> Random tree Classifier
* Train classifier
* Run classify Tool

> Support Vector Machine Classifier
* Train classifier
* Run classify Tool

> Compute accuracy for each classifier with a confusion matrix


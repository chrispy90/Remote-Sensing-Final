# Remote-Sensing-Final
This project will be comparing the how well machine learning classifiers compare to traditional supervised classifiers. This prject will be using Landsat 8 scenes. The 2011 National Land Cover Dataset will be used for both training and validation of the algorithms. ESRI's ArcGIS for Desktop 10.4 will be used for this analysis.


# Data Prep
## NLCD
Clip out section of the NLCD raster that the Landsat image covers (CLip Tool)

Reclassify the clipped NLCD raster: (Reclassify Tool)

* Class 1: Water (11, 12)
* Class 2: Developed (21, 22, 23, 24)
* Class 3: Barren (31)

####Veg 
* Class 4: Forest (41, 42, 43)
* Class 5: Shrubland (51, 52)
* Class 6: Herbaceous (71, 72, 73, 74)
* Class 7: Planted/ Cultivated (81, 82)
* Class 8: Wetlands (90, 95)

## Make Training and validation points
1.) Convert Landsat 8 images to polygons (Raster to polygon Tool)

2.) Convert the polygons to centroids (Features to Points Tool -o as shapefile)

3.) Make two subsets of the centroids (Subset Features Tool)

4.) Ensure no points overlap within each subset or between the two (Select by Location Tool)

  * Total Training sites: 7000

  * Total Validation sites: 3000

5.) Remove points with a value of -9999 and 0 (NLCD no data value)

6.) Buffer points with 10 meters (Buffer tool)

7.) Make buffers into multipart polygons (Dissolve Tool)

8.) Load buffers into the Training Sample Manager and click the save button (Image Classification Toolbar)

9.) Add known land cover classification to points via the reclassifed NLCD raster (Extract Multi Values to Points Tool)

10.) Remove extra fields in the training and validation points

## Landsat 8 Data
1.) Load bands 1 through 7 into ArcMap and open the Image analysis window

2.) Create a shapefile to use to clip the Composite Landsat image so that the No data cells are removed (Image Analysis Window: Clip button)

3.) Composite and save as a TIF (Iamage Analysis Window: Save button)


# Analysis

NOTE: had to remove class 3 (barren soil) becuase it would skew the classifier for some reason. As a result, Class 3 was removed for this entire analysis

## Maximum Likelihood Classification
1.) Generate a signature file to feed classifier (feed in training sites)
  * Load bands individually: bands 1 - 7 (use th clipped versions of these from Landsat data prep step 2)
2.) Run Maximum Likliehood Classification Tool
  * Load bands individually: bands 1 - 7 (use th clipped versions of these from Landsat data prep step 2)


## Random tree Classifier
1.) Train classifier
  * Max number of trees: 100, Max tree depth: 30, Max nummber of samples per class: 700
* Run classify Tool

## Support Vector Machine Classifier
1.) Train classifier
  * Load the training point buffers into the Training Sample Manager on the Classifcation Toolbar and save as a Feature Class in Geodatabase
  * Removed class 3 (barren soil)
  * Train SVM (Train Support Vector Machine Classifier Tool)
    100 samples per class
	
2.) Run classify Tool

## Compute accuracy for each classifier with a confusion matrix

1.) Load a your validation points and extract classified value (Extract Multi Value Tool)

2.) Export validation points to Excel (Table to excel tool)

3.) Highlight the column with the value extracted from the NLCD and the column with the value extracted from the classified image

4.) Create pivot table in excel with following table guide


FILTERS | COLUMNS | ROWS | VALUES
    --- | --- | --- | ---
   Blank| Classified Values | NLCD Values | Count of Classified Values
   
5.) Calculate overall accuracy
  * (Sum of diagonals/ Total number of observations)*100
 
# Findings

## Louisiana Delta

Classifier | Accuracy
--- | ---
Maximum Likelihood | 59.29 %
Support Vector Machine | 63.23 %
Randome Trees | 63.20 %


[Video explaining easy error matrix creation](https://www.youtube.com/watch?v=9dGjuEQie7Y)


![picture alt](https://thumbs.gfycat.com/FirsthandSingleAlaskajingle-size_restricted.gif "Stats feelings")


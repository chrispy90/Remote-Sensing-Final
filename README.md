# Remote-Sensing-Final
This project will be comparing the how well machine learning classifiers compare to traditional supervised classifiers. This prject will be using Landsat 8 scenes. The 2011 National Land Cover Dataset will be used for both training and validation of the algorithms. ESRI's ArcGIS for Desktop 10.4 will be used for this analysis.


# Data Prep
Convert Landsat 8 images to polygons (Raster to polygon Tool)

Convert the polygons to centroids (Features to Points Tool -o as shapefile)

Make two subsets of the centroids (Subset Features Tool)

Ensure no points overlap within each subset or between the two (Select by Location Tool)

* Total Training sites: 7000

* Total Validation sites: 3000

Remove points with a value of -9999 and 0 (NLCD no data value)

Buffer points with 10 meters (Buffer tool)

Make buffers into multipart polygons (Dissolve Tool)

Clip out section of the NLCD raster that the Landsat image covers (CLip Tool)

Reclassify the clipped NLCD raster: (Reclassify Tool)
	* Class 1: Water (11, 12)
	* Class 2: Developed (21, 22, 23, 24)
	* Class 3: Barren (31)
	*Veg 
		* Class 4: Forest (41, 42, 43)
		* Class 5: Shrubland (51, 52)
		* Class 6: Herbaceous (71, 72, 73, 74)
		* Class 7: Planted/ Cultivated (81, 82)
	* Class 8: Wetlands (90, 95)


Add known land cover classification to points via the reclassifed NLCD raster (Extract Multi Values to Points Tool)

Remove extra fields in the training and validation points

Create a composite of the following Landsat bands: 1 through 7 (Image Analysis window -o Compsite.tif)

Create a shapefile to use to clip the Composite Landsat image so that the No data cells are removed (Image Analysis window: Clip button)


# Analysis

> Traditional supervised classifier algorithm: Maximum Likelihood Classification
* Generate a signature file to feed classifier (feed in training sites)
	Load bands individually: bands 1 - 7
* Run Maximum Likliehood Classification Tool
	Load bands individually: bands 1 - 7

> Random tree Classifier
* Train classifier
* Run classify Tool

> Support Vector Machine Classifier
* Train classifier
	1.) load the training point buffers into the Training Sample Manager on the Classifcation Toolbar and save as a Feature Class in Geodatabase
	2.) Removed class 3 (barren soil)
	3.) Train SVM (Train Support Vector Machine Classifier Tool)
	#Note only ran the 3000 validation points through, will need to convert to buffers and remove class 3 (barren soil)
* Run classify Tool

> Compute accuracy for each classifier with a confusion matrix
	Max: Run extract multi value to point with Max Classed raster and validation points
		Had to remove class 3
		 Export to Excel
		 Create Pivot table

		FILTERS | COLUMNS
	        --- | --- 
		   Blank| Classified Values
		
		ROWS | VALUES
		 --- | ---
		 Known Values | Count of Classified Values

		 	

		Overall accuracy formula from pivot table: (sum of diagonal / # of total points) * 100


[Video explaining easy error matrix creation](https://www.youtube.com/watch?v=9dGjuEQie7Y)


![picture alt](https://thumbs.gfycat.com/FirsthandSingleAlaskajingle-size_restricted.gif "Stats feelings")


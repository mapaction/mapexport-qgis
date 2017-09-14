# mapexport-qgis
A QGIS plugin which exports and zips up a PDF and JPG for a selected Print Composer.

This plugin is one component of a QGIS equivalent of MapAction's ArcGIS MapExport toolset, which prepares map filesets for upload to online repositories. Once the user has selected a Print Composer and a destination location, it exports a PDF and JPG to a folder named after the Print Composer (which is created if necessary), with filenames using the same name, then zips the contents of the folder into a file with the same name.

It is intended to add a component to the plugin which supports creation and editing of metadata, and exporting to an XML file in the same folder. This fileset would meet the requirements of the repository upload process.

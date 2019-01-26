# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapExport
                                 A QGIS plugin
 Exports PDF, JPG and metadata XML
                             -------------------
        begin                : 2017-08-27
        git sha              : $Format:%H$
        copyright            : (C) 2017 by MapAction
        email                : info@mapaction.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 Derived from the MapsPrinter plugin, with thanks to 
 Harrissou Sant-anna (Conseil d'Architecture, 
 d'Urbanisme et de l'Environnement du Maine-et-Loire)
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MapExport class from file MapExport.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .map_export import MapExport
    return MapExport(iface)

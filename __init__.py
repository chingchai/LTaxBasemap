# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LTaxBasemapFree
                                 A QGIS plugin
 LTax Basemap free for qgis2.x
                             -------------------
        begin                : 2021-05-19
        copyright            : (C) 2021 by Attagorn Srinarong / LTMAP, LTaxSmartGroup, SmartLTax
        email                : attagorn@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LTaxBasemapFree class from file LTaxBasemapFree.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .ltax_basemap_free import LTaxBasemapFree
    return LTaxBasemapFree(iface)

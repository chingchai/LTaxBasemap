@echo off
rem call "C:\Program Files\QGIS 2.18\OSGeo4W.bat"  
rem call "%~dp0\bin\o4w_env.bat"
call "C:\Program Files\QGIS 2.18\bin\o4w_env.bat"
@echo on
rem pyrcc4 -o resources_rc.py resources.qrc
pyrcc4 -o resources.py resources.qrc
pyuic4 -x ltax_basemap_free_dockwidget_base.ui > ltax_basemap_free_dockwidget_base.py

@echo off
call "C:\OSGeo4W64\bin\o4w_env.bat"
call "C:\OSGeo4W64\bin\qt5_env.bat"
call "C:\OSGeo4W64\bin\py3_env.bat"
@echo on
pyuic5 -x ltax_basemap_free_dockwidget_base.ui  1>ltax_basemap_free_dockwidget_base.py



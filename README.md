# README #

С периодичностью раз в 4 часа выкачивается файл `https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_Global_24h.zip` и загружается в базу.

Если в базе есть точка с идентичными координатами и датой - проверяется confidence. Если он больше, то данные о пожаре для данной точки обновляются.
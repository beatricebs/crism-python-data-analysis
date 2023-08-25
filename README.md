# crism-python-data-analysis

## Introduction
In this repository you will find some code to open and carry out basic analysis of the CRISM MTRDR data cubes. 

Main functionalities: 

`CRISM_cube_visualization_and_analysis.ipynb`
- Hyperspectral cube visualization;
- Production of RGB browse product;
- Spectra extraction (with spectral ratioing) from ROIs. 

`CRISM_ratioed_cube_MTRDR.ipynb`
- Computes a "ratioed" CRISM cube, where every pixel of the scene is a ratioed spectrum. 

## Dataset

- Type of data: [CRISM Map-Projected Targeted Reduced Data Record (MTRDR)](https://ode.rsl.wustl.edu/mars/pagehelp/Content/Missions_Instruments/Mars%20Reconnaissance%20Orbiter/CRISM/CRISM%20Product%20Primer/CRISM%20MTRDR.htm).
- Access to dataset: [NASA - PDS Geoscience Node](https://pds-geosciences.wustl.edu/missions/messenger/index.htm).

## Acknowledgements
This code was developed with the help of Dr. Mario D'Amore (DLR, Berlin, Germany) and Marco Baroni (University of Padova, Italy).

## License
MIT
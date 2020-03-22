# R and Python APIs for CoVid-19 Data on Germany

This repo contains the R and Python libs for the german CoVid-19 datasets published by the <a href="https://npgeo-corona-npgeo-de.hub.arcgis.com/">NPGEO Corona Hub</a>. These libs ease the access to the latest data for epidemiologists and other statistical researchers. This project started during the <a href="https://wirvsvirushackathon.org/">#wirvsvirus Hackathon</a> hosted by the german chancellery.

## Installing

This is still work in progress and I will publish the libs to CRAN and PyPi, respectively in the next days. So far, you can install the libs directly from GitHub. 

### Installing the R lib

To install the R lib you'll need the package <code>devtools</code>. You can download the package using:

    # installing library
    install.packages("devtools")

    # source the lib
    library(devtools)

Next, you will need to use the <code>install_github()</code> function. You can simply run the following code in your R terminal, RStudio or whatever interface you use:

    # install package
	install_github(repo = "LJStroemsdoerfer/CoVid-Data-Api",
                   subdir = "r_lib/coviddatagermany",
                   dependencies = TRUE)

    # source the package
    library(coviddatagermany)

You can then easily access the data by using the <code>get_covid_data()</code> function. The function provides a standard R interface and can be called as followed:

    # request county level data
    df_county <- coviddatagermany::get_covid_data(level = "county")

The function will return data.frame for the county (Landkreis) level data on the corona virus spread in Germany. If you are more interested in the state (Bundesland) level data, then you can simply use <code>coviddatagermany::get_covid_data(level = "state")</code>.

### Installing the Python lib

To use the Python package you will have to clone the repository for now. I am already working on publishing the library to PyPi, which will happen in the next days. You can clone the repo by using:

    git clone https://github.com/LJStroemsdoerfer/CoVid-Data-Api.git

As soon as you did this, you can use the class by simply importing it from the folder. To do so, this folder needs to be accessible to the script. As I said, I am working on a proper PyPi release, which takes a bit more time, but it's gonna happen. I got the time now.

    # import the class
    from covid_data_germany.covid_data_germany import covid_data_germany

    # initiate the class
    dataset = covid_data_germany()

    # download the data
    dataset.get_data(level = "county")

In case you want to work with state level data, you can just <code>level</code> to <code>state</code>. The function will return a <code>pd.DataFrame</code> object that can be accessed by <code>dataset.data</code>.
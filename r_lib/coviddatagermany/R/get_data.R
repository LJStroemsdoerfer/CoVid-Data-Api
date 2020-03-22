#' Function to crawl the CoVid-19 data for Germany
#'
#' @description This function leverages the NPGEO Corona Data Hub to extract and prepare the geo data.
#'
#' @param level string to define the level of data, either "county" or "state". Default is "county", which requests the county level data, where "state" gives the state level data.
#'
#' @return a data.frame object
#'
#' @import dplyr RJSONIO
#'
#' @export
get_covid_data <- function(level = "county"){

  # check if county
  if(level == "county"){

    # set the url
    url <- "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json"

  # if state
  } else {

    # set the url
    url <- "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Coronaf%C3%A4lle_in_den_Bundesl%C3%A4ndern/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json"
  }

  # crawl the data
  npgeo_list <- suppressWarnings(RJSONIO::fromJSON(readLines(url))$features)

  # create empty list container
  df_list <- list()

  # loop over npgeo_list
  for(i in seq(npgeo_list)){

    # extract the list
    regional_list <- npgeo_list[[i]]$attributes

    # check for NULL values
    regional_list[sapply(regional_list, is.null)] <- NA

    # extract the colnames
    col_names <- names(regional_list)

    # create the data.frame
    df_list[[i]] <- data.frame(matrix(unlist(regional_list), nrow = 1, byrow = TRUE), stringsAsFactors = FALSE)

    # rename the columns
    names(df_list[[i]]) <- col_names

  }

  # bind the list together to one data.frame
  df <- dplyr::bind_rows(df_list)

  # return data.frame
  return(df)
}


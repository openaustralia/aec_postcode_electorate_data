A mapping of Australian postcodes to federal electorates according to the Australian Electoral Commission.

* The `redistributed` column of the data is the electorate which will be used at the next federal electorate for the given locality. For states where there was no redistribution the column will be blank.9s
* The `other` columne is the `Other Locality(s)` data from the AEC site.
* To get a consolidated list of electorate/postcode mappings for the *next* election:
    
    ```
    select distinct state, suburb, postcode, coalesce(nullif(redistributedElectorate,""), electorate) as electorate from data
    ```
    
* The list of postcodes is sourced indirectly from the [G-NAF](https://data.gov.au/dataset/ds-ga-074edff7-fd26-4ff5-87e4-0108e71afe43/details?q=g-naf), by way of [openaddresses.io](http://results.openaddresses.io/sources/au/countrywide). Recreating the list is as simple as downloading the latest data and running:
    ```
    cat countrywide.csv | cut -f 9 -d \, | sort -u > postcodes
    ```
    then removing the header line.

Pull requests welcome.


This is a scraper that runs on [Morph](https://morph.io). To get started [see the documentation](https://morph.io/documentation)

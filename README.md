# Aigeon AI Google Shopping API

## Project Description

The Aigeon AI Google Shopping API is a Python-based server application designed to interface with Google's Shopping search engine through the SerpAPI. This tool allows users to perform detailed and customizable product searches on Google Shopping, retrieving product listings and shopping results based on a variety of parameters.

## Features Overview

- **Customizable Search Queries**: Tailor your search queries with a range of parameters to refine results.
- **Location-Based Searches**: Specify geographic locations or encoded locations for more accurate results.
- **Advanced Search Options**: Utilize advanced search parameters and filters to narrow down results.
- **Device-Specific Results**: Choose between desktop, tablet, or mobile views for search results.
- **Asynchronous and Cached Searches**: Options to perform searches asynchronously or bypass cached results for fresh data.
- **Enterprise Features**: Includes enterprise-level options such as ZeroTrace mode for enhanced privacy.

## Main Features and Functionality

The primary functionality of this application is to perform searches on Google Shopping using the SerpAPI. Users can specify a wide range of parameters to customize their search experience:

- **Query (`q`)**: The core search term or phrase.
- **Location (`location`)**: Define the origin of the search by specifying a city or region.
- **Encoded Location (`uule`)**: Use Google's encoded location parameter for precise geographic targeting.
- **Google Domain (`google_domain`)**: Specify the Google domain to use for the search (e.g., google.com).
- **Country Code (`gl`)**: Two-letter code for geographic targeting.
- **Language Code (`hl`)**: Two-letter code for language-specific results.
- **Advanced Search (`tbs`)**: Use advanced search parameters for more refined queries.
- **Search Filters (`shoprs`)**: Apply specific filters to the search results.
- **Direct Links (`direct_link`)**: Option to include direct product links in results.
- **Pagination (`start`)**: Control result pagination by specifying an offset.
- **Result Count (`num`)**: Define the maximum number of results to return.
- **Device Type (`device`)**: Choose the device type for viewing results.
- **Cache Control (`no_cache`)**: Force fresh results by ignoring cached versions.
- **Asynchronous Search (`aasync`)**: Submit searches asynchronously for faster response.
- **ZeroTrace Mode (`zero_trace`)**: Enterprise feature for privacy-focused searches.

## Main Function Description

### `search_google_shopping`

This function performs a search on Google Shopping using the specified parameters. It constructs a payload with the provided options and sends a request to the SerpAPI endpoint. The function returns the search results in JSON format.

**Parameters:**

- **`q`**: (str, optional) The search query.
- **`location`**: (str, optional) The location for the search.
- **`uule`**: (str, optional) Google encoded location.
- **`google_domain`**: (str, optional) The Google domain to use.
- **`gl`**: (str, optional) Country code for geographic targeting.
- **`hl`**: (str, optional) Language code for search results.
- **`tbs`**: (str, optional) Advanced search parameters.
- **`shoprs`**: (str, optional) Helper ID for search filters.
- **`direct_link`**: (bool, optional) Include direct product links.
- **`start`**: (int, optional) Result offset for pagination.
- **`num`**: (int, optional) Maximum number of results.
- **`device`**: (Literal["desktop", "tablet", "mobile"], optional) Device type for results.
- **`no_cache`**: (bool, optional) Force fresh results.
- **`aasync`**: (bool, optional) Submit search asynchronously.
- **`zero_trace`**: (bool, optional) Enable ZeroTrace mode for privacy.

The function ensures that only non-None parameters are included in the request, optimizing the search query for the best possible results.
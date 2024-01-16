===================================================================================
				About PyCasts
===================================================================================
PyCasts is a content aggregator that fetches information form various places  online and gathers all of that information in one place. Therefore you don'y have to visit multiple sites to get the latest info: one website is enough

The main objective if this project idea is to aggregate content. First, you need to know what sites you'll wnt the content aggregator to get content from.Then, you can use libraries such as requests for sending HTTP requests and BeautifulSoup to parse and scrape the necessary content from the sites.

The application can implement its content aggregation as a background process. Libraries such as celery or apscheduler can help with that. You can try out apscheduler. It’s great for small background processes.

After scraping content from various sites, you’ll need to save it somewhere. So, you’ll use a database to save the scraped content.

==================================================================================
				How to Get Started
==================================================================================
To get started with the project, clone the repository using:
	 git clone https://github.com/balagrivine/pyCasts.git.

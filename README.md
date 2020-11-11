# Server Selector API

This project is a Proxy API that consumes an external API and transform the external API into a list of regions (getRegions) of filters the list of servers (getServers) if the name of the region is provided, otherwise it will return the whole list.

### Technologies
This is a project that uses: 
- 🐍 Python
- 🍶 flask

### Commands
- install dependencies `pip install -r requirements.txt`
- run the app in dev mode `python app.py`

### Architecture Idea
The architecture idea of this project is to have Proxy like API, and expose 3 different GET HTTP methods, all of them will use the external aiven API to get a list of cloud servers.
`getRegions` will map all the available regions and return a list of strings with the regions names
`getServers` will return the list of all available cloud servers
`getServers/<region>` will filter the cloud servers and return a list of only the servers from the selected region

To check the Frontend part, please check [ServerSelector](https://github.com/Shinkei/serverSelector)

### Deploy
The app is deployed at heroku, please check this url [https://server-selector.herokuapp.com/](https://server-selector.herokuapp.com/)
steps to deploy:(connect with the heroku account and run)
- `git push heroku master`

### Author 🤓
Jorge Ramirez
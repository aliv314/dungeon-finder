#Grabs the Game Name and Images through API calls
import requests

api_image = 'https://api.boardgameatlas.com/api/game/images?limit=20&client_id=BPsyAhFgcY'
imageCall = requests.get(api_image).json()
imageTest = imageCall['images'][0]['url']
gameID = imageCall['images'][0]['game']['id']
api_name = 'https://api.boardgameatlas.com/api/search?ids={0}&client_id=BPsyAhFgcY'.format(gameID)
nameCall = requests.get(api_name).json()
gameName = nameCall['games'][0]['name']
api_root = 'https://api.boardgameatlas.com/api/search?name=Root&client_id=BPsyAhFgcY&exact=true'
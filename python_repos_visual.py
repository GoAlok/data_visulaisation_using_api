import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {
    "Accept" : "application/vnd.github.v3+json"
}
response = requests.get(url, headers=headers)

# Store API response in a variable. 
dict_data = response.json()

# Process results.
repo_dicts = dict_data['items']
repo_names, stars = [], []

# Adding Custom Tooltips
labels, repo_links = [], []

for repo_dict in repo_dicts:
    # repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualization.
data = [{
    "type": "bar",
    # 'x': repo_names,
    'x': repo_links,
    'y': stars,
    
    'hovertext': labels,
    
    # Refining Plotly Charts
    "marker": {
        "color" : "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
        "opacity": 0.6,
    }
}]

my_layout ={
    "title": "Most-Starred Python Projects on GitHub",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont":{"size":24},
        "tickfont":{"size":14},
        },
    "yaxis": {
        "title": "Stars",
        "titlefont":{"size":24},
        "tickfont":{"size":14},
        },
}

fig = {
    "data":data,
    "layout":my_layout,
}
offline.plot(fig, filename="python_repos.html")


import requests


# Make an API call and store the response.
"""
#  --> Monitoring API Rate Limits:
        "https://api.github.com/rate_limit"
"""
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {
    "Accept" : "application/vnd.github.v3+json"
}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

# Store API response in a variable. 
dict_data = response.json()

# Process results.
# print(dict_data.keys())
print(f"Total repositories: {dict_data['total_count']}")

# Explore information about the repositories.
repo_dicts = dict_data['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.

# repo_dict = repo_dicts[0]
# # print(f"\nKeys: {len(repo_dict)}")
# # for key in sorted(repo_dict.keys()):
# #     print(key)

print(f"\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")

# --> Summarizing the Top Repositories
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")



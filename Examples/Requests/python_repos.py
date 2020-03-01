import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code: ", r.status_code)

response_dict = r.json()

print("Total repositories: ", response_dict['total_count'])

repo_dicts = response_dict['items']
names, plot_dicts = [], []
# print("Repositories returned: ", len(response_dict))
# repo_dict = repo_dicts[0]
# print("\nKeys: ", len(repo_dict))

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
    # print("\nSelected information about first repository:")
    # print('Name: ', repo_dict['name'])
    # print('Owner: ', repo_dict['owner']['login'])
    # print('Stars: ', repo_dict['stargazers_count'])
    # print('Repository: ', repo_dict['html_url'])
    # print('Created: ', repo_dict['created_at'])
    # print('Update: ', repo_dict['updated_at'])
    # print('Description: ', repo_dict['description'])

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
# chart.render()

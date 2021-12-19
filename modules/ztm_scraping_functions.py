def sort_stories_by_votes(hn_list):
  return sorted(hn_list, key=lambda k: k['votes'], reverse=True)

def create_custom_hackernews(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote): # exclude stories with no votes
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99: # exclude stories with votes <= 99
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)

#!/usr/bin/python

from collections import Counter

class FilterModule(object):
    def filters(self):
        return {
		'election': self.election
        }

    def election(self, vote_list):
        if len(vote_list) == 0:
          return 'no update to report'

        votes = Counter(vote_list)
        dict = {}
      
        for v in votes.values():
          dict[v] = []
      
        for (k,v) in votes.items():
          dict[v].append(k)
      
        total_votes = sorted(dict.keys(),reverse=True)[0]
      
        if len(dict) == 1:
          first = list(dict.items())[0][1]
          x = ' '.join(first)
        elif len(dict[total_votes]) > 1:
          x = sorted(dict[total_votes])[0]
        else:
          x = dict[total_votes][0]
        return x

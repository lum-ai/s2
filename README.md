# s2
Python wrapper for the Semantic Scholar API


### Installation

```
pip install git+https://github.com/lum-ai/s2
```

#### Testing

Assuming you've cloned the library...

```
pip install -e .[test]
```

```
green -vv --run-coverage
```


## Example


```python
from s2 import *
s2_paper_id = "b42d4d266b924e03493ffbb6d0e903a2fa84283a"
paper = SemanticScholarAPI.paper(s2_paper_id)

# grab any citing papers deemed to be influential.
# sort them by the year of publication (oldest first).
influential_papers = sorted(filter(lambda x: x.isInfluential, paper.citations), key=lambda x: x.year)

# how many times were these influential papers cited?
print("\tPUB YEAR\tTITLE\tNUM. CITED BY")
for p in influential_papers:
  complete_summary = p.full()
  print("{}\t{}\t{}".format(complete_summary.year, complete_summary.title, len(complete_summary.citations)))
```

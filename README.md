# Sentence Aligner
## How to install
```python -m pip install .```

## How to use
```python
from power import Aligner

source = "helli min wha ts ip"
target = "hello man whats up"

aligner = Aligner()
result = aligner.get_alignment(source, target)
```
The output should be something like this
```
{
    'source': ['helli', 'min', 'wha ts', 'ip'],
    'target': ['hello', 'man', 'whats', 'up'],
    'sub_ids': [0, 1, 2, 3]
}
```

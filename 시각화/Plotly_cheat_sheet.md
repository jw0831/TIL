# Plotly cheat sheet

작성자: github.com/jw0831

```python
import numpy as np
import pandas as pd
import json
from urllib.request import urlopen
```

```python
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from plotly.validators.scatter.marker import SymbolValidator
```

### Bar plot

```python
var = px.bar(df[:], x='',y='', color='Frequency', color_continuous_scale=px.colors.sequential.Cividis_r)
```


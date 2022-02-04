# Day15 (2022/02/04)

## 노트

### DataFrame Basic Statistics

  * pandas.DataFrame.head()
  * pandas.DataFrame.sample()
  * pandas.DataFrame.describe()
  * pandas.DataFrame.corr()

### Matplotlib Texts

<details>
<summary>Matplotlib Text APIs</summary>

#### Figure Text APIs

  * fig.suptitle()
  * fig.text()

#### Axes Text APIs

  * ax.set_title()
  * ax.set_xlabel()
  * ax.set_ylabel()
  * ax.text()
    * s: string
    * Design Options
      * family: serif, sans-serif, monospace, ...
      * style: normal, italic, ...
      * size: xx-small, x-small, small, medium, large, x-large, xx-large
      * weight: light, normal, medium, semibold, bold, heavy, black
      * color
      * backgroundcolor
      * linespacing
      * alpha
      * visible
      * bbox: dict(boxstyle, facecolor, alpha, ...)
    * Alignment Options
      * x
      * y
      * ha
      * va
      * rotation
      * zorder
      * multialignment: alignment option of text inside bbox
  * ax.annotate()
    * text: string
    * Design Options
      * bbox: dict(boxstyle, facecolor, alpha, ...)
      * arrowprops: dict(arrowstyle, ...)
    * Alignment Options
      * xy: tuple(location of value point)
      * xytext: list(location of annotation)
      * zorder

</details>

### Matplotlib Colors

<details>
<summary>Matplotlib Color APIs</summary>

#### matplotlib.colors.ListedColormap

```python
from matplotlib.colors import ListedColormap

# Group to Number
groups = sorted(data['grade'].unique())
gton = dict(zip(groups, range(5)))
data['grade_num'] = data['grade'].map(gton)

fig, axes = plt.subplots(2, 4)
axes = axes.flatten()
color_maps = ['Pastel1', 'Pastel2', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10']
for idx, cm in enumerate(color_maps):
  pcm = axes[idx].scatter(
    x=data['math score'],
    y=data['reading score'],
    c=data['grade_num'],
    cmap=ListedColormap(plt.cm.get_cmap(cm).colors[:5])
  )
  cbar = fig.colorbar(pcm, ax=axes[idx], ticks=range(5))
  cbar.ax.set_yticklabels(groups)
  axes[idx].set_title(cm)
plt.show()
```

#### matplotlib.colors.TwoSlopeNorm

```python
from matplotlib.colors import TwoSlopeNorm

fig, axes = plt.subplots(3, 4, figsize=(20, 15))
axes = axes.flatten()
offset = TwoSlopeNorm(vmin=0, vcenter=student['math score'].mean(), vmax=100)
color_maps = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
              'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
for idx, cm in enumerate(color_maps):    
  pcm = axes[idx].scatter(
    x=student['math score'],
    y=student['reading score'],
    c=offset(student['math score']),
    cmap=cm
  )
  cbar = fig.colorbar(pcm, ax=axes[idx], ticks=[0, 0.5, 1], orientation='horizontal')
  cbar.ax.set_xticklabels([0, student['math score'].mean(), 100])
  axes[idx].set_title(cm)
plt.show()
```

#### Axes Color APIs

  * ax.imshow()

```python
im = np.arange(100).reshape(10, 10)
fig, ax = plt.subplots(1, 1)
ax.imshow(im, cmap='Greens')
plt.show()
```

#### Sequential Color Maps

```python
fig, axes = plt.subplots(3, 6)
axes = axes.flatten()
color_maps = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
              'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
              'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
for idx, cm in enumerate(color_maps):
  pcm = axes[idx].scatter(
    x=data['math score'],
    y=data['reading score'],
    c=data['reading score'],
    cmap=cm, vmin=0, vmax=100
  )
  fig.colorbar(pcm, ax=axes[idx])
  axes[idx].set_title(cm)
plt.show()
```

#### Fixing Colors

```python
colors = data['grade'].apply(lambda x: 'blue' if x == 'A' else 'red')
color_bars = ['blue'] + ['red'] * 4

fig, axes = plt.subplots(1, 2)
grades = data['grade'].value_counts().sort_index()
axes[0].bar(grades.index, grades, color=color_bars, width=0.5)
axes[1].scatter(data['math score'], data['reading score'], c=colors, alpha=0.3)
plt.show()
```

</details>

### Matplotlib Facets

<details>
<summary>Matplotlib Facet APIs</summary>

#### matplotlib.figure.Figure.add_gridspec()

```python
fig = plt.figure()
gs = fig.add_gridspec(3, 3)
axes = [None for _ in range(5)]
axes[0] = fig.add_subplot(gs[0, :])
axes[0].set_title('gs[0, :]')
axes[1] = fig.add_subplot(gs[1, :-1])
axes[1].set_title('gs[1, :-1]')
axes[2] = fig.add_subplot(gs[1:, -1])
axes[2].set_title('gs[1:, -1]')
axes[3] = fig.add_subplot(gs[-1, 0])
axes[3].set_title('gs[-1, 0]')
axes[4] = fig.add_subplot(gs[-1, -2])
axes[4].set_title('gs[-1, -2]')
for idx in range(5):
  axes[idx].set_xticks([])
  axes[idx].set_yticks([])
plt.tight_layout()
plt.show()
```

#### matplotlib.subplot2grid()

```python
fig = plt.figure()
axes = [None for _ in range(6)]
axes[0] = plt.subplot2grid((3, 4), (0, 0), colspan=4)
axes[1] = plt.subplot2grid((3, 4), (1, 0), colspan=1)
axes[2] = plt.subplot2grid((3, 4), (1, 1), colspan=1)
axes[3] = plt.subplot2grid((3, 4), (1, 2), colspan=1)
axes[4] = plt.subplot2grid((3, 4), (1, 3), colspan=1, rowspan=2)
axes[5] = plt.subplot2grid((3, 4), (2, 0), colspan=3)
for idx in range(6): 
  axes[idx].set_title('axes[{}]'.format(idx))
  axes[idx].set_xticks([])
  axes[idx].set_yticks([])
fig.tight_layout()
plt.show()
```

#### matplotlib.figure.Figure.add_axes()

```python
fig = plt.figure()
axes = [None for _ in range(3)]
axes[0] = fig.add_axes([0.1, 0.1, 0.8, 0.4])
axes[1] = fig.add_axes([0.15, 0.6, 0.25, 0.6])
axes[2] = fig.add_axes([0.5, 0.6, 0.4, 0.3])
for idx in range(3): 
  axes[idx].set_title('axes[{}]'.format(idx))
  axes[idx].set_xticks([])
  axes[idx].set_yticks([])
fig.tight_layout()
plt.show()
```

#### matplotlib.axes.Axes.inset_axes()

```python
fig, ax = plt.subplots(1, 1)
axin = ax.inset_axes([0.75, 0.75, 0.2, 0.2])
plt.show()
```

#### mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable()

```python
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

im = np.arange(100).reshape(10, 10)
imap = ax.imshow(im, cmap='Greens')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
fig.colorbar(imap, cax=cax)
plt.show()
```

</details>

### Matplotlib Grids

<details>
<summary>Matplotlib Grid APIs</summary>

#### x = ac, y = bc

  * ax.grid()

#### x + y = c

```python
cs = np.linspace(0, 2, 11)
for c in cs:
  ax.plot([0, c], [c, 0], linestyle='--', color='gray', alpha=0.5, linewidth=1)
```

#### y = cx

```python
rads = np.linspace(0, np.pi/2, 11)
for rad in rads:
  ax.plot([0, 2], [0, 2 * np.tan(rad)], linestyle='--', color='gray', alpha=0.5, linewidth=1)
```

#### Circle Grids

```python
rs = np.linspace(0.1, 0.6, 6)
center = [0.5, 0.5]
for r in rs:
  x = r * np.cos(np.linspace(0, 2 * np.pi, 100))
  y = r * np.sin(np.linspace(0, 2 * np.pi, 100))
  ax.plot(x + center[0], y + center[1], linestyle='--', color='gray', alpha=0.5, linewidth=1)
  ax.text(
    x=center[0] + r * np.cos(np.pi / 4),
    y=center[1] + r * np.sin(np.pi / 4),
    s=f'{r:.1}',
    color='gray',
    ha='center',
    va='center'
  )
```

</details>

### Matplotlib Others

<details>
<summary>Matplotlib Other APIs</summary>

#### Managing Default Settings

```python
plt.rcParams['figure.dpi'] = 150

plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.linestyle'] = ':'
# plt.rc('lines', linewidth=2, linestyle=':')

plt.rcParams.update(plt.rcParamsDefault)
```

#### Using Themes

```python
print(plt.style.available)

plt.style.use('seaborn')
plt.plot([1, 2, 3])

# with plt.style.context('seaborn'):
#   plt.plot([1, 2, 3])
```

#### Others

  * plt.subplots(): sharex, sharey
  * fig.set_facecolor()

```python
fig, ax = plt.subplots(1, 2, sharex=True, sharey=True)
fig.set_facecolor('lightgray')
plt.show()
```

  * plt.figure(): dpi
  * fig.add_subplot(): aspect

```python
fig = plt.figure(dpi=150)
ax1 = fig.add_subplot(121, aspect=0.15)
ax2 = fig.add_subplot(122, aspect=0.25)
for ax in [ax1, ax2]:
  ax.plot([1, 2, 3], [1, 3, 9])
  ax.set_xticks([1, 2, 3])
  ax.set_yticks([1, 3, 5, 7, 9])
  ax.set_ylim(0, 10)
plt.show()
```

  * ax.spines

```python
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position('center')
ax2.spines['left'].set_position(('data', 0.3))
ax2.spines['bottom'].set_position(('axes', 0.2))
```

  * ax.axhline()
  * ax.axvline()
  * ax.axhspan()
  * ax.axvspan()

</details>

### Seaborn

<details>
<summary>Seaborn Plotting APIs</summary>

  * Categorical Plotting
    * Categorical Scatter Plotting
      * sns.stripplot()
      * sns.swarmplot()
    * Categorical Distribution Plotting
      * sns.boxplot()
      * sns.violinplot()
      * sns.boxenplot()
    * Categorical Estimation Plotting
      * sns.countplot()
      * sns.pointplot()
      * sns.barplot()
  * Distribution Plotting
    * sns.histplot()
    * sns.kdeplot()
    * sns.ecdfplot()
    * sns.rugplot()
  * Relational Plotting
    * sns.scatterplot()
    * sns.lineplot()
    * sns.heatmap()
  * Regression Plotting
    * sns.jointplot()
    * sns.pairplot()
    * sns.regplot()

#### Bar Plotting

  * sns.countplot()
    * x
    * y
    * data
    * order
    * hue
    * hue_order
    * palette
    * color
    * saturate
    * ax

```python
import seaborn as sns
sns.countplot(x='grade', data=data)
```

  * sns.pointplot()
  * sns.barplot()

#### Line Plotting

  * sns.lineplot()

```python
fig, ax = plt.subplots(1, 1)
sns.lineplot(x='student number', y='math score', data=data, ax=ax)
plt.show()
```

#### Box Plotting

  * sns.boxplot()
    * width
    * linewidth
    * filtersize

```python
fig, ax = plt.subplots(1, 1)
sns.boxplot(x='grade', y='math score', data=data, ax=ax)
plt.show()
```

#### Violin Plotting

  * sns.violinplot()
    * bw
    * cut
    * inner
    * scale
    * split

```python
fig, ax = plt.subplots(1, 1)
sns.violinplot(x='math score', data=data, ax=ax)
plt.show()
```

#### Distribution Plotting

  * sns.histplot(): Histogram
    * x
    * y
    * ax
    * data
    * binwidth
    * bins
    * element: step, poly
    * hue
    * hue_order
    * multiple: layer, dodge, stack, fill
    * color
    * cbar
  * sns.kdeplot(): Kernel Density Estimate
    * fill
    * bw_method
    * multiple: layer, stack, fill
    * cumulative
    * cut
  * sns.ecdfplot(): Empirical Histogram
    * stat: proportion, count
    * complementary
  * sns.rugplot(): Rug Plotting

#### Scatter Plotting

  * sns.scatterplot()
    * x
    * y
    * ax
    * data
    * style
    * markers
    * hue
    * hue_order
    * size
  * sns.regplot()
    * x_estimator
    * x_bins
    * order
    * logx

#### Heatmap Plotting

  * sns.heatmap()
    * vmin
    * vmax
    * center
    * cmap
    * annot
    * fmt
    * linewidth
    * square
    * cbar
    * mask

```python
fig, ax = plt.subplots(1, 1)
mask = np.zeros_like(data.corr())
mask[np.triu_indices_from(mask)] = True
sns.heatmap(data.corr(), ax=ax, mask=mask)
plt.show()
```

#### Joint Plotting

  * sns.jointplot()
    * kind: scatter, kde, hist, hex, reg, resid
  * sns.pairplot()
    * kind: scatter, kde, hist, reg
    * diag_kind: auto, hist, kde, None
    * corner

#### Others

  * sns.boxenplot()
  * sns.swarmplot()
  * sns.stripplot()

</details>

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] Data Visualization
    * Using Texts
    * Using Colors
    * Using Facets
    * Matplotlib Tips

### 강의 영상 수강 (13:00-14:30)

  * [강의] Data Visualization
    * Seaborn Introduction
    * Seaborn Basics
    * Seaborn Advanced Topics

### Daily report 작성 (14:30-15:30)

### 주간 회고 작성 (15:30-16:00)

### Peer session (16:00-17:00)

  * 주간 팀 회고 진행
  * ResNet 논문 이야기

### Special lecture (17:00-18:00)

  * 데이터 시각화 방법론 이야기
  * 커리어 관련 이야기

### Daily report 작성 (18:00-19:00)

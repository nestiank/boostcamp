# Day20 (2022/02/11)

## 노트

### Polar Plotting

#### Matplotlib Polar Coordinates

> https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html

```python
fig, ax = plt.subplots(1, 1, subplot_kw={'projection': 'polar'})
# fig, ax = plt.subplots(1, 1, subplot_kw={'polar': True})
```

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
# ax = fig.add_subplot(111, polar=True)
```

```python
ax.set_rmin(1)
ax.set_rmin(2)
ax.set_rticks([1, 1.5, 2])
ax.set_rlabel_position(45)

ax.set_thetamin(45)
ax.set_thetamax(135)
```

```python
ax1.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
ax2.bar(theta, r, width=0.5, alpha=0.5)
ax3.plot(theta, r)
ax4.fill(theta, r)
```

#### Radar Plotting

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

stats = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
values = pokemon_data.iloc[0][stats].to_list()
theta = np.linspace(0, 2 * np.pi, 6, endpoint=False).tolist()

values.append(values[0])
theta.append(theta[0])

ax.set_thetagrids([n * 60 for n in range(6)], stats)
ax.set_theta_offset(np.pi / 2)

ax.plot(theta, values)
plt.show()
```

### Pie Chart Plotting

#### Pie Plotting

```python
labels = ['A', 'B', 'C', 'D']
data = np.array([60, 90, 45, 165])
explode = [0, 0, 0.2, 0]

fig, ax = plt.subplots(1, 1)
ax.pie(
  data, labels=labels,
  startangle=90, explode=explode, shadow=True,
  autopct='%1.1f%%', labeldistance=1.2,
  counterclock=True, radius=1.5
)
plt.show()
```

#### Donut Plotting

```python
ax.pie(data, pctdistance=0.85, textprops={'color': 'w'})
center_circle = plt.Circle((0, 0), 0.7, fc='white')
ax.add_artist(center_circle)
plt.show()
```

### Data Visualization Libraries

#### Missingno

```python
import missingno as msno

msno.matrix(data, sort='descending')
msno.bar(data)
```

#### Treemap

```python
import squarify

fig, ax = plt.subplots(1, 1)

values = [100, 200, 300, 400]
labels = ['A', 'B', 'C', 'D']
colors = ['#4285F4', '#DB4437', '#F4B400', '#0F9D58']
squarify.plot(
  values, label=labels,
  color=colors, pad=0.2,
  text_kwargs={'color':'white', 'weight':'bold'},
  ax=ax
)

ax.axis('off')
plt.show()
```

#### Waffle Chart

```python
from pywaffle import Waffle

fig = plt.figure(
  FigureClass=Waffle,
  rows=5,
  columns=10,
  values=data,
  starting_location='SW',
  vertical=True,
  block_arranging_style='snake',
  icons='child',
  icon_legend=True,
  cmap_name='tab10',
  legend={
    'loc': 'upper left',
    'bbox_to_anchor': (0, -0.4),
    'ncol': len(data),
    'framealpha': 0
  }
)
plt.show()
```

#### Venn

```python
from matplotlib_venn import venn3

v = venn3(
  subsets={'001': 100, '010': 100, '011': 100, '100': 100, '101': 100, '110': 100, '111': 100},
  set_labels=('C', 'B', 'A')
)
for id in ['001', '010', '011', '100', '101', '110', '111']:
  v.get_label_by_id(id).set_text(id)
```

```python
from matplotlib_venn import venn3

set1 = set(['A', 'B', 'C', 'D'])
set2 = set(['B', 'C', 'D', 'E'])
set3 = set(['C', 'D',' E', 'F', 'G'])
venn3([set1, set2, set3], ('Set1', 'Set2', 'Set3'))
```

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] Data Visualization
    * Polar Coordinates
    * Pie Charts
    * Data Visualization Libraries

### 주간 회고 작성 (13:00-13:30)

### 어제의 daily report 보충 (13:30-15:00)

### Extended peer session (15:00-16:00)

  * Ice-breaking
  * 팀별 학습 방식 공유

### Peer session (16:00-17:00)

  * 다른 팀의 상황 공유
  * 주간 팀 회고 진행

### Special lecture (17:00-18:00)

### Daily report 작성 (18:00-19:00)

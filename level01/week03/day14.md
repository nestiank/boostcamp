# Day14 (2022/02/03)

## 노트

### Bar Plotting

```python
group = data.groupby('grade')['age'].value_counts().sort_index()
group_cnt = data['grade'].value_counts().sort_index()
```

#### Multiple Bar Plotting

```python
fig, axes = plt.subplots(1, 2)
axes[0].bar(group['A'].index, group['A'], color='blue')
axes[1].bar(group['B'].index, group['B'], color='red')
ax.legend()
plt.show()
```

#### Stacked Bar Plotting

```python
fig, axes = plt.subplots(1, 2)
axes[0].bar(group_cnt.index, group_cnt, color='darkgray')
axes[1].bar(group['A'].index, group['A'], color='blue')
axes[1].bar(group['B'].index, group['B'], bottom=group['A'], color='red')
ax.legend()
plt.show()
```

#### Percentage Bar Plotting

```python
fig, ax = plt.subplots(1, 1)
total = group['A'] + group['B']
ax.barh(group['A'].index, group['A'] / total, color='blue')
ax.barh(group['B'].index, group['B'] / total, left=group['A'] / total, color='red')
ax.legend()
plt.show()
```

#### Overlapped Bar Plotting

```python
fig, ax = plt.subplots(1, 1)
ax.bar(group['A'].index, group['A'], color='blue', alpha=0.5)
ax.bar(group['B'].index, group['B'], color='red', alpha=0.5)
ax.legend()
plt.show()
```

#### Grouped Bar Plotting

```python
fig, ax = plt.subplots(1, 1)
idx = np.arange(len(group['A'].index))
width = 0.35
score_var = student.groupby('grade').std().T
ax.bar(idx - width / 2, group['A'], yerr=score_var['A'], capsize=10, color='blue', width=width)
ax.bar(idx + width / 2, group['B'], yerr=score_var['B'], capsize=10, color='red', width=width)
ax.legend()
plt.show()
```

### Line Plotting

#### matplotlib.ticker.MultipleLocator

```python
from matplotlib.ticker import MultipleLocator
fig, ax = plt.subplots(1, 1)
ax.plot(x, y, marker='o', linewidth=2)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
```

#### Interpolation

```python
from scipy.interpolate import make_interp_spline
import matplotlib.dates as dates

fig, ax = plt.subplots(1, 1)

# Using date as index
date = data.index
date_num = dates.date2num(date)
date_num_uniform = np.linspace(date_num.min(), date_num.max(), 50)
date_uniform = dates.num2date(date_num_uniform)

spl = make_interp_spline(date_num, data['score'], k=3)
ax.plot(date_uniform, spl(date_num_uniform))
plt.show()
```

#### Using Double Axes

  * twinx()

```python
fig, ax1 = plt.subplots(1, 1)
ax1.plot(data.index, data['score'])
ax2 = ax1.twinx()
ax2.plot(data.index, data['age'])
plt.show()
```

  * secondary-xaxis()

> https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html

```python
def deg2rad(x):
  return x * np.pi / 180

def rad2deg(x):
  # Inverse transformation of deg2rad()
  return x * 180 / np.pi

fig, ax = plt.subplots(1, 1)
ax.plot(x, y)
ax.set_xlabel('Angle [deg]')
ax.set_ylabel('Signal')
secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('Angle [rad]')
plt.show()
```

### Scatter Plotting

#### Facet Grid

```python
fig, axes = plt.subplots(4, 4)
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

for i, feat1 in enumerate(features):
  for j, feat2 in enumerate(features):
    if i <= j:
      axes[i][j].set_visible(False)
    else:
      for species in iris['Species'].unique():
        iris_sub = iris[iris['Species'] == species]
        axes[i][j].scatter(x=iris_sub[feat2], y=iris_sub[feat1], label=species, alpha=0.5)
      if i == 3:
        axes[i][j].set_xlabel(feat2)
      if j == 0:
        axes[i][j].set_ylabel(feat1)

plt.tight_layout()
plt.show()
```

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] Data Visualization
    * Lecture Overview
    * Elements of Data Visualization
    * Matplotlib Introduction

### 강의 영상 수강 (13:00-16:00)

  * [강의] Data Visualization
    * Bar Plotting
    * Line Plotting
    * Scatter Plotting

### Peer session (16:00-17:10)

  * ResNet-34 구현 코드 공유
  * 다음 peer session 준비
    * 다음 주 월요일까지 R-CNN 구현해 오기
    * 주간 회고 양식 작성해 오기

### Daily report 작성 (17:10-19:00)

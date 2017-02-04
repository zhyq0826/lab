# 理解 semantic ui 的 grid

## fundamental concepts

**container**

A fixed width container 具有固定宽度的容器

**grid**

网格

**column**

网格的列

**row**

网格的行


## 固定宽度居中布局

semantic ui 提供容器 container 来快速实现固定宽度居中，使用 `container` 不需要任何 `grid`

```html
<div class="ui container">
    <div class="c">
        content
    </div>
</div>

```

如果需要对一段文本进行固定居中，semantic ui 提供了 `text container`

```html
<div class="ui text container">
    Sometimes you just need to put a single column of centered text on a page. A text container is a special type of container optimized for a single flowing column of text, like this instructions on this page.
</div>

```


## grid 布局


### 自动换行

grid 布局可以非常容易地实现任意行列组合的布局。如果 `column` 直接作为 `grid` 的 child，即没有 `row`，当前行占满之后会自动 flow 到下一行。

```html
<div class="ui grid">
    <div class="four wide column">
        content
    </div>
    <div class="four wide column">
        content
    </div>
    <div class="four wide column">
        content
    </div>
    <div class="four wide column">
        content
    </div>
    <!-- 换行 -->
    <div class="four wide column">
        content
    </div>
    <div class="four wide column">
        content
    </div>
    <div class="four wide column">
        content
    </div>
    <div class="four wide column">
        content
    </div>
</div>

```

`column` 不指定宽度时，默认用的是 1 个单位的宽。

### 手动换行

使用 `row` 可以强迫当前行即使内容没有占满就自动换行


```html
<div class="ui three column grid">
    <div class="column">
        
    </div>
    <!-- 换行 -->
    <div class="row">
        <div class="column">
            content
        </div>
        <div class="column">
            content
        </div>
        <div class="column">
            content
        </div>
    </div>
</div>
```

### 指定 grid 的 column count


可以在 `grid` 上指定单个 `column` 的 count，当每行的 column count 达到指定数目后就自动换行，不管有没有指定 `row`

```html
<div class="ui three column grid">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <!-- 换行 -->
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <div class="row">
        <div class="column">content</div>
        <div class="column">content</div>
        <div class="column">content</div>
        <!-- 称满一行 -->
    </div>
</div>

```


### row 内的 column 默认没有高度

```html

<div class="ui three column grid">
    <div class="row">
        <!-- height 0 -->
        <div class="column">
        </div>
        <div class="column">
        </div>
        <div class="column">
        </div>
    </div>
</div>
```

### 指定 column 的宽度

```html
<div class="ui grid">
    <div class="four wide column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
```


### 特定 grid 必须要有 row

`celled grid` `internally celled grid` `divided grid` `vertially divide grid` 都需要指定 row


```html
<div class="ui celled grid">
    <div class="row" >
        <div class="column">content</div>
        <div class="column">content</div>
        <div class="column">content</div>
    </div>
</div>

```

### 居中 column

如果 column 没有占满一行，可以使用 `ui centered grid`, `centered row`, or `centered column` 来是列居中

```
<div class="ui two column centered grid">
    <div class="column"></div>
    <div class="four column centered row">
      <div class="column">content</div>
      <div class="column">content</div>
    </div>
</div>
```

`row` 中指定的 column count 能够覆盖 grid 的 column count

### 浮动 column

left floated item should come first, and a right floated item last in its row

```html
<div class="ui grid">
    <div class="left floated six wide column">
      <div class="ui segment">
        Left floated
      </div>
    </div>
    <div class="right floated six wide column">
      <div class="ui segment">
        Right floated
      </div>
    </div>
</div>

```

### 在任意级别 grid, row, column 指定文本的对齐方式


```html
<div class="ui grid">
    <div class="right aligned eight wide column">
      right aligned column
    </div>
    <div class="left aligned eight wide column">
      left aligned column
    </div>
    <div class="center aligned two column row">
      <div class="column">
        center aligned row
      </div>
      <div class="column">
        center aligned row
      </div>
    </div>
    <div class="sixteen wide right aligned column">
      right aligned column
    </div>
</div>
```

**垂直居中对齐**

```html
<div class="ui middle aligned four column centered grid">
    <div class="row">
      <div class="column">
        <img class="ui wireframe image" src="assets/images/wireframe/image.png">
      </div>
      <div class="column">
        <img class="ui wireframe image" src="assets/images/wireframe/image.png">
        <img class="ui wireframe image" src="assets/images/wireframe/image.png">
      </div>
      <div class="column">
        <img class="ui wireframe image" src="assets/images/wireframe/image.png">
      </div>
    </div>
</div>
```


### 均分 column width

`grid` 指定 equal width 可以使 `row` 中的任意列宽度相同

```
<div class="ui equal width grid">
    <div class="row">
      <div class="column">column</div>
      <div class="column">column</div>
      <div class="column">column</div>
      <div class="column">column</div>
    </div>
    <div class="row">
      <div class="column">column</div>
      <div class="column">column</div>
      <div class="column">column</div>
    </div>
</div>
```
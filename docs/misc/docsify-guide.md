# Docsify：一个让人惊喜的文档工具

> "我感觉这个工具非常非常的好用，我感触最深的就是他不需要任何构建，速度特别快。"

这是我在使用 Docsify 时的第一感受。作为一个轻量级的文档网站生成器，Docsify 的与众不同之处在于：它不会生成静态的 `.html` 文件，而是在运行时直接加载和解析 Markdown 文件。这个特性让它在众多文档工具中脱颖而出。

## 为什么选择 Docsify？

在探索文档工具的过程中，我发现很多工具要么配置太复杂，要么构建太慢。而 Docsify 的优势恰恰在于它的简单和高效：

### 主要优势

1. **零构建，实时渲染**
   - 无需构建过程，直接加载 Markdown 文件
   - 修改文件后立即生效，开发体验好
   - 部署简单，只需要静态文件服务器

2. **轻量级**
   - 核心库体积小
   - 按需加载插件
   - 服务器负载低

3. **配置简单**
   - 一个 HTML 文件即可启动
   - Markdown 文件无需特殊格式
   - 配置直观，学习成本低

### 潜在限制

当然，任何工具都有其局限性。正如我们讨论的，Docsify 也有一些需要注意的地方：

1. **SEO 不友好**
   - 因为是客户端渲染，搜索引擎可能无法很好地索引内容
   - 对比 Jekyll、Hugo 等静态站点生成器生成的是纯 HTML，更利于 SEO

2. **首屏加载性能**
   - 需要等待 JavaScript 加载和执行
   - 大型文档站点可能加载较慢

3. **功能限制**
   - 不支持复杂的模板系统
   - 自定义主题需要 CSS/JavaScript 知识

## 快速上手

在我们的项目中，我是这样使用 Docsify 的：

### 1. 基本设置

```bash
# 安装 docsify-cli
npm i docsify-cli -g

# 创建文档目录
mkdir docs
```
要启动并查看效果，你需要：

1. 进入项目根目录
2. 运行以下命令：
```bash:docs/misc/docsify-guide.md
docsify serve docs
```
3. 打开浏览器访问: http://localhost:3000



### 2. 核心文件

项目的核心只需要两个文件：

#### index.html
这是整个站点的入口文件，包含了基本配置：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>文档标题</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: '项目名称',
      repo: '仓库地址',
      loadSidebar: true,
      subMaxLevel: 3,
      search: {
        paths: 'auto',
        placeholder: '搜索'
      }
    }
  </script>
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
</body>
</html>
```

#### _sidebar.md
这个文件定义了文档的结构，比如我们的课程笔记是这样组织的：

```markdown
* 课程笔记
  * [课程介绍](0_course_intro.md)
  * [生成式AI导论](1_intro_to_genAI.md)
  * [Prompt工程](2_prompt_engineering.md)
  ...
```

### 3. 实用插件

在使用过程中，我发现这些插件特别有用：

1. **全文搜索**（快速定位内容）
   ```html
   <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
   ```

2. **代码复制**（方便分享代码）
   ```html
   <script src="//cdn.jsdelivr.net/npm/docsify-copy-code"></script>
   ```

3. **数学公式**（对于AI课程笔记必不可少）
   ```html
   <script src="//cdn.jsdelivr.net/npm/docsify-katex@latest/dist/docsify-katex.js"></script>
   ```

## 常见问题与解决

在使用过程中，我遇到过一些常见问题，这里分享解决方案：

1. **页面显示 404**
   - 检查文件是否确实在 `docs` 目录下
   - 确认文件名和路径大小写是否匹配
   - 验证链接格式是否正确

2. **侧边栏不显示**
   - 确认 `loadSidebar: true` 配置已添加
   - 检查 `_sidebar.md` 文件存在且格式正确

3. **图片显示问题**
   - 使用相对路径
   - 确保图片文件存在
   - 检查路径大小写

## 适用场景

基于我们的实践经验，Docsify 最适合：
1. 个人笔记和学习记录（比如我们的课程笔记）
2. 小到中型的文档项目
3. 团队内部文档（SEO不是主要考虑因素时）
4. 需要快速搭建和频繁更新的文档

## 参考资源

- [Docsify 官方文档](https://docsify.js.org/)
- [Docsify 主题](https://docsify.js.org/#/themes)
- [Docsify 插件列表](https://docsify.js.org/#/plugins)

记住，选择工具的关键是要符合实际需求。对于我们的课程笔记项目来说，Docsify 的轻量级和即时预览特性正是我们所需要的。 
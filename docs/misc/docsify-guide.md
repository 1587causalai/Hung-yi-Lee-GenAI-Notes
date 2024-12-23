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
   - 确认文件名和路径大小写是否配
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

## 部署方案

在完成本地开发后，我们需要让其他人也能访问到我们的文档。GitHub Pages 是一个很好的选择，它免费、易用，而且和我们的开发流程完美集成。

### GitHub Pages 部署

有两种部署方式，这里我们介绍最简单的方式：直接从主分支的 `/docs` 目录部署。

#### 1. 准备工作
首先，确保你的仓库中包含以下文件：
- `docs/index.html`（Docsify 配置文件）
- `docs/README.md`（首页内容）
- `docs/_sidebar.md`（如果使用侧边栏）
- `docs/.nojekyll`（防止 GitHub Pages 忽略下划线开头的文件）

#### 2. 配置 index.html
这是最关键的一步，需要正确配置基础路径。在 `window.$docsify` 配置中添加：

```js
window.$docsify = {
  // ... 其他配置 ...
  basePath: '/你的仓库名/',  // 例如：'/Hung-yi-Lee-GenAI-2024-Notes/'
  nameLink: '/你的仓库名/',  // 保持和 basePath 一致
}
```

这个配置确保了在 GitHub Pages 上能正确加载资源。

#### 3. 启用 GitHub Pages
1. 进入仓库设置 Settings > Pages
2. 在 "Source" 部分选择 "Deploy from a branch"
3. 在 "Branch" 部分选择主分支（通常是 `master` 或 `main`）
4. 在文件夹下拉菜单中选择 `/docs`
5. 点击 Save

#### 4. 访问你的站点
- 部署完成后，你的文档会在 `https://<username>.github.io/<repository>` 上线
- 例如：`https://1587causalai.github.io/Hung-yi-Lee-GenAI-2024-Notes/`

#### 5. 常见问题解决
如果遇到 404 错误，通常是以下原因之一：
- 没有正确设置 `basePath`
- 没有创建 `.nojekyll` 文件
- 没有选择正确的部署分支或目录
- 文件路径大小写不匹配（GitHub Pages 区分大小写）

### 进阶部署方案

如果你需要更复杂的部署流程（比如构建步骤），可以考虑使用 GitHub Actions。主要步骤是：

1. 创建 `.github/workflows/deploy.yml` 文件
2. 配置工作流以部署到 `gh-pages` 分支
3. 在 GitHub Pages 设置中选择 `gh-pages` 分支

但对于大多数文档项目来说，直接从 `/docs` 目录部署已经足够了。

记住，无论选择哪种部署方案，Docsify 的零构建特性都能让部署过程变得更加简单和快速。 
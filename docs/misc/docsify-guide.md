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
   - 确认文件名和路径大小写是否���配
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

### GitHub Pages 自动部署

#### 1. 准备工作
首先，确保你的仓库中包含以下文件：
- `index.html`（Docsify 配置文件）
- `README.md`（首页内容）
- `_sidebar.md`（如果使用侧边栏）
- `.nojekyll`（防止 GitHub Pages 忽略下划线开头的文件）

#### 2. 创建 GitHub Actions 工作流
在仓库根目录创建 `.github/workflows/deploy.yml` 文件：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main  # 或者是你的默认分支

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16'

      - name: Install Dependencies
        run: npm install -g docsify-cli

      - name: Build
        run: |
          # 如果需要构建步骤，可以在这里添加
          echo "No build step required for Docsify"

      - name: Deploy
        uses: JamesIves/github-pages-deploy-action@v4
        with:
          branch: gh-pages  # 部署到 gh-pages 分支
          folder: .         # 部署整个目录
          clean: true      # 清理旧文件
```

#### 3. 启用 GitHub Pages
1. 进入仓库设置 Settings > Pages
2. Source 选择 "Deploy from a branch"
3. Branch 选择 "gh-pages" 分支，文件夹选择 "/ (root)"
4. 点击 Save

#### 4. 自动部署流程
当你推送代码到 main 分支时：
1. GitHub Actions 会自动触发部署工作流
2. 工作流会创建/更新 gh-pages 分支
3. GitHub Pages 会自动从 gh-pages 分支部署网站
4. 部署完成后可以通过 `https://<username>.github.io/<repository>` 访问

#### 5. 私有仓库说明
对于私有仓库，你需要：
- 升级到 GitHub Pro/Team/Enterprise
- 或者使用其他部署方案（如 Vercel、Netlify）
- 或者考虑使用 GitLab（支持私有仓库的 Pages）

#### 6. 自定义域名（可选）
如果你想使用自己的域名：
1. 在仓库设置中添加自定义域名
2. 创建 `CNAME` 文件，内容为你的域名
3. 在域名提供商处添加相应的 DNS 记录

#### 7. 部署检查
部署完成后，你可以：
- 在 Actions 标签页查看部署状态
- 在 Settings > Pages 查看部署 URL
- 检查 gh-pages 分支是否正确更新

### 其他部署选项

除了 GitHub Pages，还有其他一些流行的部署选项：

1. **Vercel**
   - 支持自动部署
   - 提供免费的 SSL 证书
   - 全球 CDN 加速

2. **Netlify**
   - 简单的拖放部署
   - 自动构建和部署
   - 提供免费套餐

3. **GitLab Pages**
   - 支持私有仓库
   - 集成 CI/CD
   - 配置灵活

选择哪种部署方案主要取决于你的具体需求：
- 如果是开源项目，GitHub Pages 是最简单的选择
- 如果需要更好的访问速度，可以考虑 Vercel 或 Netlify
- 如果是私有项目，可以考虑 GitLab Pages 或付费方案

记住，无论选择哪种部署方案，Docsify 的零构建特性都能让部署过程变得更加简单和快速。 
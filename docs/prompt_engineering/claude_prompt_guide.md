# Thu Jan 02 2025 12:23:31

## Claude 官方提示词工程指南学习笔记

今天读到了 Claude 的官方提示词工程文档 https://docs.anthropic.com/zh-CN/docs/build-with-claude/prompt-engineering/overview，以下是重要内容整理。

### 1. 提示词工程技术框架

Claude 官方建议按照以下顺序尝试这些技术（从最基础到专门）：

1. 提示生成器
2. 保持清晰直接
3. 使用示例（多样本）
4. 让 Claude 思考（思维链）
5. 使用 XML 标签
6. 给 Claude 一个角色（系统提示）
7. 预填充 Claude 的响应
8. 链接复杂提示
9. 长上下文提示

### 2. 实用工具与资源

1. **官方模板库**：
   - 地址：https://docs.anthropic.com/zh-CN/prompt-library/library
   - 提供了大量可以直接参考的官方提示词模板

2. **提示词生成工具**：
   - Colab 地址：https://colab.research.google.com/drive/1SoAajN8CBYTl79VyTwxtxncfCWlHlyy9
   - 使用步骤：
     - 复制到自己的 Drive
     - 输入 API key
     - 输入任务描述
     - 可选：指定输入变量
     - 运行获取生成的提示词

3. **官方项目资源**：
   - 详细教程：https://github.com/anthropics/courses
   - 示例代码库：https://github.com/anthropics/anthropic-cookbook

### 3. 关键技术要点

#### 3.1 提示词模板与变量

在 Anthropic Console 中使用 `{{双括号}}` 作为变量占位符，例如：
```text
Translate this text from English to Spanish: {{text}}
```

**补充说明**：不同平台的占位符约定：
- Anthropic Claude：`{{变量名}}`
- OpenAI：`<变量名>` 或 `[变量名]`
- 常见模板引擎：`${变量名}` 或 `%变量名%`

#### 3.2 系统角色提示

通过 system 参数给 Claude 分配角色可以显著提升性能。这种技术被称为角色提示，是使用系统提示的最有效方式。这个概念对个性化对齐研究特别有价值。

#### 3.3 预填充响应

通过预填充 Assistant 消息可以：
- 引导回复方向
- 跳过不必要的前言
- 强制使用特定格式（如 JSON/XML）
- 帮助保持角色一致性

#### 3.4 复杂任务处理

![复杂任务处理建议](https://s2.loli.net/2025/01/02/pt3OQZgPTieMrEB.png)

对于复杂任务：
1. 将任务拆分为多个步骤
2. 每个步骤使用单独的提示
3. 将前一步的输出作为下一步的输入

#### 3.5 长文本处理策略

**最佳实践**：
- 将长文档（20K+ tokens）放在提示的顶部
- 将具体指令和问题放在末尾

**原因说明**：
1. 让模型先建立完整的上下文理解
2. 确保最后的指令能获得直接关注
3. 避免长文本干扰指令的执行
4. 在保持上下文的同时确保准确执行最新指令

### 4. 提示词工程原则

![提示词工程原则](https://s2.loli.net/2025/01/02/7dwxpAWq1EQXBgh.png)

这张图总结了核心原则，值得反复参考。

### 5. Metaprompt 概念与工具

#### 5.1 Metaprompt 简介
Metaprompt 是一个包含多个优质提示示例的长提示词，这些示例帮助 Claude 为特定任务生成合适的提示词。这是一个很有创新性的概念，可以帮助生成更高质量的提示词。

#### 5.2 官方提示词生成器
Claude 官方提供了一个基于 Metaprompt 的提示词生成工具：
- Colab 链接：https://colab.research.google.com/drive/1SoAajN8CBYTl79VyTwxtxncfCWlHlyy9
- 工具特点：
  - 使用 Metaprompt 技术
  - 包含多个高质量提示词示例
  - 可以为特定任务自动生成合适的提示词
  - 遵循提示词工程最佳实践

#### 5.3 使用方法
1. **准备工作**：
   - 在 Google Drive 中创建副本（File -> Save a copy in Drive）
   - 准备好 Anthropic API key

2. **配置步骤**：
   - 在指定位置输入 API key
   - 在 "Replace with your task!" 处输入您的任务
   - 可选：在变量部分指定输入变量（使用大写字母，用逗号分隔）

3. **运行方式**：
   - 方法一：点击 "Runtime -> Run all" 运行所有单元格
   - 方法二：选择特定单元格，按 Shift + Enter 运行

4. **查看结果**：
   - 生成的提示词将显示在笔记本底部
   - 可以直接复制使用或根据需要调整

#### 5.4 工作原理
Metaprompt 通过以下方式工作：
1. 收集了多个高质量提示词示例
2. 这些示例展示了不同任务类型的最佳实践
3. Claude 分析这些示例，理解其结构和模式
4. 基于理解，为新任务生成类似的高质量提示词

这个工具特别适合：
- 不确定如何编写提示词的新手
- 需要快速生成高质量提示词的场景
- 想要学习提示词最佳实践的用户
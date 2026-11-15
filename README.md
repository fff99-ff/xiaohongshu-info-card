# 小红书信息卡（xiaohongshu-info-card）

把任意研究报告、文章、观点转化为小红书风格信息卡图文笔记的完整工作流 + 设计系统。

## 功能

- 统一设计系统：低饱和暖色 + 奶油底 + 5 级字体层级
- 完整卡片组件库：封面 / 数字卡 / 信息块 / 判断块 / 步骤链 / 进度条 / 引言
- 截图导出脚本：Selenium + Chrome headless → PNG（960×1280 @2x）
- 发布文案模板 + 半自动存草稿工作流

## 快速开始

1. 复制 `template.html` 为你的卡片文件
2. 按 `design-system.md` 规范填充内容（3-4 个内容组/页）
3. 运行截图脚本导出 PNG：

```bash
python screenshot.py
```

4. 输出发布文案 → 上传小红书

## 目录结构

```
xiaohongshu-info-card/
├── SKILL.md           # 技能定义与工作流
├── design-system.md   # 设计规范（配色/字体/版式/组件）
├── template.html      # 标准卡片模板
├── screenshot.py      # 截图导出脚本
└── examples/          # 成品示例
```

## 示例

见 `examples/` 目录（Anthropic 报告信息卡 P01-P09）。

## License

MIT

# 主页素材与维护

本仓库为 `by-lastime` 的 GitHub Profile README。项目简介以对应公开仓库和作者提供的项目经历为依据。

## 当前设计

2026-11-07 更新：二维 macOS 窗口风格：黑灰底色、细边框、轻微半透明层次、系统字体与蓝绿代码高亮；正面平面布局，不使用透视或实体产品渲染。正文使用 GitHub 原生 Markdown/HTML，按三列三排紧凑展示九个项目，图片随单元格宽度缩放，文案只保留简介、入口与状态；顶部导航与完整课程目录均为可点击文本。页面底色仍由访客的 GitHub 主题控制。

| 素材 | 来源与用途 |
| --- | --- |
| `assets/header-macos-2d.png` | 内置 imagegen 生成的二维 macOS 窗口个人横幅 |
| `assets/ia-gs-studio.png` | 作者公开仓库 `by-lastime/IA-GS` 的 `assets/screenshots/studio.png`，实际应用截图；保留原样 |
| `assets/course-notes-macos-2d.png` | imagegen 生成，四门课程的代码编辑器概念视觉 |
| `assets/bilibili-mcp-macos-2d.png` | imagegen 生成，MCP 终端概念视觉；并非实际命令输出截图 |
| `assets/vocabulary-macos-2d.png` | imagegen 生成，词汇学习概念视觉；并非应用界面或真实学习数据 |
| `assets/writing-skill-macos-2d.png` | imagegen 生成，中文写作协作概念视觉 |
| `assets/solar-filament-macos-2d.png` | imagegen 生成，太阳暗条分割示意；不是真实观测或实验结果 |
| `assets/cat-intent-macos-2d.png` | imagegen 生成，姿态与音频示意；不是真实推理结果 |
| `assets/math-bank-macos-2d.png` | imagegen 生成，数学题目与方法关联概念视觉 |
| `assets/research-workflow-macos-2d.png` | imagegen 生成，科研学习流程概念视觉 |
| `assets/image-prompts.json` | 当前九张生成图片（横幅与八张项目配图）的完整提示词 |

本次使用内置图片生成工具。工具没有提供模型选择或具体版本确认，故不把产物标记为已经核实的“Image 2.6”。生成图保留原始 PNG，不裁切、不重绘；所有引用素材均存放在本仓库。

历史 SVG、上一版 `*-code.png` 与 `scripts/build-assets.py` 保留供回溯；当前 README 不再引用旧横幅或旧项目示意图。运行该脚本只会生成历史素材，不会更新当前 PNG。

## 内容维护

- 九个主展示项为 IA’GS、课程笔记、B 站 MCP、阳阳不忘词、Codex × DeepSeek 写作 Skill、太阳暗条实例分割、猫类意图识别、高中数学题库、科研工作流。
- 猫类意图识别链接到主页已有研究进展；其余入口使用已核实的公开仓库或课程目录。
- 课程目录收录当前公开的 AI 数学、DSA、ICS、VCI 四个笔记仓库。新增课程时同步更新目录、课程数量与配图说明。
- 项目阶段以对应仓库为准；不要把概念配图标成实际截图或把展示仓库称为完整开源应用。
- 研究经历和职责沿用作者已提供的事实，不添加未经核实的数据、成果或角色。
- 修改后检查 GitHub Markdown 渲染、所有锚点、图片与项目链接，并检查桌面和手机视口。
- 个人资料页的导航链接使用实站生成的 `#user-content-标题` 锚点；只检查 Markdown API 预览不足以确认跳转，须在个人资料页实际点击复验。

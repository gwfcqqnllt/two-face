# [AIU创智部二面实战]

##项目简介
[基于 Ollama 部署了本地大模型，通过扣子构建智能体，跑通了 YOLO模型训练，实现了前端摄像头实时目标检测推理。]

##功能特性
-本地大模型部署（Ollama）
-智能体搭建（扣子）
-YOLO 模型训练（Ultralytics）
-YOLO 实时推理部署（Python）

##项目目录结构
├── docs/                       # 项目文档与记录
│   ├── screenshots/            # 存放运行截图、测试效果图
│   ├── LOG.md                  # 开发日志
│   └── coze_api.md             # 扣子API对接记录
├── llm/                        # 大模型与智能体相关代码
│   ├── coze_cli.py             # 交互式 CLI 主入口
│   ├── test_ollama.py          # 本地 Ollama 测试脚本
│   └── requirements.txt        # Python 依赖清单
├── yolo/                       # YOLO 目标检测相关代码
│   ├── ai_director.py          # 整合 YOLO 与大模型的调度脚本
│   ├── app.py                  # Web 端
│   └── predict_image.py        # 单张图片推理脚本
├── .gitignore               
├── README.md                   # 项目说明文档（就是你正在写的东西）

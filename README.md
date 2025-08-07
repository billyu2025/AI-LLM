# AI Multimodal App Monorepo

本仓库采用 Nx 作为 monorepo 工具，结构如下：

```
ai-multimodal-app/
├── apps/
│   ├── web/        # Web前端（React/TS）
│   └── app/        # 移动端（Flutter）
├── services/
│   ├── api-gateway/
│   ├── llm-gpt/
│   ├── llm-gemini/
│   ├── llm-claude/
│   ├── multimodal/
│   └── user/
├── libs/
│   ├── shared/
│   └── ui/
├── scripts/
├── docker-compose.yaml
├── nx.json
├── workspace.json
├── package.json
└── README.md
```

## 快速开始

1. 初始化依赖：`npm install`
2. 各服务/端详细说明请见对应目录 README
3. 本地服务编排：`docker-compose up`
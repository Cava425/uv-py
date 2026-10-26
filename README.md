# uv-py

Python 3.12 学习项目，使用 [uv](https://docs.astral.sh/uv/) 管理，并已配置 Jupyter 环境（JupyterLab + ipykernel）。

## 启动 Jupyter

1. 安装依赖：

   ```bash
   uv sync
   ```

2. 启动 JupyterLab（浏览器会自动打开）：

   ```bash
   uv run jupyter lab
   ```

   指定 notebook 目录：`uv run jupyter lab --notebook-dir=notebooks`

   如需经典界面：`uv run jupyter notebook`（需先 `uv add notebook`）。

3. 在终端输出的链接（含 token）中访问，默认地址为 <http://localhost:8888>。按 `Ctrl+C` 两次可停止服务。

Notebook 文件存放于 `notebooks/` 目录。新增依赖请使用 `uv add <package>`。

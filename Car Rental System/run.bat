@echo off
SET "VENV=venv"  REM 设置虚拟环境的名称
SET "PROJECT=%~dp0"  REM 获取当前脚本所在的目录
SET "PYTHON=python"  REM 如果需要，可以指定完整的 Python 路径
SET "SRC=%PROJECT%src"  REM src 目录的路径

REM 创建虚拟环境
echo Creating virtual environment...
%PYTHON% -m venv "%PROJECT%%VENV%"

REM 激活虚拟环境
call "%PROJECT%%VENV%\Scripts\activate.bat"

REM 检查 src 目录和 main.py 文件是否存在
if not exist "%SRC%\main.py" (
    echo Error: main.py not found in the src directory.
)

REM 运行 main.py 文件
echo Running main.py...
%PYTHON% "%SRC%\main.py"
pause

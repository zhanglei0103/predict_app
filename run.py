import os
import sys
import streamlit.web.cli as stcli

def resolve_path(path):
    """处理打包后的路径问题"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的可执行文件
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
    else:
        # 如果是本地开发环境
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path

if __name__ == "__main__":
    # 获取 app.py 的绝对路径
    app_path = resolve_path("app.py")
    
    # 模拟命令行参数执行 streamlit
    sys.argv = [
        "streamlit", 
        "run", 
        app_path, 
        "--global.developmentMode=false", 
        "--browser.gatherUsageStats=false"
    ]
    sys.exit(stcli.main())
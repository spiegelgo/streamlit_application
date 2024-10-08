import subprocess
from concurrent.futures import ThreadPoolExecutor

def get_version(package):
    result = subprocess.run(["pip", "show", package], capture_output=True, text=True, check=True)
    print(f"Result for {package}:\n{result.stdout}")  # 디버깅 출력 
    if result.stdout:
        for line in result.stdout.splitlines():
            if line.startswith("Version:"):
                return f"{package}=={line.split(':')[1].strip()}"
    return None


# 패키지 목록을 읽어옵니다
packages = [
    "altair",
    "anyio",
    "argon2-cffi",
    "argon2-cffi-bindings",
    "asttokens",
    "async-lru",
    "attrs",
    "Babel",
    "beautifulsoup4",
    "bleach",
    "blinker",
    "Bottleneck",
    "Brotli",
    "cachetools",
    "certifi",
    "cffi",
    "charset-normalizer",
    "click",
    "colorama",
    "comm",
    "contourpy",
    "cycler",
    "debugpy",
    "decorator",
    "defusedxml",
    "exceptiongroup",
    "executing",
    "fastjsonschema",
    "fonttools",
    "gitdb",
    "GitPython",
    "idna",
    "ipykernel",
    "ipython",
    "ipywidgets",
    "jedi",
    "Jinja2",
    "joblib",
    "json5",
    "jsonschema",
    "jsonschema-specifications",
    "jupyter",
    "jupyter-console",
    "jupyter-events",
    "jupyter-lsp",
    "jupyter_client",
    "jupyter_core",
    "jupyter_server",
    "jupyter_server_terminals",
    "jupyterlab",
    "jupyterlab-pygments",
    "jupyterlab-widgets",
    "jupyterlab_server",
    "kiwisolver",
    "markdown-it-py",
    "MarkupSafe",
    "matplotlib",
    "matplotlib-inline",
    "mdurl",
    "mistune",
    "mkl-fft",
    "mkl-random",
    "mkl-service",
    "nbclient",
    "nbconvert",
    "nbformat",
    "nest-asyncio",
    "notebook",
    "notebook_shim",
    "numexpr",
    "numpy",
    "overrides",
    "packaging",
    "pandas",
    "pandocfilters",
    "parso",
    "patsy",
    "pillow",
    "platformdirs",
    "plotly",
    "plotly-express",
    "ply",
    "prometheus-client",
    "prompt-toolkit",
    "protobuf",
    "psutil",
    "pure-eval",
    "pyarrow",
    "pycparser",
    "pydeck",
    "Pygments",
    "pyparsing",
    "PyQt5",
    "PyQt5-sip",
    "PySocks",
    "python-dateutil",
    "python-json-logger",
    "pytz",
    "pywin32",
    "pywinpty",
    "PyYAML",
    "pyzmq",
    "qtconsole",
    "QtPy",
    "referencing",
    "requests",
    "rfc3339-validator",
    "rfc3986-validator",
    "rich",
    "rpds-py",
    "scikit-learn",
    "scipy",
    "seaborn",
    "Send2Trash",
    "sip",
    "six",
    "smmap",
    "sniffio",
    "soupsieve",
    "stack-data",
    "statsmodels",
    "streamlit",
    "tenacity",
    "terminado",
    "threadpoolctl",
    "tinycss2",
    "toml",
    "tomli",
    "toolz",
    "tornado",
    "traitlets",
    "typing_extensions",
    "tzdata",
    "unicodedata2",
    "urllib3",
    "watchdog",
    "wcwidth",
    "webencodings",
    "websocket-client",
    "widgetsnbextension",
    "win-inet-pton"
]

with ThreadPoolExecutor() as executor:
    versions = list(executor.map(get_version, packages))

with open('requirements.txt', 'w') as f:
    for version in versions:
        if version:
            f.write(f"{version}\n")
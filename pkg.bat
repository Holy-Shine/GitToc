@REM call conda remove -y -n installer --all
@REM call conda create -y --name installer python=3.7
call conda activate installer
call pip install -r requirements.txt
call pyinstaller -F -w -i ./icon.ico gitToc_GUI.py
call conda deactivate installer